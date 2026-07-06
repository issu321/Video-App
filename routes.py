import os
import uuid
from datetime import datetime
from threading import Thread
from flask import (
    Blueprint, render_template, redirect, url_for, request,
    flash, current_app, send_from_directory, abort
)
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db, bcrypt
from models import User, VideoProject, ProjectImage
from video_utils import generate_video, allowed_file, secure_unique_filename

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm', '')

        if not all([username, email, password, confirm]):
            flash('All fields are required', 'error')
            return redirect(url_for('auth.register'))

        if password != confirm:
            flash('Passwords do not match', 'error')
            return redirect(url_for('auth.register'))

        if len(password) < 6:
            flash('Password must be at least 6 characters', 'error')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('auth.register'))

        user = User(
            username=username,
            email=email,
            password_hash=bcrypt.generate_password_hash(password).decode('utf-8')
        )
        db.session.add(user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            flash('Please enter both username and password', 'error')
            return redirect(url_for('auth.login'))

        user = User.query.filter_by(username=username).first()

        if not user or not bcrypt.check_password_hash(user.password_hash, password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('auth.login'))

        login_user(user, remember=True)
        next_page = request.args.get('next')
        if next_page and next_page.startswith('/'):
            return redirect(next_page)
        return redirect(url_for('main.dashboard'))

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('main.home'))

@main_bp.route('/')
def index():
    return redirect(url_for('main.home'))

@main_bp.route('/home')
def home():
    return render_template('home.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    projects = VideoProject.query.filter_by(user_id=current_user.id)        .order_by(VideoProject.created_at.desc()).all()
    return render_template('dashboard.html', projects=projects)

@main_bp.route('/new_project', methods=['GET', 'POST'])
@login_required
def new_project():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        audio = request.files.get('audio')
        images = request.files.getlist('images')

        if not title:
            flash('Project title is required', 'error')
            return redirect(url_for('main.new_project'))

        if not audio or audio.filename == '':
            flash('Audio file is required', 'error')
            return redirect(url_for('main.new_project'))

        if not images or all(img.filename == '' for img in images):
            flash('At least one image is required', 'error')
            return redirect(url_for('main.new_project'))

        if not allowed_file(audio.filename, current_app.config['ALLOWED_AUDIO_EXTENSIONS']):
            flash('Invalid audio file format. Supported: MP3, WAV, AAC, OGG, FLAC, M4A, WMA', 'error')
            return redirect(url_for('main.new_project'))

        audio_filename = secure_unique_filename(current_app.config['UPLOAD_FOLDER_AUDIO'], audio.filename)
        audio_path = os.path.join(current_app.config['UPLOAD_FOLDER_AUDIO'], audio_filename)
        audio.save(audio_path)

        project = VideoProject(
            user_id=current_user.id,
            title=title,
            audio_file=audio_filename,
            status='pending'
        )
        db.session.add(project)
        db.session.flush()

        image_paths = []

        for i, image in enumerate(images):
            if image and image.filename != '' and allowed_file(image.filename, current_app.config['ALLOWED_IMAGE_EXTENSIONS']):
                img_filename = secure_unique_filename(current_app.config['UPLOAD_FOLDER_IMAGES'], image.filename)
                img_path = os.path.join(current_app.config['UPLOAD_FOLDER_IMAGES'], img_filename)
                image.save(img_path)
                image_paths.append(img_path)

                pi = ProjectImage(
                    project_id=project.id,
                    filename=img_filename,
                    order_index=i
                )
                db.session.add(pi)

        if not image_paths:
            db.session.rollback()
            if os.path.exists(audio_path):
                os.remove(audio_path)
            flash('At least one valid image file is required', 'error')
            return redirect(url_for('main.new_project'))

        db.session.commit()

        project.status = 'processing'
        db.session.commit()

        output_filename = f"output_{project.id}_{uuid.uuid4().hex[:8]}.mp4"
        output_path = os.path.join(current_app.config['UPLOAD_FOLDER_OUTPUT'], output_filename)

        def process_video_async(app, project_id, audio_path, image_paths, output_path):
            with app.app_context():
                proj = VideoProject.query.get(project_id)
                try:
                    generate_video(
                        audio_path,
                        image_paths,
                        output_path,
                        resolution=app.config['VIDEO_RESOLUTION'],
                        fps=app.config['VIDEO_FPS'],
                        transition=app.config['VIDEO_TRANSITION_SECONDS']
                    )
                    proj.output_file = os.path.basename(output_path)
                    proj.status = 'completed'
                    proj.completed_at = datetime.utcnow()
                except Exception as e:
                    proj.status = 'failed'
                    proj.error_message = str(e)
                finally:
                    db.session.commit()

        thread = Thread(
            target=process_video_async,
            args=(current_app._get_current_object(), project.id, audio_path, image_paths, output_path)
        )
        thread.daemon = True
        thread.start()

        return redirect(url_for('main.processing', project_id=project.id))

    return render_template('new_project.html')

@main_bp.route('/processing/<int:project_id>')
@login_required
def processing(project_id):
    project = VideoProject.query.get_or_404(project_id)
    if project.user_id != current_user.id:
        abort(403)

    if project.status == 'completed':
        return redirect(url_for('main.result', project_id=project.id))
    elif project.status == 'failed':
        flash(f'Video generation failed: {project.error_message}', 'error')
        return redirect(url_for('main.dashboard'))

    return render_template('processing.html', project=project)

@main_bp.route('/result/<int:project_id>')
@login_required
def result(project_id):
    project = VideoProject.query.get_or_404(project_id)
    if project.user_id != current_user.id:
        abort(403)

    if project.status == 'processing':
        return redirect(url_for('main.processing', project_id=project.id))
    elif project.status == 'failed':
        flash(f'Video generation failed: {project.error_message}', 'error')
        return redirect(url_for('main.dashboard'))

    return render_template('result.html', project=project)

@main_bp.route('/video/<int:project_id>')
@login_required
def serve_video(project_id):
    project = VideoProject.query.get_or_404(project_id)
    if project.user_id != current_user.id or not project.output_file:
        abort(403)
    return send_from_directory(
        current_app.config['UPLOAD_FOLDER_OUTPUT'],
        project.output_file,
        mimetype='video/mp4'
    )

@main_bp.route('/download/<int:project_id>')
@login_required
def download(project_id):
    project = VideoProject.query.get_or_404(project_id)
    if project.user_id != current_user.id or not project.output_file:
        abort(403)

    return send_from_directory(
        current_app.config['UPLOAD_FOLDER_OUTPUT'],
        project.output_file,
        as_attachment=True,
        download_name=f"{project.title.replace(' ', '_')}.mp4"
    )

@main_bp.route('/delete/<int:project_id>', methods=['POST'])
@login_required
def delete_project(project_id):
    project = VideoProject.query.get_or_404(project_id)
    if project.user_id != current_user.id:
        abort(403)

    try:
        if project.audio_file:
            path = os.path.join(current_app.config['UPLOAD_FOLDER_AUDIO'], project.audio_file)
            if os.path.exists(path):
                os.remove(path)

        if project.output_file:
            path = os.path.join(current_app.config['UPLOAD_FOLDER_OUTPUT'], project.output_file)
            if os.path.exists(path):
                os.remove(path)

        for img in project.images.all():
            path = os.path.join(current_app.config['UPLOAD_FOLDER_IMAGES'], img.filename)
            if os.path.exists(path):
                os.remove(path)
    except Exception as e:
        current_app.logger.error(f"Error deleting files: {e}")

    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully', 'success')
    return redirect(url_for('main.dashboard'))
