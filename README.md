<div align="center">

<!-- ANIMATED LOGO -->
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8b5cf6">
        <animate attributeName="stop-color" values="#8b5cf6;#f472b6;#22d3ee;#8b5cf6" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#f472b6">
        <animate attributeName="stop-color" values="#f472b6;#22d3ee;#8b5cf6;#f472b6" dur="4s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect x="10" y="10" width="100" height="100" rx="24" fill="url(#logoGrad)" filter="url(#glow)" opacity="0.9">
    <animateTransform attributeName="transform" type="rotate" from="0 60 60" to="360 60 60" dur="20s" repeatCount="indefinite"/>
  </rect>
  <rect x="10" y="10" width="100" height="100" rx="24" fill="url(#logoGrad)" opacity="0.9"/>
  <polygon points="42,35 85,60 42,85" fill="white">
    <animate attributeName="opacity" values="1;0.7;1" dur="2s" repeatCount="indefinite"/>
  </polygon>
  <circle cx="85" cy="60" r="8" fill="white" opacity="0.8">
    <animate attributeName="r" values="8;12;8" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.8;0.3;0.8" dur="2s" repeatCount="indefinite"/>
  </circle>
</svg>

<h1>
  <span style="background: linear-gradient(135deg, #8b5cf6, #f472b6, #22d3ee); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
    Video Studio
  </span>
</h1>

<p><strong>AI-Powered Video Creation Engine</strong></p>
<p>Turn your photos & audio into cinematic MP4 videos — automatically.</p>

<!-- BADGES -->
<p>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white&labelColor=0f0f1a"/>
  <img src="https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white&labelColor=0f0f1a"/>
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white&labelColor=0f0f1a"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0f0f1a"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Maintained%20by-Mohammed%20Usman-8b5cf6?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-f472b6?style=flat-square"/>
</p>

</div>

---

<br>

## 🎬 Application Workflow

<!-- ANIMATED FLOWCHART -->
<div align="center">
<svg width="900" height="320" viewBox="0 0 900 320" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="boxGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8b5cf6"/><stop offset="100%" style="stop-color:#7c3aed"/>
    </linearGradient>
    <linearGradient id="boxGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f472b6"/><stop offset="100%" style="stop-color:#ec4899"/>
    </linearGradient>
    <linearGradient id="boxGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#22d3ee"/><stop offset="100%" style="stop-color:#06b6d4"/>
    </linearGradient>
    <linearGradient id="boxGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#34d399"/><stop offset="100%" style="stop-color:#10b981"/>
    </linearGradient>
    <linearGradient id="boxGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fbbf24"/><stop offset="100%" style="stop-color:#f59e0b"/>
    </linearGradient>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#a78bfa"/>
    </marker>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#8b5cf6" flood-opacity="0.2"/>
    </filter>
  </defs>

  <!-- Background grid -->
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(139,92,246,0.05)" stroke-width="1"/>
  </pattern>
  <rect width="900" height="320" fill="url(#grid)"/>

  <!-- Nodes -->
  <g filter="url(#shadow)">
    <!-- Node 1: User -->
    <rect x="30" y="120" width="130" height="80" rx="16" fill="url(#boxGrad1)" opacity="0.9"/>
    <text x="95" y="155" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="14" font-weight="700">👤 USER</text>
    <text x="95" y="175" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-family="Inter, sans-serif" font-size="11">Registers / Login</text>
  </g>

  <!-- Node 2: Upload -->
  <g filter="url(#shadow)">
    <rect x="220" y="120" width="130" height="80" rx="16" fill="url(#boxGrad2)" opacity="0.9"/>
    <text x="285" y="155" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="14" font-weight="700">📤 UPLOAD</text>
    <text x="285" y="175" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-family="Inter, sans-serif" font-size="11">Audio + Images</text>
  </g>

  <!-- Node 3: Processing -->
  <g filter="url(#shadow)">
    <rect x="410" y="120" width="130" height="80" rx="16" fill="url(#boxGrad3)" opacity="0.9"/>
    <text x="475" y="155" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="14" font-weight="700">⚙️ PROCESS</text>
    <text x="475" y="175" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-family="Inter, sans-serif" font-size="11">FFmpeg Engine</text>
  </g>

  <!-- Node 4: Output -->
  <g filter="url(#shadow)">
    <rect x="600" y="120" width="130" height="80" rx="16" fill="url(#boxGrad4)" opacity="0.9"/>
    <text x="665" y="155" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="14" font-weight="700">🎬 OUTPUT</text>
    <text x="665" y="175" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-family="Inter, sans-serif" font-size="11">MP4 Video</text>
  </g>

  <!-- Node 5: Download -->
  <g filter="url(#shadow)">
    <rect x="790" y="120" width="100" height="80" rx="16" fill="url(#boxGrad5)" opacity="0.9"/>
    <text x="840" y="155" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="14" font-weight="700">⬇️ GET</text>
    <text x="840" y="175" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-family="Inter, sans-serif" font-size="11">Download</text>
  </g>

  <!-- Animated connection lines -->
  <path d="M160 160 L220 160" stroke="url(#boxGrad1)" stroke-width="3" fill="none" marker-end="url(#arrow)" opacity="0.6">
    <animate attributeName="stroke-dasharray" values="0,200;200,0" dur="2s" repeatCount="indefinite"/>
  </path>
  <path d="M350 160 L410 160" stroke="url(#boxGrad2)" stroke-width="3" fill="none" marker-end="url(#arrow)" opacity="0.6">
    <animate attributeName="stroke-dasharray" values="0,200;200,0" dur="2s" begin="0.4s" repeatCount="indefinite"/>
  </path>
  <path d="M540 160 L600 160" stroke="url(#boxGrad3)" stroke-width="3" fill="none" marker-end="url(#arrow)" opacity="0.6">
    <animate attributeName="stroke-dasharray" values="0,200;200,0" dur="2s" begin="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M730 160 L790 160" stroke="url(#boxGrad4)" stroke-width="3" fill="none" marker-end="url(#arrow)" opacity="0.6">
    <animate attributeName="stroke-dasharray" values="0,200;200,0" dur="2s" begin="1.2s" repeatCount="indefinite"/>
  </path>

  <!-- Floating particles -->
  <circle cx="190" cy="140" r="4" fill="#a78bfa" opacity="0.6">
    <animate attributeName="cy" values="140;120;140" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0;0.6" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="380" cy="180" r="3" fill="#f472b6" opacity="0.6">
    <animate attributeName="cy" values="180;200;180" dur="2.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0;0.6" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="570" cy="140" r="4" fill="#22d3ee" opacity="0.6">
    <animate attributeName="cy" values="140;120;140" dur="3.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0;0.6" dur="3.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="760" cy="180" r="3" fill="#34d399" opacity="0.6">
    <animate attributeName="cy" values="180;200;180" dur="2.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0;0.6" dur="2.8s" repeatCount="indefinite"/>
  </circle>

  <!-- Status labels below -->
  <text x="95" y="240" text-anchor="middle" fill="#64748b" font-family="Inter, sans-serif" font-size="10">Auth / Session</text>
  <text x="285" y="240" text-anchor="middle" fill="#64748b" font-family="Inter, sans-serif" font-size="10">Multi-part Form</text>
  <text x="475" y="240" text-anchor="middle" fill="#64748b" font-family="Inter, sans-serif" font-size="10">Background Thread</text>
  <text x="665" y="240" text-anchor="middle" fill="#64748b" font-family="Inter, sans-serif" font-size="10">1280×720 MP4</text>
  <text x="840" y="240" text-anchor="middle" fill="#64748b" font-family="Inter, sans-serif" font-size="10">Stream / Download</text>

  <!-- Animated pulse rings around nodes -->
  <circle cx="95" cy="160" r="50" fill="none" stroke="#8b5cf6" stroke-width="1" opacity="0">
    <animate attributeName="r" values="50;70" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.3;0" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="475" cy="160" r="50" fill="none" stroke="#22d3ee" stroke-width="1" opacity="0">
    <animate attributeName="r" values="50;70" dur="2s" begin="0.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.3;0" dur="2s" begin="0.5s" repeatCount="indefinite"/>
  </circle>
</svg>
</div>

<br>

---

<br>

## 🧠 Neural Video Generation Engine

<!-- NEURAL BRAIN WORKFLOW -->
<div align="center">
<svg width="900" height="500" viewBox="0 0 900 500" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="neuralGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8b5cf6"/><stop offset="100%" style="stop-color:#a78bfa"/>
    </linearGradient>
    <linearGradient id="neuralGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f472b6"/><stop offset="100%" style="stop-color:#f9a8d4"/>
    </linearGradient>
    <linearGradient id="neuralGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#22d3ee"/><stop offset="100%" style="stop-color:#67e8f9"/>
    </linearGradient>
    <linearGradient id="neuralGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#34d399"/><stop offset="100%" style="stop-color:#6ee7b7"/>
    </linearGradient>
    <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#8b5cf6;stop-opacity:0.4"/>
      <stop offset="100%" style="stop-color:#8b5cf6;stop-opacity:0"/>
    </radialGradient>
    <filter id="blur">
      <feGaussianBlur stdDeviation="2"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="900" height="500" fill="#0a0a0f"/>
  <pattern id="neuralGrid" width="50" height="50" patternUnits="userSpaceOnUse">
    <path d="M 50 0 L 0 0 0 50" fill="none" stroke="rgba(139,92,246,0.03)" stroke-width="1"/>
  </pattern>
  <rect width="900" height="500" fill="url(#neuralGrid)"/>

  <!-- Title -->
  <text x="450" y="40" text-anchor="middle" fill="#f1f5f9" font-family="Space Grotesk, sans-serif" font-size="22" font-weight="700">
    Video Generation Neural Core
  </text>
  <text x="450" y="65" text-anchor="middle" fill="#64748b" font-family="Inter, sans-serif" font-size="12">
    Real-time processing pipeline visualization
  </text>

  <!-- INPUT LAYER -->
  <text x="100" y="110" text-anchor="middle" fill="#a78bfa" font-family="Inter, sans-serif" font-size="13" font-weight="600">INPUT LAYER</text>

  <!-- Input Nodes -->
  <g>
    <circle cx="60" cy="150" r="28" fill="url(#neuralGrad1)" opacity="0.9">
      <animate attributeName="r" values="28;30;28" dur="3s" repeatCount="indefinite"/>
    </circle>
    <text x="60" y="155" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="10" font-weight="600">Audio</text>
    <circle cx="60" cy="150" r="40" fill="none" stroke="#8b5cf6" stroke-width="1" opacity="0">
      <animate attributeName="r" values="28;50" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.4;0" dur="2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <g>
    <circle cx="140" cy="150" r="28" fill="url(#neuralGrad1)" opacity="0.9">
      <animate attributeName="r" values="28;30;28" dur="3s" begin="0.5s" repeatCount="indefinite"/>
    </circle>
    <text x="140" y="155" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="10" font-weight="600">Images</text>
    <circle cx="140" cy="150" r="40" fill="none" stroke="#8b5cf6" stroke-width="1" opacity="0">
      <animate attributeName="r" values="28;50" dur="2s" begin="0.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.4;0" dur="2s" begin="0.5s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- HIDDEN LAYER 1: Analysis -->
  <text x="300" y="110" text-anchor="middle" fill="#f472b6" font-family="Inter, sans-serif" font-size="13" font-weight="600">ANALYSIS LAYER</text>

  <g>
    <circle cx="260" cy="150" r="24" fill="url(#neuralGrad2)" opacity="0.9">
      <animate attributeName="r" values="24;26;24" dur="2.5s" repeatCount="indefinite"/>
    </circle>
    <text x="260" y="154" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="9" font-weight="600">Duration</text>
  </g>
  <g>
    <circle cx="300" cy="190" r="24" fill="url(#neuralGrad2)" opacity="0.9">
      <animate attributeName="r" values="24;26;24" dur="2.5s" begin="0.3s" repeatCount="indefinite"/>
    </circle>
    <text x="300" y="194" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="9" font-weight="600">Count</text>
  </g>
  <g>
    <circle cx="340" cy="150" r="24" fill="url(#neuralGrad2)" opacity="0.9">
      <animate attributeName="r" values="24;26;24" dur="2.5s" begin="0.6s" repeatCount="indefinite"/>
    </circle>
    <text x="340" y="154" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="9" font-weight="600">Format</text>
  </g>

  <!-- HIDDEN LAYER 2: Processing Core -->
  <text x="500" y="110" text-anchor="middle" fill="#22d3ee" font-family="Inter, sans-serif" font-size="13" font-weight="600">PROCESSING CORE</text>

  <!-- Central Core -->
  <circle cx="500" cy="170" r="50" fill="url(#coreGlow)" opacity="0.6">
    <animate attributeName="r" values="50;70;50" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0.2;0.6" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="500" cy="170" r="35" fill="url(#neuralGrad3)" opacity="0.95">
    <animate attributeName="r" values="35;38;35" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="500" y="175" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="700">FFmpeg</text>

  <!-- Orbiting nodes around core -->
  <g>
    <circle cx="500" cy="110" r="18" fill="#0a0a0f" stroke="#22d3ee" stroke-width="2">
      <animateTransform attributeName="transform" type="rotate" from="0 500 170" to="360 500 170" dur="8s" repeatCount="indefinite"/>
    </circle>
    <text x="500" y="114" text-anchor="middle" fill="#22d3ee" font-family="Inter, sans-serif" font-size="8">Resize</text>
  </g>
  <g>
    <circle cx="560" cy="170" r="18" fill="#0a0a0f" stroke="#22d3ee" stroke-width="2">
      <animateTransform attributeName="transform" type="rotate" from="120 500 170" to="480 500 170" dur="8s" repeatCount="indefinite"/>
    </circle>
    <text x="560" y="174" text-anchor="middle" fill="#22d3ee" font-family="Inter, sans-serif" font-size="8">Crossfade</text>
  </g>
  <g>
    <circle cx="500" cy="230" r="18" fill="#0a0a0f" stroke="#22d3ee" stroke-width="2">
      <animateTransform attributeName="transform" type="rotate" from="240 500 170" to="600 500 170" dur="8s" repeatCount="indefinite"/>
    </circle>
    <text x="500" y="234" text-anchor="middle" fill="#22d3ee" font-family="Inter, sans-serif" font-size="8">Merge</text>
  </g>

  <!-- HIDDEN LAYER 3: Encoding -->
  <text x="700" y="110" text-anchor="middle" fill="#34d399" font-family="Inter, sans-serif" font-size="13" font-weight="600">ENCODING LAYER</text>

  <g>
    <circle cx="660" cy="150" r="24" fill="url(#neuralGrad4)" opacity="0.9">
      <animate attributeName="r" values="24;26;24" dur="2.5s" repeatCount="indefinite"/>
    </circle>
    <text x="660" y="154" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="9" font-weight="600">H.264</text>
  </g>
  <g>
    <circle cx="700" cy="190" r="24" fill="url(#neuralGrad4)" opacity="0.9">
      <animate attributeName="r" values="24;26;24" dur="2.5s" begin="0.3s" repeatCount="indefinite"/>
    </circle>
    <text x="700" y="194" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="9" font-weight="600">AAC</text>
  </g>
  <g>
    <circle cx="740" cy="150" r="24" fill="url(#neuralGrad4)" opacity="0.9">
      <animate attributeName="r" values="24;26;24" dur="2.5s" begin="0.6s" repeatCount="indefinite"/>
    </circle>
    <text x="740" y="154" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="9" font-weight="600">MP4</text>
  </g>

  <!-- OUTPUT LAYER -->
  <text x="840" y="110" text-anchor="middle" fill="#fbbf24" font-family="Inter, sans-serif" font-size="13" font-weight="600">OUTPUT</text>
  <g>
    <rect x="800" y="135" width="80" height="50" rx="12" fill="url(#neuralGrad5)" opacity="0.9">
      <animate attributeName="opacity" values="0.9;1;0.9" dur="2s" repeatCount="indefinite"/>
    </rect>
    <text x="840" y="164" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="700">MP4</text>
  </g>

  <!-- Animated connections -->
  <g opacity="0.4">
    <!-- Input to Analysis -->
    <path d="M88 150 Q170 150 236 150" stroke="#a78bfa" stroke-width="2" fill="none">
      <animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" repeatCount="indefinite"/>
    </path>
    <path d="M168 150 Q220 170 276 180" stroke="#a78bfa" stroke-width="1.5" fill="none">
      <animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" begin="0.2s" repeatCount="indefinite"/>
    </path>

    <!-- Analysis to Core -->
    <path d="M284 150 Q390 150 465 150" stroke="#f472b6" stroke-width="2" fill="none">
      <animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" begin="0.3s" repeatCount="indefinite"/>
    </path>
    <path d="M324 150 Q410 160 465 165" stroke="#f472b6" stroke-width="1.5" fill="none">
      <animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" begin="0.5s" repeatCount="indefinite"/>
    </path>

    <!-- Core to Encoding -->
    <path d="M535 160 Q590 150 636 150" stroke="#22d3ee" stroke-width="2" fill="none">
      <animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" begin="0.6s" repeatCount="indefinite"/>
    </path>
    <path d="M535 175 Q590 180 636 180" stroke="#22d3ee" stroke-width="1.5" fill="none">
      <animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" begin="0.8s" repeatCount="indefinite"/>
    </path>

    <!-- Encoding to Output -->
    <path d="M764 150 Q780 150 800 160" stroke="#34d399" stroke-width="2" fill="none">
      <animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" begin="0.9s" repeatCount="indefinite"/>
    </path>
  </g>

  <!-- Data flow particles -->
  <circle r="3" fill="#a78bfa">
    <animateMotion path="M88 150 Q170 150 236 150" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <circle r="3" fill="#f472b6">
    <animateMotion path="M284 150 Q390 150 465 150" dur="1.5s" begin="0.5s" repeatCount="indefinite"/>
  </circle>
  <circle r="3" fill="#22d3ee">
    <animateMotion path="M535 160 Q590 150 636 150" dur="1.5s" begin="1s" repeatCount="indefinite"/>
  </circle>
  <circle r="3" fill="#34d399">
    <animateMotion path="M764 150 Q780 150 800 160" dur="1.5s" begin="1.3s" repeatCount="indefinite"/>
  </circle>

  <!-- Bottom info panel -->
  <rect x="50" y="280" width="800" height="180" rx="16" fill="rgba(255,255,255,0.02)" stroke="rgba(139,92,246,0.1)" stroke-width="1"/>

  <text x="450" y="310" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="14" font-weight="600">Core Processing Parameters</text>

  <!-- Parameter bars -->
  <g transform="translate(100, 340)">
    <text x="0" y="0" fill="#64748b" font-family="Inter, sans-serif" font-size="11">Resolution</text>
    <rect x="0" y="8" width="200" height="8" rx="4" fill="rgba(139,92,246,0.1)"/>
    <rect x="0" y="8" width="180" height="8" rx="4" fill="url(#neuralGrad1)">
      <animate attributeName="width" values="0;180" dur="2s" repeatCount="indefinite"/>
    </rect>
    <text x="210" y="16" fill="#a78bfa" font-family="Inter, sans-serif" font-size="10">1280×720</text>
  </g>

  <g transform="translate(100, 370)">
    <text x="0" y="0" fill="#64748b" font-family="Inter, sans-serif" font-size="11">Frame Rate</text>
    <rect x="0" y="8" width="200" height="8" rx="4" fill="rgba(244,114,182,0.1)"/>
    <rect x="0" y="8" width="160" height="8" rx="4" fill="url(#neuralGrad2)">
      <animate attributeName="width" values="0;160" dur="2s" begin="0.3s" repeatCount="indefinite"/>
    </rect>
    <text x="210" y="16" fill="#f472b6" font-family="Inter, sans-serif" font-size="10">24 FPS</text>
  </g>

  <g transform="translate(100, 400)">
    <text x="0" y="0" fill="#64748b" font-family="Inter, sans-serif" font-size="11">Transition</text>
    <rect x="0" y="8" width="200" height="8" rx="4" fill="rgba(34,211,238,0.1)"/>
    <rect x="0" y="8" width="80" height="8" rx="4" fill="url(#neuralGrad3)">
      <animate attributeName="width" values="0;80" dur="2s" begin="0.6s" repeatCount="indefinite"/>
    </rect>
    <text x="210" y="16" fill="#22d3ee" font-family="Inter, sans-serif" font-size="10">0.5s</text>
  </g>

  <g transform="translate(500, 340)">
    <text x="0" y="0" fill="#64748b" font-family="Inter, sans-serif" font-size="11">Audio Codec</text>
    <rect x="0" y="8" width="200" height="8" rx="4" fill="rgba(52,211,153,0.1)"/>
    <rect x="0" y="8" width="190" height="8" rx="4" fill="url(#neuralGrad4)">
      <animate attributeName="width" values="0;190" dur="2s" begin="0.9s" repeatCount="indefinite"/>
    </rect>
    <text x="210" y="16" fill="#34d399" font-family="Inter, sans-serif" font-size="10">AAC</text>
  </g>

  <g transform="translate(500, 370)">
    <text x="0" y="0" fill="#64748b" font-family="Inter, sans-serif" font-size="11">Video Codec</text>
    <rect x="0" y="8" width="200" height="8" rx="4" fill="rgba(139,92,246,0.1)"/>
    <rect x="0" y="8" width="185" height="8" rx="4" fill="url(#neuralGrad1)">
      <animate attributeName="width" values="0;185" dur="2s" begin="1.2s" repeatCount="indefinite"/>
    </rect>
    <text x="210" y="16" fill="#a78bfa" font-family="Inter, sans-serif" font-size="10">H.264</text>
  </g>

  <g transform="translate(500, 400)">
    <text x="0" y="0" fill="#64748b" font-family="Inter, sans-serif" font-size="11">Output Format</text>
    <rect x="0" y="8" width="200" height="8" rx="4" fill="rgba(251,191,36,0.1)"/>
    <rect x="0" y="8" width="195" height="8" rx="4" fill="url(#neuralGrad5)">
      <animate attributeName="width" values="0;195" dur="2s" begin="1.5s" repeatCount="indefinite"/>
    </rect>
    <text x="210" y="16" fill="#fbbf24" font-family="Inter, sans-serif" font-size="10">MP4</text>
  </g>

  <!-- Live indicator -->
  <circle cx="830" cy="305" r="5" fill="#34d399">
    <animate attributeName="opacity" values="1;0.3;1" dur="1s" repeatCount="indefinite"/>
  </circle>
  <text x="845" y="310" fill="#34d399" font-family="Inter, sans-serif" font-size="10">Live Processing</text>
</svg>
</div>

<br>

---

<br>

## 🏗️ System Architecture

<!-- ARCHITECTURE DIAGRAM -->
<div align="center">
<svg width="900" height="420" viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="archGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#8b5cf6;stop-opacity:0.3"/>
      <stop offset="100%" style="stop-color:#8b5cf6;stop-opacity:0.05"/>
    </linearGradient>
    <linearGradient id="archGrad2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#22d3ee;stop-opacity:0.3"/>
      <stop offset="100%" style="stop-color:#22d3ee;stop-opacity:0.05"/>
    </linearGradient>
    <linearGradient id="archGrad3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#f472b6;stop-opacity:0.3"/>
      <stop offset="100%" style="stop-color:#f472b6;stop-opacity:0.05"/>
    </linearGradient>
    <linearGradient id="archGrad4" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#34d399;stop-opacity:0.3"/>
      <stop offset="100%" style="stop-color:#34d399;stop-opacity:0.05"/>
    </linearGradient>
    <marker id="archArrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L0,8 L8,4 z" fill="#64748b"/>
    </marker>
  </defs>

  <rect width="900" height="420" fill="#0a0a0f"/>
  <pattern id="archGrid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(139,92,246,0.03)" stroke-width="1"/>
  </pattern>
  <rect width="900" height="420" fill="url(#archGrid)"/>

  <text x="450" y="35" text-anchor="middle" fill="#f1f5f9" font-family="Space Grotesk, sans-serif" font-size="20" font-weight="700">System Architecture</text>

  <!-- Client Layer -->
  <rect x="50" y="60" width="800" height="80" rx="12" fill="url(#archGrad1)" stroke="rgba(139,92,246,0.2)" stroke-width="1"/>
  <text x="80" y="85" fill="#a78bfa" font-family="Inter, sans-serif" font-size="12" font-weight="700">🖥️ CLIENT LAYER</text>

  <rect x="80" y="95" width="120" height="35" rx="8" fill="rgba(139,92,246,0.15)" stroke="#8b5cf6" stroke-width="1"/>
  <text x="140" y="117" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11">Browser</text>

  <rect x="220" y="95" width="120" height="35" rx="8" fill="rgba(139,92,246,0.15)" stroke="#8b5cf6" stroke-width="1"/>
  <text x="280" y="117" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11">HTML/CSS/JS</text>

  <rect x="360" y="95" width="120" height="35" rx="8" fill="rgba(139,92,246,0.15)" stroke="#8b5cf6" stroke-width="1"/>
  <text x="420" y="117" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11">Jinja2 Templates</text>

  <rect x="500" y="95" width="120" height="35" rx="8" fill="rgba(139,92,246,0.15)" stroke="#8b5cf6" stroke-width="1"/>
  <text x="560" y="117" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11">Glassmorphism UI</text>

  <!-- Application Layer -->
  <rect x="50" y="160" width="800" height="100" rx="12" fill="url(#archGrad2)" stroke="rgba(34,211,238,0.2)" stroke-width="1"/>
  <text x="80" y="185" fill="#22d3ee" font-family="Inter, sans-serif" font-size="12" font-weight="700">⚙️ APPLICATION LAYER</text>

  <rect x="80" y="200" width="140" height="45" rx="8" fill="rgba(34,211,238,0.15)" stroke="#22d3ee" stroke-width="1"/>
  <text x="150" y="220" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">Flask App</text>
  <text x="150" y="235" text-anchor="middle" fill="#67e8f9" font-family="Inter, sans-serif" font-size="9">app.py</text>

  <rect x="240" y="200" width="140" height="45" rx="8" fill="rgba(34,211,238,0.15)" stroke="#22d3ee" stroke-width="1"/>
  <text x="310" y="220" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">Routes</text>
  <text x="310" y="235" text-anchor="middle" fill="#67e8f9" font-family="Inter, sans-serif" font-size="9">routes.py</text>

  <rect x="400" y="200" width="140" height="45" rx="8" fill="rgba(34,211,238,0.15)" stroke="#22d3ee" stroke-width="1"/>
  <text x="470" y="220" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">Video Engine</text>
  <text x="470" y="235" text-anchor="middle" fill="#67e8f9" font-family="Inter, sans-serif" font-size="9">video_utils.py</text>

  <rect x="560" y="200" width="140" height="45" rx="8" fill="rgba(34,211,238,0.15)" stroke="#22d3ee" stroke-width="1"/>
  <text x="630" y="220" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">Auth System</text>
  <text x="630" y="235" text-anchor="middle" fill="#67e8f9" font-family="Inter, sans-serif" font-size="9">Bcrypt + CSRF</text>

  <rect x="720" y="200" width="110" height="45" rx="8" fill="rgba(34,211,238,0.15)" stroke="#22d3ee" stroke-width="1"/>
  <text x="775" y="220" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">Config</text>
  <text x="775" y="235" text-anchor="middle" fill="#67e8f9" font-family="Inter, sans-serif" font-size="9">config.py</text>

  <!-- Data Layer -->
  <rect x="50" y="280" width="800" height="100" rx="12" fill="url(#archGrad3)" stroke="rgba(244,114,182,0.2)" stroke-width="1"/>
  <text x="80" y="305" fill="#f472b6" font-family="Inter, sans-serif" font-size="12" font-weight="700">🗄️ DATA LAYER</text>

  <rect x="80" y="320" width="140" height="45" rx="8" fill="rgba(244,114,182,0.15)" stroke="#f472b6" stroke-width="1"/>
  <text x="150" y="340" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">SQLite</text>
  <text x="150" y="355" text-anchor="middle" fill="#f9a8d4" font-family="Inter, sans-serif" font-size="9">app.db</text>

  <rect x="240" y="320" width="140" height="45" rx="8" fill="rgba(244,114,182,0.15)" stroke="#f472b6" stroke-width="1"/>
  <text x="310" y="340" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">SQLAlchemy</text>
  <text x="310" y="355" text-anchor="middle" fill="#f9a8d4" font-family="Inter, sans-serif" font-size="9">ORM Models</text>

  <rect x="400" y="320" width="140" height="45" rx="8" fill="rgba(244,114,182,0.15)" stroke="#f472b6" stroke-width="1"/>
  <text x="470" y="340" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">File Storage</text>
  <text x="470" y="355" text-anchor="middle" fill="#f9a8d4" font-family="Inter, sans-serif" font-size="9">uploads/</text>

  <!-- External Layer -->
  <rect x="50" y="400" width="800" height="60" rx="12" fill="url(#archGrad4)" stroke="rgba(52,211,153,0.2)" stroke-width="1"/>
  <text x="80" y="420" fill="#34d399" font-family="Inter, sans-serif" font-size="12" font-weight="700">🔌 EXTERNAL SERVICES</text>

  <rect x="80" y="430" width="140" height="35" rx="8" fill="rgba(52,211,153,0.15)" stroke="#34d399" stroke-width="1"/>
  <text x="150" y="452" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">FFmpeg</text>

  <rect x="240" y="430" width="140" height="35" rx="8" fill="rgba(52,211,153,0.15)" stroke="#34d399" stroke-width="1"/>
  <text x="310" y="452" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="11" font-weight="600">Subprocess</text>

  <!-- Animated connections between layers -->
  <line x1="450" y1="140" x2="450" y2="160" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#archArrow)" opacity="0.5">
    <animate attributeName="stroke-dashoffset" values="0;10" dur="1s" repeatCount="indefinite"/>
  </line>
  <line x1="450" y1="260" x2="450" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#archArrow)" opacity="0.5">
    <animate attributeName="stroke-dashoffset" values="0;10" dur="1s" repeatCount="indefinite"/>
  </line>
  <line x1="450" y1="380" x2="450" y2="400" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#archArrow)" opacity="0.5">
    <animate attributeName="stroke-dashoffset" values="0;10" dur="1s" repeatCount="indefinite"/>
  </line>
</svg>
</div>

<br>

---

<br>

## ✨ Features

<div align="center">

<!-- FEATURE CARDS SVG -->
<svg width="900" height="280" viewBox="0 0 900 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="featGrad1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#8b5cf6;stop-opacity:0.2"/><stop offset="100%" style="stop-color:#7c3aed;stop-opacity:0.1"/></linearGradient>
    <linearGradient id="featGrad2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#f472b6;stop-opacity:0.2"/><stop offset="100%" style="stop-color:#ec4899;stop-opacity:0.1"/></linearGradient>
    <linearGradient id="featGrad3" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#22d3ee;stop-opacity:0.2"/><stop offset="100%" style="stop-color:#06b6d4;stop-opacity:0.1"/></linearGradient>
    <linearGradient id="featGrad4" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#34d399;stop-opacity:0.2"/><stop offset="100%" style="stop-color:#10b981;stop-opacity:0.1"/></linearGradient>
  </defs>

  <rect width="900" height="280" fill="#0a0a0f"/>

  <!-- Card 1: Audio Sync -->
  <g transform="translate(30, 30)">
    <rect width="195" height="220" rx="16" fill="url(#featGrad1)" stroke="rgba(139,92,246,0.3)" stroke-width="1">
      <animate attributeName="stroke-opacity" values="0.3;0.6;0.3" dur="3s" repeatCount="indefinite"/>
    </rect>
    <circle cx="97" cy="50" r="30" fill="rgba(139,92,246,0.2)" stroke="#8b5cf6" stroke-width="1">
      <animate attributeName="r" values="30;32;30" dur="3s" repeatCount="indefinite"/>
    </circle>
    <text x="97" y="58" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="20">🎵</text>
    <text x="97" y="100" text-anchor="middle" fill="#f1f5f9" font-family="Inter, sans-serif" font-size="13" font-weight="700">Audio Sync</text>
    <text x="97" y="125" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">Auto-calculates image</text>
    <text x="97" y="140" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">duration from audio</text>
    <text x="97" y="155" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">track length</text>
  </g>

  <!-- Card 2: Transitions -->
  <g transform="translate(245, 30)">
    <rect width="195" height="220" rx="16" fill="url(#featGrad2)" stroke="rgba(244,114,182,0.3)" stroke-width="1">
      <animate attributeName="stroke-opacity" values="0.3;0.6;0.3" dur="3s" begin="0.5s" repeatCount="indefinite"/>
    </rect>
    <circle cx="97" cy="50" r="30" fill="rgba(244,114,182,0.2)" stroke="#f472b6" stroke-width="1">
      <animate attributeName="r" values="30;32;30" dur="3s" begin="0.5s" repeatCount="indefinite"/>
    </circle>
    <text x="97" y="58" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="20">✨</text>
    <text x="97" y="100" text-anchor="middle" fill="#f1f5f9" font-family="Inter, sans-serif" font-size="13" font-weight="700">Smooth Transitions</text>
    <text x="97" y="125" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">Elegant crossfade</text>
    <text x="97" y="140" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">effects between every</text>
    <text x="97" y="155" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">image frame</text>
  </g>

  <!-- Card 3: Smart Resize -->
  <g transform="translate(460, 30)">
    <rect width="195" height="220" rx="16" fill="url(#featGrad3)" stroke="rgba(34,211,238,0.3)" stroke-width="1">
      <animate attributeName="stroke-opacity" values="0.3;0.6;0.3" dur="3s" begin="1s" repeatCount="indefinite"/>
    </rect>
    <circle cx="97" cy="50" r="30" fill="rgba(34,211,238,0.2)" stroke="#22d3ee" stroke-width="1">
      <animate attributeName="r" values="30;32;30" dur="3s" begin="1s" repeatCount="indefinite"/>
    </circle>
    <text x="97" y="58" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="20">🖼️</text>
    <text x="97" y="100" text-anchor="middle" fill="#f1f5f9" font-family="Inter, sans-serif" font-size="13" font-weight="700">Smart Resizing</text>
    <text x="97" y="125" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">Intelligent center-crop</text>
    <text x="97" y="140" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">to 1280×720 HD</text>
    <text x="97" y="155" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">resolution</text>
  </g>

  <!-- Card 4: Secure -->
  <g transform="translate(675, 30)">
    <rect width="195" height="220" rx="16" fill="url(#featGrad4)" stroke="rgba(52,211,153,0.3)" stroke-width="1">
      <animate attributeName="stroke-opacity" values="0.3;0.6;0.3" dur="3s" begin="1.5s" repeatCount="indefinite"/>
    </rect>
    <circle cx="97" cy="50" r="30" fill="rgba(52,211,153,0.2)" stroke="#34d399" stroke-width="1">
      <animate attributeName="r" values="30;32;30" dur="3s" begin="1.5s" repeatCount="indefinite"/>
    </circle>
    <text x="97" y="58" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-size="20">🔒</text>
    <text x="97" y="100" text-anchor="middle" fill="#f1f5f9" font-family="Inter, sans-serif" font-size="13" font-weight="700">Secure & Private</text>
    <text x="97" y="125" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">Bcrypt encryption,</text>
    <text x="97" y="140" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">CSRF protection,</text>
    <text x="97" y="155" text-anchor="middle" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">auto file cleanup</text>
  </g>
</svg>

</div>

<br>

---

<br>

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

<br>

---

<br>

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

<br>

---

<br>

## ⚙️ Configuration

Edit `config.py` to customize:

| Parameter | Default | Description |
|---|---|---|
| `VIDEO_RESOLUTION` | `1280x720` | Output video dimensions |
| `VIDEO_FPS` | `24` | Frames per second |
| `VIDEO_TRANSITION_SECONDS` | `0.5` | Crossfade duration |
| `MAX_CONTENT_LENGTH` | `100MB` | Maximum upload size |

<br>

---

<br>

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Backend** | Flask, Python 3.8+ |
| **Database** | SQLite, SQLAlchemy ORM |
| **Auth** | Flask-Login, Flask-Bcrypt, Flask-WTF (CSRF) |
| **Video Engine** | FFmpeg (subprocess) |
| **Frontend** | HTML5, CSS3, Jinja2, Vanilla JS |
| **UI Design** | Glassmorphism, Custom Animations |

</div>

<br>

---

<br>

## 🧑‍💻 Developer

<div align="center">

<table>
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/issu321" width="100" style="border-radius: 50%;" alt="Mohammed Usman"/>
      <br>
      <strong>Mohammed Usman</strong>
      <br>
      <sub>Full Stack Developer</sub>
    </td>
  </tr>
</table>

<p>
  <a href="https://github.com/issu321"><img src="https://img.shields.io/badge/GitHub-issu321-181717?style=for-the-badge&logo=github"/></a>
  <a href="https://issu321.github.io/issu321"><img src="https://img.shields.io/badge/Portfolio-issu321.github.io-8b5cf6?style=for-the-badge&logo=google-chrome"/></a>
  <a href="mailto:jaafreeusman@gmail.com"><img src="https://img.shields.io/badge/Email-jaafreeusman@gmail.com-f472b6?style=for-the-badge&logo=gmail"/></a>
  <a href="tel:+918884294749"><img src="https://img.shields.io/badge/Phone-%2B91%208884294749-22d3ee?style=for-the-badge&logo=whatsapp"/></a>
</p>

<p>
  <a href="https://github.com/issu321/Video-App"><img src="https://img.shields.io/badge/⭐_Star_this_Repo-Video--App-8b5cf6?style=for-the-badge"/></a>
</p>

</div>

<br>

---

<br>

<div align="center">

<!-- ANIMATED FOOTER -->
<svg width="600" height="80" viewBox="0 0 600 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#8b5cf6"/>
      <stop offset="50%" style="stop-color:#f472b6"/>
      <stop offset="100%" style="stop-color:#22d3ee"/>
    </linearGradient>
  </defs>
  <text x="300" y="30" text-anchor="middle" fill="url(#footerGrad)" font-family="Space Grotesk, sans-serif" font-size="16" font-weight="700">
    Crafted with precision by Mohammed Usman
    <animate attributeName="opacity" values="0.8;1;0.8" dur="3s" repeatCount="indefinite"/>
  </text>
  <text x="300" y="55" text-anchor="middle" fill="#64748b" font-family="Inter, sans-serif" font-size="11">
    Video Studio © 2024 — All rights reserved
  </text>
  <line x1="150" y1="70" x2="450" y2="70" stroke="url(#footerGrad)" stroke-width="1" opacity="0.3">
    <animate attributeName="x1" values="150;200;150" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="x2" values="450;400;450" dur="4s" repeatCount="indefinite"/>
  </line>
</svg>

</div>
