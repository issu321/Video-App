from extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    projects = db.relationship('VideoProject', backref='user', lazy='dynamic', cascade='all, delete-orphan')

class VideoProject(db.Model):
    __tablename__ = 'video_projects'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    audio_file = db.Column(db.String(300), nullable=False)
    output_file = db.Column(db.String(300))
    status = db.Column(db.String(20), default='pending')
    error_message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    images = db.relationship('ProjectImage', backref='project', lazy='dynamic', 
                             cascade='all, delete-orphan', 
                             order_by='ProjectImage.order_index')

class ProjectImage(db.Model):
    __tablename__ = 'project_images'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('video_projects.id'), nullable=False)
    filename = db.Column(db.String(300), nullable=False)
    order_index = db.Column(db.Integer, nullable=False)
