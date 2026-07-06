import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production-2024'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER_AUDIO = os.path.join(basedir, 'uploads', 'audio')
    UPLOAD_FOLDER_IMAGES = os.path.join(basedir, 'uploads', 'images')
    UPLOAD_FOLDER_OUTPUT = os.path.join(basedir, 'uploads', 'output')

    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB total upload limit

    ALLOWED_AUDIO_EXTENSIONS = {'mp3', 'wav', 'aac', 'ogg', 'flac', 'm4a', 'wma'}
    ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

    VIDEO_RESOLUTION = (1280, 720)
    VIDEO_FPS = 24
    VIDEO_TRANSITION_SECONDS = 0.5
