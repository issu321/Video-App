<div align="center">

<!-- LOGO -->
<img src="https://raw.githubusercontent.com/issu321/Video-App/main/assets/logo.svg" width="120" alt="Video Studio Logo">

<h1>
  <img src="https://readme-typing-svg.herokuapp.com?font=Space+Grotesk&weight=700&size=40&pause=1000&color=8B5CF6&center=true&vCenter=true&width=500&lines=Video+Studio" alt="Video Studio">
</h1>

<p><strong>AI-Powered Video Creation Engine</strong></p>
<p>Turn your photos & audio into cinematic MP4 videos — automatically.</p>

<!-- BADGES -->
<p>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white&labelColor=0f0f1a">
  <img src="https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white&labelColor=0f0f1a">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white&labelColor=0f0f1a">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0f0f1a">
</p>

<p>
  <img src="https://img.shields.io/badge/Maintained%20by-Mohammed%20Usman-8b5cf6?style=flat-square">
  <img src="https://img.shields.io/badge/License-MIT-f472b6?style=flat-square">
</p>

</div>

---

## 🎬 Application Workflow

```mermaid
flowchart LR
    A["👤 User"] -->|Register / Login| B["📤 Upload"]
    B -->|Audio + Images| C["⚙️ Process"]
    C -->|FFmpeg Engine| D["🎬 Output"]
    D -->|MP4 Video| E["⬇️ Download"]

    style A fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff
    style B fill:#f472b6,stroke:#ec4899,stroke-width:2px,color:#fff
    style C fill:#22d3ee,stroke:#06b6d4,stroke-width:2px,color:#fff
    style D fill:#34d399,stroke:#10b981,stroke-width:2px,color:#fff
    style E fill:#fbbf24,stroke:#f59e0b,stroke-width:2px,color:#fff
```

---

## 🧠 Neural Video Generation Engine

```mermaid
flowchart TB
    subgraph INPUT["🔷 INPUT LAYER"]
        A1["🎵 Audio File"]
        A2["🖼️ Images"]
    end

    subgraph ANALYSIS["🔶 ANALYSIS LAYER"]
        B1["⏱️ Duration Calc"]
        B2["📊 Image Count"]
        B3["🔍 Format Check"]
    end

    subgraph CORE["💠 PROCESSING CORE"]
        C1["🔄 Resize 1280x720"]
        C2["✨ Crossfade FX"]
        C3["🔊 Audio Merge"]
        C4["🎬 FFmpeg Engine"]
    end

    subgraph ENCODE["🔷 ENCODING LAYER"]
        D1["📹 H.264 Video"]
        D2["🎵 AAC Audio"]
        D3["📦 MP4 Container"]
    end

    subgraph OUTPUT["⭐ OUTPUT"]
        E1["🎞️ Final MP4"]
    end

    A1 --> B1
    A2 --> B2
    A1 --> B3
    A2 --> B3

    B1 --> C4
    B2 --> C4
    B3 --> C4

    C4 --> C1
    C4 --> C2
    C4 --> C3

    C1 --> D1
    C2 --> D1
    C3 --> D2

    D1 --> D3
    D2 --> D3
    D3 --> E1

    style INPUT fill:#8b5cf620,stroke:#8b5cf6,stroke-width:2px,color:#fff
    style ANALYSIS fill:#f472b620,stroke:#f472b6,stroke-width:2px,color:#fff
    style CORE fill:#22d3ee20,stroke:#22d3ee,stroke-width:3px,color:#fff
    style ENCODE fill:#34d39920,stroke:#34d399,stroke-width:2px,color:#fff
    style OUTPUT fill:#fbbf2420,stroke:#fbbf24,stroke-width:2px,color:#fff
```

### Core Processing Parameters

| Parameter | Value | Description |
|---|---|---|
| **Resolution** | `1280×720` | HD Output |
| **Frame Rate** | `24 FPS` | Cinematic smoothness |
| **Transition** | `0.5s` | Crossfade duration |
| **Audio Codec** | `AAC` | High-quality audio |
| **Video Codec** | `H.264` | Universal compatibility |
| **Output Format** | `MP4` | Standard container |

---

## 🏗️ System Architecture

```mermaid
flowchart TB
    subgraph CLIENT["🖥️ CLIENT LAYER"]
        C1["Browser"]
        C2["HTML/CSS/JS"]
        C3["Jinja2 Templates"]
        C4["Glassmorphism UI"]
    end

    subgraph APP["⚙️ APPLICATION LAYER"]
        A1["Flask App — app.py"]
        A2["Routes — routes.py"]
        A3["Video Engine — video_utils.py"]
        A4["Auth System — Bcrypt + CSRF"]
        A5["Config — config.py"]
    end

    subgraph DATA["🗄️ DATA LAYER"]
        D1["SQLite — app.db"]
        D2["SQLAlchemy ORM"]
        D3["File Storage — uploads/"]
    end

    subgraph EXT["🔌 EXTERNAL"]
        E1["FFmpeg"]
        E2["Subprocess"]
    end

    CLIENT --> APP
    APP --> DATA
    APP --> EXT

    style CLIENT fill:#8b5cf620,stroke:#8b5cf6,stroke-width:2px,color:#fff
    style APP fill:#22d3ee20,stroke:#22d3ee,stroke-width:2px,color:#fff
    style DATA fill:#f472b620,stroke:#f472b6,stroke-width:2px,color:#fff
    style EXT fill:#34d39920,stroke:#34d399,stroke-width:2px,color:#fff
```

---

## ✨ Features

```mermaid
flowchart LR
    F1["🎵<br/>Audio Sync<br/>Auto-calculates image<br/>duration from audio<br/>track length"] 
    F2["✨<br/>Smooth Transitions<br/>Elegant crossfade<br/>effects between every<br/>image frame"]
    F3["🖼️<br/>Smart Resizing<br/>Intelligent center-crop<br/>to 1280×720 HD<br/>resolution"]
    F4["🔒<br/>Secure & Private<br/>Bcrypt encryption,<br/>CSRF protection,<br/>auto file cleanup"]

    F1 --- F2 --- F3 --- F4

    style F1 fill:#8b5cf620,stroke:#8b5cf6,stroke-width:2px,color:#fff
    style F2 fill:#f472b620,stroke:#f472b6,stroke-width:2px,color:#fff
    style F3 fill:#22d3ee20,stroke:#22d3ee,stroke-width:2px,color:#fff
    style F4 fill:#34d39920,stroke:#34d399,stroke-width:2px,color:#fff
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/issu321/Video-App.git
cd Video-App

# 2. Install FFmpeg (if not already installed)
# macOS: brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg
# Windows: Download from ffmpeg.org and add to PATH

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py

# 5. Open browser → http://localhost:5000
```

---

## 📁 Project Structure

```
Video-App/
├── app.py              # Application entry point
├── config.py           # Configuration settings
├── extensions.py       # Flask extensions (DB, Login, Bcrypt, CSRF)
├── models.py           # Database models
├── routes.py           # All application routes
├── video_utils.py      # Video generation engine (FFmpeg)
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── static/
│   └── css/
│       └── style.css   # Premium glassmorphism theme
├── templates/          # Jinja2 HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── new_project.html
│   ├── processing.html
│   └── result.html
└── uploads/            # File storage (auto-created)
    ├── audio/
    ├── images/
    └── output/
```

---

## ⚙️ Configuration

Edit `config.py` to customize:

| Parameter | Default | Description |
|---|---|---|
| `VIDEO_RESOLUTION` | `1280x720` | Output video dimensions |
| `VIDEO_FPS` | `24` | Frames per second |
| `VIDEO_TRANSITION_SECONDS` | `0.5` | Crossfade duration |
| `MAX_CONTENT_LENGTH` | `100MB` | Maximum upload size |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Flask, Python 3.8+ |
| **Database** | SQLite, SQLAlchemy ORM |
| **Auth** | Flask-Login, Flask-Bcrypt, Flask-WTF (CSRF) |
| **Video Engine** | FFmpeg (subprocess) |
| **Frontend** | HTML5, CSS3, Jinja2, Vanilla JS |
| **UI Design** | Glassmorphism, Custom Animations |

---

## 🧑‍💻 Developer

<div align="center">

**Mohammed Usman**

*Full Stack Developer*

<p>
  <a href="https://github.com/issu321">
    <img src="https://img.shields.io/badge/GitHub-issu321-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <a href="https://issu321.github.io/issu321">
    <img src="https://img.shields.io/badge/Portfolio-issu321.github.io-8b5cf6?style=for-the-badge&logo=google-chrome&logoColor=white">
  </a>
</p>

<p>
  <a href="mailto:jaafreeusman@gmail.com">
    <img src="https://img.shields.io/badge/Email-jaafreeusman@gmail.com-f472b6?style=for-the-badge&logo=gmail&logoColor=white">
  </a>
  <a href="https://wa.me/918884294749">
    <img src="https://img.shields.io/badge/Phone-%2B91%208884294749-22d3ee?style=for-the-badge&logo=whatsapp&logoColor=white">
  </a>
</p>

<p>
  <a href="https://github.com/issu321/Video-App">
    <img src="https://img.shields.io/badge/⭐_Star_this_Repo-Video--App-8b5cf6?style=for-the-badge">
  </a>
</p>

</div>

---

<div align="center">

**Crafted with precision by Mohammed Usman**

Video Studio © 2024 — All rights reserved

</div>
