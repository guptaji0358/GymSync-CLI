```markdown
<div align="center">
  <h1>🏋️ GymSync-CLI</h1>
  <p><strong>Ultra-Fast • Terminal-First • Chrome Automation Framework</strong></p>

  <pre>
   ██████╗ ██╗   ██╗███╗   ███╗███████╗██╗   ██╗███╗   ██╗ ██████╗ 
  ██╔════╝ ██║   ██║████╗ ████║██╔════╝╚██╗ ██╔╝████╗  ██║██╔════╝ 
  ██║  ███╗██║   ██║██╔████╔██║███████╗ ╚████╔╝ ██╔██╗ ██║██║  ███╗
  ██║   ██║██║   ██║██║╚██╔╝██║╚════██║  ╚██╔╝  ██║╚██╗██║██║   ██║
  ╚██████╔╝╚██████╔╝██║ ╚═╝ ██║███████║   ██║   ██║ ╚████║╚██████╔╝
   ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝ 
  </pre>

  <p><em>Direct LocalStorage Injection • Selenium Powered • Zero GUI • Production Grade Terminal Experience</em></p>

  ![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
  ![Chrome](https://img.shields.io/badge/Chrome-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
  ![License](https://img.shields.io/badge/License-MIT-00C853?style=for-the-badge)
  ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-212121?style=for-the-badge)
  ![CLI](https://img.shields.io/badge/Terminal-CLI-00E676?style=for-the-badge)

  <p>
    <a href="https://github.com/guptaji0358/GymSync-CLI/stargazers"><img src="https://img.shields.io/github/stars/guptaji0358/GymSync-CLI?style=social" alt="Stars"></a>
    <a href="https://github.com/guptaji0358/GymSync-CLI/issues"><img src="https://img.shields.io/github/issues/guptaji0358/GymSync-CLI?style=social" alt="Issues"></a>
  </p>
</div>

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Why GymSync CLI?](#why-gymsync-cli)
- [Architecture Diagram](#architecture-diagram)
- [Workflow Diagram](#workflow-diagram)
- [Core Architecture](#core-architecture)
- [Matrix Mapping](#matrix-mapping)
- [Terminal Preview](#terminal-preview)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Performance](#performance)
- [Security](#security)
- [Future Roadmap](#future-roadmap)
- [Open Source Contribution](#open-source-contribution)
- [License](#license)
- [FAQ](#faq)
- [Credits](#credits)
- [Author](#author)

---

## Project Overview

**GymSync-CLI** is a premium, high-performance command-line automation tool that revolutionizes gym schedule management. It uses Selenium WebDriver to control Google Chrome, injects data directly into LocalStorage, synchronizes the DOM in real-time, and delivers everything through a beautiful, responsive terminal interface.

No more slow web UIs. No more repetitive clicking. Just pure speed and precision from your terminal.

Built for developers, power users, and serious fitness enthusiasts who value efficiency, control, and automation.

**Key Philosophy**: Treat the browser as a programmable backend. Use the terminal as the primary interface.

---

## Features

### Core Strengths

- **⚡ LocalStorage Injection** — Writes schedule data directly into Chrome’s storage layer with atomic precision
- **🔄 DOM Synchronization** — Forces real-time UI updates after every injection
- **🛡️ Zero Traceback Protection** — Clean error handling that never leaks sensitive information
- **⏹️ Double Ctrl+C Exit** — Safe two-step graceful shutdown
- **🔒 Profile Isolation** — Dedicated Chrome profiles for every session
- **🔄 Account Recovery** — Built-in retry and fallback authentication
- **📊 Interactive Dashboard** — Rich terminal UI with live updates and keyboard navigation
- **📅 Schedule Automation** — Full weekly matrix support with custom time slots
- **🚀 Fast Runtime** — Sub-45 second complete workflows
- **🌐 Live JavaScript Injection** — Dynamic script execution engine
- **📝 Clean Structured Logging** — Color-coded, exportable logs
- **🛠️ Error Recovery** — Self-healing with intelligent retries
- **📦 Expandable Architecture** — Modular and plugin-ready design

---

## Why GymSync CLI?

Manual gym scheduling is slow, repetitive, and error-prone. GymSync-CLI delivers:

- **Speed**: Complete schedule updates in seconds instead of minutes
- **Efficiency**: Extremely low CPU & memory usage
- **Reliability**: Robust error handling and recovery
- **Flexibility**: Scriptable, version-controllable, and automation-friendly
- **Control**: Full access to browser internals via JavaScript injection

Terminal tools win when precision and speed matter.

---

## Architecture Diagram

```ascii
                     ┌─────────────────────┐
                     │       User CLI      │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │   Session Manager   │
                     └──────────┬──────────┘
                                │
                ┌───────────────┴───────────────┐
                ▼                               ▼
   ┌────────────────────┐             ┌────────────────────┐
   │   Profile Manager  │             │  Browser Controller│
   └────────────────────┘             └────────────────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │     Selenium +      │
                     │   ChromeDriver      │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │   Google Chrome     │
                     │  (Isolated Profile) │
                     └──────────┬──────────┘
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
   ┌────────────────────┐         ┌────────────────────┐
   │ JavaScript Engine  │◀───────▶│   DOM Sync Layer   │
   └────────────────────┘         └────────────────────┘
                 │
                 ▼
   ┌────────────────────┐
   │  LocalStorage      │
   │  Manipulation      │
   └────────────────────┘
```

---

## Workflow Diagram

```ascii
User → CLI Command → Validation → Chrome Launch
                    ↓
              Authentication
                    ↓
           Schedule Loading
                    ↓
         JavaScript Injection
                    ↓
         DOM + LocalStorage Sync
                    ↓
              Success Dashboard
```

---

## Core Architecture

**Session Manager** — Full lifecycle control  
**Profile Manager** — Isolated Chrome environments  
**Injection Engine** — High-precision JavaScript delivery  
**Terminal Engine** — Beautiful, responsive console UI  
**Scheduler** — Matrix parsing and validation  
**Storage Layer** — Safe LocalStorage abstraction  
**Account Manager** — Secure multi-account handling  

---

## Matrix Mapping

| Day       | Slot 1       | Slot 2       | Slot 3       | Notes              |
|-----------|--------------|--------------|--------------|--------------------|
| Monday    | Chest        | Triceps      | Cardio       | Heavy day          |
| Tuesday   | Back         | Biceps       | Core         | Pull focus         |
| Wednesday | Legs         | Shoulders    | Mobility     | Recovery           |

Full custom time support (e.g., `07:30`, `18:00`) and exercise variants.

---

## Terminal Preview

```bash
$ python main.py

╔══════════════════════════════════════════════════════════════╗
║                 🏋️  GYMSYNC-CLI v1.0.0                      ║
║               Premium Terminal Automation                   ║
╚══════════════════════════════════════════════════════════════╝

[✓] Profile Loaded          [✓] Chrome Connected
[✓] Session Active          [⏱] Ready in 1.4s

1. Inject Weekly Schedule
2. Quick Day Update
3. Account Manager
4. View Storage State
5. Run Diagnostics
0. Exit

> 1
[INFO] Loading schedule matrix...
[INFO] Validating 48 exercises... ✓
[INFO] Injecting into LocalStorage... ████████████ 100% ✓

✅ Schedule synchronized successfully!
   • 7 days • 48 exercises • 2.8 seconds
```

---

## Folder Structure

```bash
GymSync-CLI/
├── chrome_profile/          # Chrome user data
├── config/                  # settings + mappings
├── assets/
├── scripts/js_injection/    # JavaScript payloads
├── logs/
├── gymsync/                 # Core Python package
│   ├── core/
│   ├── engines/
│   └── terminal/
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/guptaji0358/GymSync-CLI.git
cd GymSync-CLI

python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

pip install -r requirements.txt

# Place ChromeDriver in PATH or project root
python main.py
```

---

## Requirements

- Python 3.8+
- Google Chrome
- ChromeDriver (matching Chrome version)
- Works on Windows, Linux, macOS

---

## Configuration

All settings in `config/settings.json`. Easy to customize Chrome paths, timeouts, themes, and more.

---

## Usage

Run `python main.py` and follow the beautiful interactive menu. Full command-line flags also supported for scripting.

---

## Technical Details

- Selenium WebDriver for browser control
- Direct JavaScript injection into Chrome
- LocalStorage manipulation
- Rich terminal rendering
- Robust error handling and recovery
- Isolated session management

---

## Performance

| Metric           | GymSync-CLI | Traditional GUI |
|------------------|-------------|-----------------|
| Memory           | ~85 MB      | 500-800 MB      |
| Startup          | < 2s        | 10-20s          |
| Injection Speed  | < 3s        | 30-90s          |

---

## Security

- Everything runs locally
- Isolated profiles
- No telemetry
- Clean session handling

---

## Future Roadmap

- Headless improvements
- Plugin system
- AI schedule generator
- Docker support
- Dark/light terminal themes
- REST API mode

---

## Open Source Contribution

Fork → Branch → Commit → PR. All contributions welcome!

---

## License

MIT License

---

## FAQ

**Q: Do I need programming experience?**  
A: Basic terminal usage is enough. Advanced users can extend it easily.

**Q: Is my data safe?**  
A: Yes. Everything stays on your machine.

**Q: Can it run automatically?**  
A: Yes. Perfect for cron jobs and scripts.

**Q: Does it support custom exercises?**  
A: Yes. Full mapping support.

**Q: Can I use it headless?**  
A: Yes, with configuration.

---

## Credits

- Python Community
- Selenium Team
- Google Chrome
- Open Source Contributors

---

<div align="center">
  <strong>Built with passion for speed and simplicity.</strong><br><br>
  <blockquote>
    "The core framework is fully optimized, stable, and locked down. Robin is officially not launching a V2 of this tool—this code stands completed as the absolute definitive release."
  </blockquote>
</div>

**Made by [Robin Gupta](https://github.com/guptaji0358)**
```
