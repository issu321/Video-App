import os
from flask import Flask
from config import Config
from extensions import db, login_manager, bcrypt, csrf
from models import User, VideoProject, ProjectImage
from routes import main_bp, auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(app.config['UPLOAD_FOLDER_AUDIO'], exist_ok=True)
    os.makedirs(app.config['UPLOAD_FOLDER_IMAGES'], exist_ok=True)
    os.makedirs(app.config['UPLOAD_FOLDER_OUTPUT'], exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
