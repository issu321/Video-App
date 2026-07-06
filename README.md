<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=8b5cf6,7c3aed,f472b6,22d3ee&height=200&section=header&text=Video%20Studio&fontSize=60&fontColor=ffffff&animation=twinkling&fontAlignY=35&desc=AI-Powered%20Video%20Creation%20Engine&descAlignY=55&descSize=18">

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
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#8b5cf6', 'primaryTextColor': '#fff', 'primaryBorderColor': '#7c3aed', 'lineColor': '#a78bfa', 'secondaryColor': '#f472b6', 'tertiaryColor': '#22d3ee', 'fontFamily': 'Inter'}}}%%
flowchart LR
    A["👤 User"] -->|Register / Login| B["📤 Upload"]
    B -->|Audio + Images| C["⚙️ Process"]
    C -->|FFmpeg Engine| D["🎬 Output"]
    D -->|MP4 Video| E["⬇️ Download"]

    style A fill:#8b5cf6,stroke:#7c3aed,stroke-width:3px,color:#fff
    style B fill:#f472b6,stroke:#ec4899,stroke-width:3px,color:#fff
    style C fill:#22d3ee,stroke:#06b6d4,stroke-width:3px,color:#fff
    style D fill:#34d399,stroke:#10b981,stroke-width:3px,color:#fff
    style E fill:#fbbf24,stroke:#f59e0b,stroke-width:3px,color:#fff
```

---

## 🧠 Neural Video Generation Engine

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#8b5cf6', 'primaryTextColor': '#fff', 'primaryBorderColor': '#7c3aed', 'lineColor': '#a78bfa', 'secondaryColor': '#f472b6', 'tertiaryColor': '#22d3ee', 'fontFamily': 'Inter'}}}%%
flowchart TB
    subgraph INPUT["🔷 INPUT LAYER"]
        direction LR
        A1["🎵 Audio File<br/>MP3/WAV/AAC/OGG/FLAC/M4A/WMA"]
        A2["🖼️ Images<br/>PNG/JPG/GIF/WEBP/BMP"]
    end

    subgraph ANALYSIS["🔶 ANALYSIS LAYER"]
        direction LR
        B1["⏱️ Duration Calculation<br/>audio_length / image_count"]
        B2["📊 Image Count<br/>Validate min/max"]
        B3["🔍 Format Check<br/>MIME type validation"]
    end

    subgraph CORE["💠 PROCESSING CORE — FFmpeg Engine"]
        direction TB
        C1["🔄 Resize<br/>Center-crop 1280x720"]
        C2["✨ Crossfade FX<br/>0.5s transition duration"]
        C3["🔊 Audio Merge<br/>Original track overlay"]
        C4["🎬 FFmpeg Subprocess<br/>Multi-threaded pipeline"]
    end

    subgraph ENCODE["🔷 ENCODING LAYER"]
        direction LR
        D1["📹 H.264 Video Codec<br/>libx264 encoder"]
        D2["🎵 AAC Audio Codec<br/>libfdk_aac / aac"]
        D3["📦 MP4 Container<br/>yuv420p pixel format"]
    end

    subgraph OUTPUT["⭐ OUTPUT LAYER"]
        E1["🎞️ Final MP4<br/>1280x720 @ 24fps"]
    end

    subgraph META["📋 METADATA"]
        M1["Project Title"]
        M2["Created At"]
        M3["Status: completed"]
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

    E1 --> M1
    E1 --> M2
    E1 --> M3

    style INPUT fill:#8b5cf615,stroke:#8b5cf6,stroke-width:3px,color:#fff
    style ANALYSIS fill:#f472b615,stroke:#f472b6,stroke-width:3px,color:#fff
    style CORE fill:#22d3ee15,stroke:#22d3ee,stroke-width:4px,color:#fff
    style ENCODE fill:#34d39915,stroke:#34d399,stroke-width:3px,color:#fff
    style OUTPUT fill:#fbbf2415,stroke:#fbbf24,stroke-width:3px,color:#fff
    style META fill:#a78bfa15,stroke:#a78bfa,stroke-width:2px,color:#fff
```

---

## 🧠 Neural Brain — Deep Processing Pipeline

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#8b5cf6', 'primaryTextColor': '#fff', 'primaryBorderColor': '#7c3aed', 'lineColor': '#a78bfa', 'secondaryColor': '#f472b6', 'tertiaryColor': '#22d3ee', 'fontFamily': 'Inter'}}}%%
flowchart TB
    subgraph SENSORS["🎯 SENSORY INPUT"]
        S1["👁️ Visual Cortex<br/>Image Array Parser"]
        S2["👂 Auditory Cortex<br/>Audio Waveform Analyzer"]
    end

    subgraph NEURON1["🟣 NEURON CLUSTER — Preprocessing"]
        direction TB
        N1["Normalize<br/>Color Space"]
        N2["Aspect Ratio<br/>Intelligence"]
        N3["Bitrate<br/>Analysis"]
    end

    subgraph NEURON2["🔵 NEURON CLUSTER — Temporal"]
        direction TB
        N4["Duration<br/>Per Frame"]
        N5["Keyframe<br/>Extraction"]
        N6["Sync<br/>Points"]
    end

    subgraph NEURON3["🟢 NEURON CLUSTER — Synthesis"]
        direction TB
        N7["Crossfade<br/>Matrix"]
        N8["Audio-Visual<br/>Sync"]
        N9["Render<br/>Buffer"]
    end

    subgraph BRAINSTEM["🔴 BRAINSTEM — FFmpeg Core"]
        B1["Command Builder<br/>Filter Complex"]
        B2["Subprocess<br/>Spawner"]
        B3["Progress<br/>Monitor"]
        B4["Error<br/>Handler"]
    end

    subgraph MOTOR["⚡ MOTOR OUTPUT"]
        M1["Video Stream<br/>H.264"]
        M2["Audio Stream<br/>AAC"]
        M3["MP4 Muxer<br/>Container"]
    end

    S1 --> N1
    S1 --> N2
    S2 --> N3

    N1 --> N4
    N2 --> N5
    N3 --> N6

    N4 --> N7
    N5 --> N8
    N6 --> N9

    N7 --> B1
    N8 --> B2
    N9 --> B3

    B1 --> B4
    B2 --> B4
    B3 --> B4

    B4 --> M1
    B4 --> M2
    B4 --> M3

    style SENSORS fill:#8b5cf615,stroke:#8b5cf6,stroke-width:3px,color:#fff
    style NEURON1 fill:#f472b615,stroke:#f472b6,stroke-width:3px,color:#fff
    style NEURON2 fill:#22d3ee15,stroke:#22d3ee,stroke-width:3px,color:#fff
    style NEURON3 fill:#34d39915,stroke:#34d399,stroke-width:3px,color:#fff
    style BRAINSTEM fill:#ef444415,stroke:#ef4444,stroke-width:4px,color:#fff
    style MOTOR fill:#fbbf2415,stroke:#fbbf24,stroke-width:3px,color:#fff
```

---

## 🔄 Real-Time Processing State Machine

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#8b5cf6', 'primaryTextColor': '#fff', 'primaryBorderColor': '#7c3aed', 'lineColor': '#a78bfa', 'secondaryColor': '#f472b6', 'tertiaryColor': '#22d3ee', 'fontFamily': 'Inter'}}}%%
stateDiagram-v2
    [*] --> Idle: App Start
    Idle --> Uploading: Select Files

    Uploading --> Validating: Submit Form
    Uploading --> Idle: Cancel

    Validating --> Processing: Valid
    Validating --> Error: Invalid Format

    Processing --> Analyzing: Start Thread
    Processing --> Error: Thread Fail

    Analyzing --> Resizing: Calculate Duration
    Analyzing --> Error: Zero Division

    Resizing --> Transitioning: All Images Ready
    Resizing --> Error: Corrupt Image

    Transitioning --> Merging: Crossfade Complete
    Transitioning --> Error: FFmpeg Error

    Merging --> Encoding: Audio Synced
    Merging --> Error: Audio Mismatch

    Encoding --> Completed: MP4 Ready
    Encoding --> Error: Encode Fail

    Completed --> [*]: Download
    Completed --> Cleanup: Delete Project

    Error --> Idle: Retry
    Error --> [*]: Abort

    Cleanup --> [*]: Files Removed

    state Idle {
        [*] --> Waiting
    }

    state Processing {
        [*] --> ThreadSpawn
        ThreadSpawn --> ProgressMonitor
        ProgressMonitor --> [*]
    }

    state Completed {
        [*] --> PreviewReady
        PreviewReady --> DownloadReady
    }
```

---

## 🏗️ System Architecture

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#8b5cf6', 'primaryTextColor': '#fff', 'primaryBorderColor': '#7c3aed', 'lineColor': '#a78bfa', 'secondaryColor': '#f472b6', 'tertiaryColor': '#22d3ee', 'fontFamily': 'Inter'}}}%%
flowchart TB
    subgraph CLIENT["🖥️ CLIENT LAYER"]
        direction LR
        C1["Browser<br/>Chrome/Firefox/Safari"]
        C2["HTML5/CSS3<br/>Glassmorphism UI"]
        C3["Vanilla JS<br/>Animations + Particles"]
        C4["Jinja2 Templates<br/>Server-Side Render"]
    end

    subgraph APP["⚙️ APPLICATION LAYER — Flask"]
        direction TB
        A1["app.py<br/>Application Factory"]
        A2["routes.py<br/>Blueprint Routes"]
        A3["video_utils.py<br/>FFmpeg Engine"]
        A4["models.py<br/>SQLAlchemy ORM"]
        A5["extensions.py<br/>Login + Bcrypt + CSRF"]
        A6["config.py<br/>Environment Config"]
    end

    subgraph DATA["🗄️ DATA LAYER"]
        direction TB
        D1["SQLite<br/>app.db"]
        D2["User Table<br/>id, username, password_hash"]
        D3["VideoProject Table<br/>id, title, status, timestamps"]
        D4["ProjectImage Table<br/>id, project_id, filename, order"]
        D5["File Storage<br/>uploads/audio/ images/ output/"]
    end

    subgraph EXT["🔌 EXTERNAL SERVICES"]
        direction TB
        E1["FFmpeg Binary<br/>System PATH"]
        E2["Subprocess<br/>Popen Pipeline"]
        E3["OS File System<br/>Read/Write/Delete"]
    end

    subgraph SEC["🔒 SECURITY LAYER"]
        direction TB
        S1["Bcrypt<br/>Password Hashing"]
        S2["Flask-Login<br/>Session Management"]
        S3["Flask-WTF<br/>CSRF Protection"]
        S4["Werkzeug<br/>Secure File Uploads"]
    end

    CLIENT --> APP
    APP --> DATA
    APP --> EXT
    APP --> SEC

    style CLIENT fill:#8b5cf615,stroke:#8b5cf6,stroke-width:3px,color:#fff
    style APP fill:#22d3ee15,stroke:#22d3ee,stroke-width:3px,color:#fff
    style DATA fill:#f472b615,stroke:#f472b6,stroke-width:3px,color:#fff
    style EXT fill:#34d39915,stroke:#34d399,stroke-width:3px,color:#fff
    style SEC fill:#fbbf2415,stroke:#fbbf24,stroke-width:3px,color:#fff
```

---

## ⚡ Data Flow Architecture

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#8b5cf6', 'primaryTextColor': '#fff', 'primaryBorderColor': '#7c3aed', 'lineColor': '#a78bfa', 'secondaryColor': '#f472b6', 'tertiaryColor': '#22d3ee', 'fontFamily': 'Inter'}}}%%
sequenceDiagram
    autonumber
    participant U as 👤 User
    participant B as 🌐 Browser
    participant F as ⚙️ Flask App
    participant DB as 🗄️ SQLite
    participant V as 🎬 video_utils.py
    participant FF as 🔌 FFmpeg
    participant FS as 📁 File System

    U->>B: Register / Login
    B->>F: POST /auth/login
    F->>DB: Query User
    DB-->>F: User Data
    F->>B: Set Session Cookie

    U->>B: Upload Audio + Images
    B->>F: POST /new_project
    F->>FS: Save Files
    F->>DB: Create Project (pending)
    F->>B: Redirect /processing

    par Background Thread
        F->>V: generate_video(project_id)
        V->>DB: Update Status (processing)
        V->>FF: Build Filter Complex
        FF->>FS: Read Source Files
        FF->>FF: Resize + Crossfade + Merge
        FF->>FS: Write output.mp4
        V->>DB: Update Status (completed)
    and Polling
        B->>F: GET /processing (every 5s)
        F->>DB: Check Status
        DB-->>F: Status
        F->>B: Render Page
    end

    U->>B: View Result
    B->>F: GET /result
    F->>DB: Fetch Project
    F->>B: Render Video Player

    U->>B: Download MP4
    B->>F: GET /download
    F->>FS: Stream File
    FS-->>F: Binary Data
    F->>B: File Response
    B->>U: Save to Disk

    U->>B: Delete Project
    B->>F: POST /delete
    F->>DB: Delete Records
    F->>FS: Delete Files
    F->>B: Redirect /dashboard
```

---

## ✨ Feature Matrix

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#8b5cf6', 'primaryTextColor': '#fff', 'primaryBorderColor': '#7c3aed', 'lineColor': '#a78bfa', 'secondaryColor': '#f472b6', 'tertiaryColor': '#22d3ee', 'fontFamily': 'Inter'}}}%%
flowchart LR
    subgraph FEATURES["🚀 FEATURE ENGINE"]
        direction TB
        F1["🎵 Audio Sync<br/>auto_duration = audio_length / image_count<br/>Each image gets equal time"]
        F2["✨ Crossfade FX<br/>xfade=transition<br/>duration=0.5s<br/>smooth blending"]
        F3["🖼️ Smart Resize<br/>scale=1280:720<br/>force_original_aspect_ratio=decrease<br/>pad=black"]
        F4["🔒 Security Stack<br/>Bcrypt + CSRF + LoginManager<br/>Secure file handling"]
        F5["⚡ Background Thread<br/>threading.Thread<br/>Non-blocking UI<br/>Status polling"]
        F6["📱 Responsive UI<br/>Glassmorphism CSS<br/>Mobile-first design<br/>Particle animations"]
    end

    subgraph TECH["🛠️ TECH STACK"]
        direction TB
        T1["Python 3.8+"]
        T2["Flask + Jinja2"]
        T3["SQLite + SQLAlchemy"]
        T4["FFmpeg CLI"]
        T5["Vanilla JS/CSS3"]
    end

    FEATURES --> TECH

    style FEATURES fill:#8b5cf615,stroke:#8b5cf6,stroke-width:3px,color:#fff
    style TECH fill:#22d3ee15,stroke:#22d3ee,stroke-width:3px,color:#fff
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

<img src="https://capsule-render.vercel.app/api?type=waving&color=8b5cf6,7c3aed,f472b6,22d3ee&height=100&section=footer&text=Crafted%20with%20precision%20by%20Mohammed%20Usman&fontSize=20&fontColor=ffffff&animation=twinkling">

<p align="center">
  Video Studio &copy; <span id="year"></span> — All rights reserved
</p>

<script>
  document.getElementById("year").textContent = new Date().getFullYear();
</script>

</div>
