<a name="top"></a>
<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1f6feb,100:43b02a&height=220&section=header&text=GymSync-CLI&fontSize=64&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Terminal-First%20Browser%20Automation%20Framework&descAlignY=58&descSize=20" />

<br>

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
<img src="https://img.shields.io/badge/Google-Chrome-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white" />
<img src="https://img.shields.io/badge/CLI-Terminal-00C853?style=for-the-badge" />
<img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" />

<br>

<img src="https://img.shields.io/github/stars/guptaji0358/GymSync-CLI?style=for-the-badge&color=f1e05a&label=STARS" />
<img src="https://img.shields.io/github/forks/guptaji0358/GymSync-CLI?style=for-the-badge&color=blue&label=FORKS" />
<img src="https://img.shields.io/github/issues/guptaji0358/GymSync-CLI?style=for-the-badge&color=critical&label=ISSUES" />
<img src="https://img.shields.io/github/last-commit/guptaji0358/GymSync-CLI?style=for-the-badge&color=success&label=LAST%20COMMIT" />

<br><br>

<a href="https://www.youtube.com/watch?v=83uUFUtQ_b4"><img src="https://img.shields.io/badge/▶_WATCH_DEMO-FF0000?style=for-the-badge&logo=youtube&logoColor=white" /></a>
<a href="#-quick-start"><img src="https://img.shields.io/badge/⚡_QUICK_START-1f6feb?style=for-the-badge&logo=rocket&logoColor=white" /></a>
<a href="https://github.com/guptaji0358/GymSync-CLI/stargazers"><img src="https://img.shields.io/badge/⭐_STAR_THIS_REPO-f1e05a?style=for-the-badge&logo=github&logoColor=black" /></a>

<br><br>

<i>Automate. Synchronize. Inject. Control.</i><br>
<sub>A modern, high-performance command-line automation framework powered by Python and Selenium WebDriver.</sub>

</div>

<br>

<table>
<tr>
<td align="center" width="50%">
<a href="https://chat.openai.com"><img src="https://img.shields.io/badge/ChatGPT-Assisted-10A37F?style=flat-square&logo=openai&logoColor=white" /></a>
</td>
<td align="center" width="50%">
<a href="https://gemini.google.com"><img src="https://img.shields.io/badge/Gemini-Assisted-8E75FF?style=flat-square&logo=googlegemini&logoColor=white" /></a>
</td>
</tr>
</table>

<br>

## 📖 Overview

GymSync-CLI treats the browser as a **programmable engine, not a manual interface**. Instead of relying on slow graphical interfaces, it communicates with Google Chrome via Selenium WebDriver, injects JavaScript, synchronizes data through LocalStorage, and updates gym scheduling data in real time — all from a clean, interactive terminal dashboard.

<br>

## 🔥 Key Capabilities

<table width="100%">
<tr>
<td width="50%" valign="top">
<div style="background-color:#161b22;border:1px solid #30363d;border-radius:10px;padding:16px;">
<h3>⚡ Direct LocalStorage Injection</h3>
<p>Serialized schedule data is injected straight into the browser's LocalStorage — no temp files, instant synchronization, real-time state updates.</p>
</div>
</td>
<td width="50%" valign="top">
<div style="background-color:#161b22;border:1px solid #30363d;border-radius:10px;padding:16px;">
<h3>🌐 Live DOM Synchronization</h3>
<p>JavaScript routines refresh the active webpage immediately after injection, keeping every UI element in sync without manual interaction.</p>
</div>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<div style="background-color:#161b22;border:1px solid #30363d;border-radius:10px;padding:16px;">
<h3>🔒 Isolated Chrome Profiles</h3>
<p>Every automation session runs inside its own dedicated Chrome profile — separate cookies, saved preferences, zero interference with your personal browser.</p>
</div>
</td>
<td width="50%" valign="top">
<div style="background-color:#161b22;border:1px solid #30363d;border-radius:10px;padding:16px;">
<h3>🧠 Intelligent Account Handling</h3>
<p>Continuously monitors auth state — expired sessions, logouts, and validation errors pause execution safely instead of crashing.</p>
</div>
</td>
</tr>
</table>

<br>

## 🎥 Live Demo

<div align="center">
<a href="https://www.youtube.com/watch?v=83uUFUtQ_b4">
<img src="https://img.youtube.com/vi/83uUFUtQ_b4/maxresdefault.jpg" alt="GymSync-CLI Demo" width="720" style="border-radius:12px;border:1px solid #30363d;" />
</a>
<br><br>
<a href="https://www.youtube.com/watch?v=83uUFUtQ_b4"><img src="https://img.shields.io/badge/▶%20Watch%20Full%20Demo%20on%20YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" /></a>
</div>

<br>

## 💻 CLI / Workflow Demo

<pre><code>══════════════════════════════════════════════════════════════════
                🏋️  GYM AUTOMATION DASHBOARD
══════════════════════════════════════════════════════════════════
Status
✔ Browser Connected     ✔ Session Active
✔ Chrome Profile Loaded ✔ Schedule Ready
──────────────────────────────────────────────────────────────────
1. View Booked Classes        6. Reload Browser
2. Sync Weekly Schedule        7. Clear Terminal
3. Delete Existing Schedule    8. Switch Account
4. Diagnostics                 9. Exit
5. Manage Custom Classes
──────────────────────────────────────────────────────────────────
Select Option > 2

[INFO] Loading Weekly Schedule...
██████████████████████████████ 100%
[INFO] Checking Browser...        ✔ Connected
[INFO] Injecting JavaScript...
██████████████████████████████ 100%
[INFO] Synchronizing LocalStorage...
██████████████████████████████ 100%
[INFO] Refreshing DOM...
██████████████████████████████ 100%
[SUCCESS] Schedule Updated Successfully
Elapsed Time : 2.84 Seconds
</code></pre>

<br>

## 🧰 Core Tech Stack

<table width="100%">
<tr>
<td align="center" width="25%"><img width="48" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" /><br><b>Python 3.8+</b><br><sub>Core Runtime</sub></td>
<td align="center" width="25%"><img width="48" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" /><br><b>Selenium</b><br><sub>Browser Automation</sub></td>
<td align="center" width="25%"><img width="48" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/chrome/chrome-original.svg" /><br><b>Google Chrome</b><br><sub>Target Browser</sub></td>
<td align="center" width="25%"><img width="48" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" /><br><b>JavaScript</b><br><sub>DOM Injection</sub></td>
</tr>
<tr>
<td align="center" width="25%"><img width="48" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" /><br><b>Git</b><br><sub>Version Control</sub></td>
<td align="center" width="25%"><img width="48" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg" /><br><b>Windows</b><br><sub>Supported OS</sub></td>
<td align="center" width="25%"><img width="48" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" /><br><b>Linux</b><br><sub>Supported OS</sub></td>
<td align="center" width="25%"><img width="48" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apple/apple-original.svg" /><br><b>macOS</b><br><sub>Supported OS</sub></td>
</tr>
</table>

<br>

## 🚀 Quick Start

1. **Clone the repository**

<pre><code>git clone https://github.com/guptaji0358/GymSync-CLI.git
cd GymSync-CLI</code></pre>

2. **Create and activate a virtual environment**

<pre><code># Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate</code></pre>

3. **Install dependencies**

<pre><code>pip install -r requirements.txt
# or manually
pip install selenium</code></pre>

4. **Install Google Chrome + matching ChromeDriver**, then run:

<pre><code>python 49_GYM__SYNC.py</code></pre>

<br>

## 🔐 Setup & Credentials Guide

<table width="100%">
<tr>
<td style="background-color:#161b22;border-left:4px solid #d29922;border-radius:6px;padding:14px;">
<b>⚠️ Warning — Chrome Profile</b><br>
The <code>chrome_profile/</code> folder stores cookies, session tokens, and preferences. Deleting it resets all logged-in sessions. Never commit this folder to version control.
</td>
</tr>
</table>

<br>

<table width="100%">
<tr>
<td style="background-color:#161b22;border-left:4px solid #1f6feb;border-radius:6px;padding:14px;">
<b>ℹ️ Note — ChromeDriver Version</b><br>
ChromeDriver <b>must match</b> your installed Chrome version exactly, or Selenium will fail to attach. Ensure it is available on your system PATH.
</td>
</tr>
</table>

<br>

<table width="100%">
<tr>
<td style="background-color:#161b22;border-left:4px solid #3fb950;border-radius:6px;padding:14px;">
<b>✅ Tip — Isolation</b><br>
GymSync-CLI never touches your personal Chrome profile or uploads data to the cloud — everything stays local and isolated.
</td>
</tr>
</table>

<br>

## 🎓 Concepts Mastered

<table width="100%">
<tr>
<td width="33%" valign="top">
<h4>🏗️ Modular Architecture</h4>
<p>Session Manager, Browser Controller, Schedule Engine, and Profile Manager operate as independent, replaceable modules.</p>
</td>
<td width="33%" valign="top">
<h4>🛡️ Defensive Engineering</h4>
<p>Zero-traceback exception handling, isolated sessions, and controlled Ctrl+C interrupt confirmation flows.</p>
</td>
<td width="33%" valign="top">
<h4>🌐 Browser-as-Runtime</h4>
<p>Direct JavaScript injection and LocalStorage manipulation instead of brittle UI-click automation.</p>
</td>
</tr>
</table>

<br>

## 🛣️ Open Source & Roadmap

- [ ] 🚀 Headless automation mode
- [ ] 🔔 Desktop notifications (Windows / Linux / macOS)
- [ ] 📅 Built-in task scheduler for auto-sync
- [ ] 📈 Analytics dashboard for scheduling history
- [ ] 🔌 Plugin system for custom exercises & providers
- [ ] 🐳 Docker containerized deployment
- [ ] 🤖 AI-assisted schedule suggestions

Contributions are welcome — fork the repo, create a feature branch, and open a pull request. See the full contribution workflow in the repository.

<br>

<div align="center">

## 👨‍💻 Author

<img src="https://img.shields.io/badge/Robin%20Gupta-Lead%20Developer-1f6feb?style=for-the-badge&logo=github&logoColor=white" />

<b>Developer • Python Programmer • C++ Learner • Desktop Application Enthusiast</b>

<a href="https://github.com/guptaji0358"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="https://github.com/guptaji0358/GymSync-CLI"><img src="https://img.shields.io/badge/Repository-GymSync--CLI-43B02A?style=for-the-badge&logo=selenium&logoColor=white" /></a>

<br><br>

⭐ **If GymSync-CLI helped you, please consider starring the repository!** ⭐

<br>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:43b02a,50:1f6feb,100:0d1117&height=150&section=footer" />

</div>
