import os
import subprocess
import shutil
import urllib.request
import zipfile
import platform
from config import Config

TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools')

def get_ffmpeg_path():
    """Return path to ffmpeg binary, downloading if necessary."""
    if platform.system() == 'Windows':
        ffmpeg_name = 'ffmpeg.exe'
        ffprobe_name = 'ffprobe.exe'
    else:
        ffmpeg_name = 'ffmpeg'
        ffprobe_name = 'ffprobe'

    ffmpeg_path = os.path.join(TOOLS_DIR, ffmpeg_name)
    ffprobe_path = os.path.join(TOOLS_DIR, ffprobe_name)

    # Check system PATH first
    system_ffmpeg = shutil.which('ffmpeg')
    system_ffprobe = shutil.which('ffprobe')

    if system_ffmpeg and system_ffprobe:
        return system_ffmpeg, system_ffprobe

    # Check our tools directory
    if os.path.exists(ffmpeg_path) and os.path.exists(ffprobe_path):
        return ffmpeg_path, ffprobe_path

    # Download ffmpeg binaries
    _download_ffmpeg()

    if os.path.exists(ffmpeg_path) and os.path.exists(ffprobe_path):
        return ffmpeg_path, ffprobe_path

    raise RuntimeError(
        "FFmpeg could not be downloaded or found.\n"
        "Please install FFmpeg manually from https://ffmpeg.org/download.html"
    )

def _download_ffmpeg():
    """Download pre-built ffmpeg binaries for the current platform."""
    import tempfile

    os.makedirs(TOOLS_DIR, exist_ok=True)

    if platform.system() == 'Windows':
        url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
        print("Downloading FFmpeg for Windows... (this may take a minute)")
    elif platform.system() == 'Darwin':
        url = "https://evermeet.cx/ffmpeg/ffmpeg-7.1.1.zip"
        print("Downloading FFmpeg for macOS... (this may take a minute)")
    else:
        url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
        print("Downloading FFmpeg for Linux... (this may take a minute)")

    temp_file = os.path.join(tempfile.gettempdir(), 'ffmpeg_download.zip')

    try:
        urllib.request.urlretrieve(url, temp_file)
    except Exception as e:
        raise RuntimeError(f"Failed to download FFmpeg: {e}")

    # Extract
    extract_dir = os.path.join(tempfile.gettempdir(), 'ffmpeg_extract')
    os.makedirs(extract_dir, exist_ok=True)

    if url.endswith('.zip'):
        with zipfile.ZipFile(temp_file, 'r') as z:
            z.extractall(extract_dir)
    else:
        import tarfile
        with tarfile.open(temp_file, 'r:xz') as t:
            t.extractall(extract_dir)

    # Find ffmpeg and ffprobe binaries
    for root, dirs, files in os.walk(extract_dir):
        for f in files:
            if f.lower() in ('ffmpeg.exe', 'ffmpeg'):
                shutil.copy2(os.path.join(root, f), os.path.join(TOOLS_DIR, f))
            elif f.lower() in ('ffprobe.exe', 'ffprobe'):
                shutil.copy2(os.path.join(root, f), os.path.join(TOOLS_DIR, f))

    # Cleanup
    os.remove(temp_file)
    shutil.rmtree(extract_dir, ignore_errors=True)

    # Make executable on Unix
    if platform.system() != 'Windows':
        for f in ['ffmpeg', 'ffprobe']:
            p = os.path.join(TOOLS_DIR, f)
            if os.path.exists(p):
                os.chmod(p, 0o755)

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def secure_unique_filename(upload_folder, filename):
    from werkzeug.utils import secure_filename
    import uuid
    base = secure_filename(filename)
    if '.' in base:
        name, ext = base.rsplit('.', 1)
        ext = ext.lower()
        unique = f"{name}_{uuid.uuid4().hex[:8]}.{ext}"
    else:
        unique = f"{base}_{uuid.uuid4().hex[:8]}"
    return unique

def get_audio_duration(audio_path):
    """Get audio duration in seconds using ffprobe."""
    _, ffprobe_path = get_ffmpeg_path()
    try:
        result = subprocess.run(
            [
                ffprobe_path, '-v', 'error', '-show_entries',
                'format=duration', '-of',
                'default=noprint_wrappers=1:nokey=1', audio_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        duration = float(result.stdout.strip())
        return duration
    except Exception as e:
        raise ValueError(f"Cannot determine audio duration: {str(e)}")

def resize_image(img_path, output_path, resolution):
    """Resize image to fill resolution using ffmpeg (center crop)."""
    ffmpeg_path, _ = get_ffmpeg_path()
    w, h = resolution
    try:
        subprocess.run(
            [
                ffmpeg_path, '-y', '-i', img_path,
                '-vf', f'scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:black',
                '-frames:v', '1', output_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            timeout=30
        )
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Cannot process image {os.path.basename(img_path)}: {e.stderr.decode('utf-8', errors='ignore')[:200]}")

def generate_video(audio_path, image_paths, output_path,
                   resolution=Config.VIDEO_RESOLUTION,
                   fps=Config.VIDEO_FPS,
                   transition=Config.VIDEO_TRANSITION_SECONDS):
    if not image_paths:
        raise ValueError("At least one image is required to generate video")
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    audio_duration = get_audio_duration(audio_path)
    if audio_duration <= 0:
        raise ValueError("Invalid audio duration")

    num_images = len(image_paths)
    if num_images == 1:
        img_duration = audio_duration
        transition = 0
    else:
        img_duration = (audio_duration + (num_images - 1) * transition) / num_images

    if img_duration <= 0:
        raise ValueError("Calculated image duration is invalid")

    ffmpeg_path, _ = get_ffmpeg_path()

    # Create temp directory for processed images
    import tempfile
    temp_dir = tempfile.mkdtemp(prefix="video_app_")

    try:
        # Process all images to target resolution
        processed_images = []
        for i, img_path in enumerate(image_paths):
            if not os.path.exists(img_path):
                raise FileNotFoundError(f"Image not found: {img_path}")
            out_img = os.path.join(temp_dir, f"frame_{i:04d}.jpg")
            resize_image(img_path, out_img, resolution)
            processed_images.append(out_img)

        # Build ffmpeg filter_complex for crossfade slideshow
        if num_images == 1:
            # Simple single image with audio
            filter_complex = f"[0:v]fps={fps},format=yuv420p[v]"
            input_args = ['-loop', '1', '-i', processed_images[0], '-t', str(audio_duration)]
        else:
            # Multiple images with crossfade
            inputs = []
            for img in processed_images:
                inputs.extend(['-loop', '1', '-i', img])

            # Build filter_complex
            parts = []
            for i in range(num_images):
                parts.append(f"[{i}:v]trim=duration={img_duration},setpts=PTS-STARTPTS[v{i}];")

            # Chain crossfades
            fade_d = transition
            if fade_d > 0:
                chain = f"[v0][v1]xfade=transition=fade:duration={fade_d}:offset={img_duration - fade_d}[x0];"
                for i in range(1, num_images - 1):
                    offset = (i + 1) * img_duration - (i + 1) * fade_d
                    chain += f"[x{i-1}][v{i+1}]xfade=transition=fade:duration={fade_d}:offset={offset}[x{i}];"
                chain += f"[x{num_images-2}]fps={fps},format=yuv420p[v]"
            else:
                # No transitions, just concat
                concat = ""
                for i in range(num_images):
                    concat += f"[v{i}]"
                concat += f"concat=n={num_images}:v=1:a=0[outv];[outv]fps={fps},format=yuv420p[v]"
                chain = concat

            filter_complex = "".join(parts) + chain
            input_args = inputs

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        cmd = [
            ffmpeg_path, '-y'
        ] + input_args + [
            '-i', audio_path,
            '-filter_complex', filter_complex,
            '-map', '[v]',
            '-map', str(num_images) + ':a',
            '-c:v', 'libx264',
            '-preset', 'medium',
            '-crf', '23',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-pix_fmt', 'yuv420p',
            '-shortest',
            output_path
        ]

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=300
        )

        if result.returncode != 0:
            err = result.stderr.decode('utf-8', errors='ignore')[-500:]
            raise RuntimeError(f"FFmpeg failed: {err}")

    finally:
        # Cleanup temp directory
        import shutil as sh
        if os.path.exists(temp_dir):
            sh.rmtree(temp_dir, ignore_errors=True)

    if not os.path.exists(output_path):
        raise RuntimeError("Video file was not created")

    return output_path
