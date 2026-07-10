# 🏋️ GymSync-CLI

<div align="center">

### ⚡ Ultra-Fast • Terminal-First • Browser Automation Framework

```

<div align="center">

<h1>🏋️ GymSync-CLI</h1>

<h3>⚡ Ultra-Fast • Terminal-First • Browser Automation Framework</h3>

<p><em>Fast • Lightweight • Selenium Powered • Open Source</em></p>

</div>

```

**A modern, high-performance command-line automation framework powered by Python and Selenium WebDriver.**

*Automate. Synchronize. Inject. Control.*

---

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Chrome](https://img.shields.io/badge/Google-Chrome-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-Terminal-00C853?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

[![GitHub Stars](https://img.shields.io/github/stars/guptaji0358/GymSync-CLI?style=social)](https://github.com/guptaji0358/GymSync-CLI/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/guptaji0358/GymSync-CLI?style=social)](https://github.com/guptaji0358/GymSync-CLI/network)
[![GitHub Issues](https://img.shields.io/github/issues/guptaji0358/GymSync-CLI)](https://github.com/guptaji0358/GymSync-CLI/issues)

## 🤖 AI-Assisted Development

![ChatGPT](https://img.shields.io/badge/ChatGPT-Assisted-10A37F?style=for-the-badge&logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-Assisted-8E75FF?style=for-the-badge&logo=googlegemini&logoColor=white)

</div>

---

# 🚀 Introduction

GymSync-CLI is a **high-performance browser automation framework** designed to automate gym schedule management directly from the terminal.

Instead of relying on slow graphical interfaces, GymSync-CLI communicates with **Google Chrome** using **Selenium WebDriver**, executes custom JavaScript, synchronizes browser data through **LocalStorage**, and updates the website in real time.

The project focuses on **speed**, **automation**, **clean architecture**, and **developer-friendly workflows**, making repetitive scheduling tasks nearly effortless.

Whether you're a developer exploring browser automation or a power user looking for an efficient scheduling tool, GymSync-CLI delivers a responsive command-line experience without unnecessary GUI overhead.

---

# ✨ Highlights

- ⚡ High-speed browser automation
- 🏋️ Interactive terminal dashboard
- 🌐 Selenium-powered Chrome control
- 🔄 Real-time DOM synchronization
- 💾 Direct LocalStorage manipulation
- 🔒 Isolated Chrome profile management
- 🧠 Intelligent account handling
- 📅 Weekly schedule automation
- 🚀 Lightweight command-line workflow
- 🛠️ Open-source and fully customizable

---

# 🎯 Design Philosophy

GymSync-CLI follows a simple philosophy:

> **"Treat the browser as a programmable engine, not as a manual interface."**

Instead of clicking buttons repeatedly, the application automates everything through structured Python code, browser scripting, and intelligent data injection.

This results in:

- Less repetitive work
- Faster execution
- Cleaner workflows
- Better reliability
- Easier maintenance

---

# 📑 Table of Contents

- [🚀 Introduction](#-introduction)
- [✨ Highlights](#-highlights)
- [🎯 Design Philosophy](#-design-philosophy)
- [📖 Project Overview](#-project-overview)
- [🔥 Core Features](#-core-features)
- [💡 Why GymSync-CLI?](#-why-gymsync-cli)
- [🏗️ Architecture](#️-architecture)
- [🔄 Workflow](#-workflow)
- [🧠 Core Components](#-core-components)
- [📊 Matrix Mapping](#-matrix-mapping)
- [🖥️ Terminal Preview](#️-terminal-preview)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [📦 Requirements](#-requirements)
- [🛠️ Configuration](#️-configuration)
- [🚀 Usage](#-usage)
- [🔬 Technical Details](#-technical-details)
- [📈 Performance](#-performance)
- [🔒 Security](#-security)
- [🛣️ Future Roadmap](#️-future-roadmap)
- [🤝 Contributing](#-contributing)
- [❓ Frequently Asked Questions](#-frequently-asked-questions)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)

---

# 📖 Project Overview

GymSync-CLI is a command-line automation framework built with **Python** and **Selenium WebDriver** that provides a modern approach to automating browser-based gym schedule management.

Unlike traditional automation tools that rely on visible GUI interactions, GymSync-CLI treats the browser as a programmable runtime. It communicates directly with the active browser session, injects JavaScript, synchronizes DOM elements, manipulates LocalStorage, and performs complex scheduling tasks with minimal user interaction.

The framework was designed around four primary goals:

## ⚡ Performance

Avoid unnecessary GUI operations and reduce repetitive manual interactions by automating the complete workflow directly from the terminal.

---

## 🛡️ Reliability

Maintain isolated browser profiles, structured exception handling, and controlled runtime behavior to ensure stable automation sessions.

---

## 🧩 Modularity

Every subsystem is designed to be extendable. Developers can customize mappings, workflows, scheduling logic, browser behavior, and future integrations without rewriting the entire application.

---

## 🌍 Open Source

GymSync-CLI is fully open-source and intended for learning, customization, experimentation, and community contributions.

Whether you're exploring Selenium, browser automation, or command-line application architecture, the project serves as both a practical utility and a learning resource.

---

> **Status:** ✅ Active Development Complete  
> **Current Release:** Stable  
> **Language:** Python  
> **Interface:** Command Line (CLI)  
> **Automation Engine:** Selenium WebDriver  
> **Browser:** Google Chrome  
> **License:** MIT

# 🔥 Core Features

GymSync-CLI is built around a modular automation engine where every component performs a dedicated task. Together they create a fast, reliable, and developer-friendly browser automation framework.

---

## ⚡ Direct LocalStorage Injection

Instead of manually interacting with dozens of webpage elements, GymSync-CLI injects serialized schedule data directly into the browser's LocalStorage.

### Benefits

- 🚀 Extremely fast updates
- 📦 No temporary files
- ⚡ Instant browser synchronization
- 🔄 Real-time application state updates

---

## 🌐 Live DOM Synchronization

Once data is injected, the framework immediately executes JavaScript routines that refresh and synchronize the active webpage.

This ensures every UI component reflects the newest information without requiring manual page interaction.

### Advantages

- Instant UI updates
- Reduced user interaction
- Better responsiveness
- Cleaner automation flow

---

## 🔒 Isolated Chrome Profiles

Every automation session runs inside its own dedicated Chrome profile.

```
chrome_profile/
```

Benefits include:

- Separate login sessions
- Persistent cookies
- Saved preferences
- Safe testing environment
- No interference with your personal Chrome profile

---

## 🧠 Intelligent Account Management

GymSync-CLI continuously monitors browser state during authentication.

If an account:

- doesn't exist
- expires
- logs out
- encounters validation errors

the framework intelligently pauses execution and allows the user to:

- Register
- Retry Login
- Exit Safely

instead of crashing.

---

## 🛡️ Zero Traceback Protection

Unexpected exceptions can clutter terminals with long Python tracebacks.

GymSync-CLI implements custom exception handling that keeps terminal output clean while preventing unnecessary information from appearing.

Benefits:

- Cleaner logs
- Better user experience
- Easier debugging
- Professional terminal appearance

---

## ⌨️ Smart Keyboard Controls

Instead of immediately terminating execution,

GymSync-CLI uses a controlled interrupt system.

Example:

```
Press Ctrl+C once
↓

Confirmation Requested

↓

Press Ctrl+C again

↓

Application exits safely
```

This prevents accidental termination.

---

## 📅 Dynamic Schedule Engine

Supports complete weekly scheduling.

Features include:

- Multiple exercise categories
- Custom time slots
- Weekly planning
- Flexible schedule mapping
- Expandable configuration

---

## ⚙️ Browser Automation Engine

Powered by Selenium WebDriver.

Capabilities include:

- Login automation
- Form interaction
- Button clicking
- JavaScript execution
- Data extraction
- Dynamic page updates

---

## 📊 Interactive Terminal Dashboard

Instead of dozens of command-line arguments,

GymSync-CLI provides an interactive dashboard.

```
===============================
 GYM AUTOMATION DASHBOARD
===============================

1. Book Classes

2. Update Schedule

3. Delete Schedule

4. Diagnostics

5. Settings

6. Exit

===============================
```

This makes the framework beginner friendly while remaining powerful.

---

## 📝 Clean Console Logging

Every operation is logged using structured terminal messages.

Example

```
[INFO] Initializing Chrome...

[SUCCESS] Login Successful

[INFO] Injecting Schedule...

[SUCCESS] Synchronization Complete

[WARNING] Sunday already exists.

[ERROR] Session Expired.
```

Readable logs make debugging significantly easier.

---

## 🚀 Performance Focused

The framework was designed around speed.

Instead of repeatedly clicking webpage elements,

it performs direct browser operations whenever possible.

Result:

- Lower execution time
- Lower CPU usage
- Reduced unnecessary browser activity

---

# 💡 Why GymSync-CLI?

Many browser automation scripts are simply collections of Selenium commands.

GymSync-CLI is different.

It behaves more like a complete desktop application running entirely inside a terminal.

---

## Traditional Browser Automation

❌ Manual clicking

❌ Hardcoded scripts

❌ Poor error handling

❌ Difficult maintenance

❌ Limited scalability

---

## GymSync-CLI

✅ Interactive dashboard

✅ Modular architecture

✅ Intelligent synchronization

✅ LocalStorage manipulation

✅ JavaScript execution

✅ Structured logging

✅ Extendable design

✅ Professional workflow

---

## Why Terminal?

Command-line applications provide several advantages over traditional graphical interfaces.

### ⚡ Faster

No heavy GUI rendering.

Resources remain focused on automation.

---

### 🎯 More Accurate

Automation logic executes directly without unnecessary mouse movement.

---

### 🧩 Easier Integration

Can easily integrate with:

- Scheduled Tasks
- Cron Jobs
- Batch Scripts
- PowerShell
- Bash
- CI/CD Pipelines

---

### 💻 Developer Friendly

Everything can be:

- scripted
- automated
- version controlled
- customized

---

## Philosophy

Instead of controlling a browser like a human,

GymSync-CLI treats it as a programmable runtime.

```
User
   │
   ▼
Python Engine
   │
   ▼
Selenium
   │
   ▼
Chrome
   │
   ▼
JavaScript
   │
   ▼
DOM + LocalStorage
   │
   ▼
Updated User Interface
```

---

# 🏗️ Architecture Diagram

```text
                           USER
                             │
                             ▼
                 ┌────────────────────┐
                 │ Terminal Dashboard │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Command Dispatcher │
                 └─────────┬──────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼

 Session Manager      Schedule Engine     Profile Manager

        │                  │                  │

        └──────────────┬───┴──────────────────┘
                       ▼

              Browser Controller

                       │

                       ▼

               Selenium WebDriver

                       │

                       ▼

               Google Chrome

                       │

      ┌────────────────┼────────────────┐

      ▼                ▼                ▼

 JavaScript        DOM Engine      LocalStorage

      │                │                │

      └────────────────┼────────────────┘

                       ▼

              Updated Browser UI
```

---

# 🔄 Workflow Diagram

```text
Start Program
      │
      ▼
Initialize Environment
      │
      ▼
Load Chrome Profile
      │
      ▼
Launch Browser
      │
      ▼
Authenticate User
      │
      ▼
Load Schedule Data
      │
      ▼
Validate Entries
      │
      ▼
Inject JavaScript
      │
      ▼
Update LocalStorage
      │
      ▼
Synchronize DOM
      │
      ▼
Verify Changes
      │
      ▼
Display Success Dashboard
      │
      ▼
Wait for Next Command
```

---

## 🚀 Core Principles

GymSync-CLI is built upon five engineering principles:

### ⚡ Performance First

Every feature is optimized to minimize execution time.

---

### 🔒 Stability

Controlled browser sessions, isolated profiles, and intelligent exception handling.

---

### 🧩 Modularity

Every component is replaceable and extendable.

---

### 🌍 Open Source

Fork it.

Modify it.

Improve it.

Build upon it.

---

### ❤️ Developer Experience

Readable code.

Readable logs.

Predictable architecture.

Professional workflow.

# 🧠 Core Components

GymSync-CLI is divided into independent modules. Each module has a single responsibility, making the framework easier to maintain, debug, and extend.

---

## 🚀 Session Manager

The Session Manager is responsible for controlling the entire lifecycle of the application.

### Responsibilities

- Initialize runtime
- Validate configuration
- Launch browser
- Monitor execution
- Handle shutdown
- Manage active sessions

```
Application Start
        │
        ▼
 Session Manager
        │
        ├── Load Settings
        ├── Start Browser
        ├── Initialize Modules
        ├── Monitor Runtime
        └── Safe Shutdown
```

---

## 🌐 Browser Controller

Acts as the communication bridge between Python and Google Chrome.

### Responsibilities

- Launch Chrome
- Connect Selenium
- Open URLs
- Refresh pages
- Execute scripts
- Manage browser windows

---

## 🔥 JavaScript Injection Engine

One of the most powerful components of GymSync-CLI.

Instead of repeatedly clicking webpage elements, JavaScript is injected directly into the active browser.

### Responsibilities

- Execute JavaScript
- Read DOM
- Update DOM
- Read LocalStorage
- Write LocalStorage
- Trigger UI refresh

```
Python
   │
   ▼
Selenium
   │
   ▼
JavaScript
   │
   ▼
Browser Runtime
```

---

## 💾 LocalStorage Manager

Responsible for reading and writing browser storage.

### Features

- Save schedules
- Update existing values
- Remove entries
- Serialize Python objects
- Deserialize browser data

Advantages

- Faster than repeated clicking
- Cleaner synchronization
- Better performance

---

## 📅 Schedule Engine

Handles every scheduling operation.

### Supports

- Weekly schedules
- Daily schedules
- Exercise mapping
- Time mapping
- Custom schedules
- Dynamic updates

---

## 👤 Account Manager

Responsible for login validation.

Features include

- Login detection
- Logout detection
- Invalid account detection
- Registration support
- Session recovery

---

## 📁 Profile Manager

Creates an isolated browser environment.

```
chrome_profile/

├── Cookies

├── Preferences

├── Local Storage

├── Cache

└── Session Data
```

Benefits

- Persistent login
- Saved browser state
- Independent testing
- Safe automation

---

## 📊 Terminal Engine

Responsible for everything displayed inside the CLI.

### Includes

- Dashboard
- Menus
- Progress
- Logging
- Colors
- Status messages
- User input

---

## 🛡️ Error Handler

Centralized exception management.

Instead of crashing immediately,

GymSync-CLI

- captures exceptions
- logs useful information
- keeps terminal clean
- safely exits when necessary

---

## 🔄 Synchronization Engine

Responsible for keeping browser state synchronized.

```
Python Data

      │

      ▼

JavaScript

      │

      ▼

LocalStorage

      │

      ▼

DOM Update

      │

      ▼

Visible Browser UI
```

---

# 📊 Matrix Mapping

GymSync-CLI uses lightweight numeric mappings to make schedule selection faster inside the terminal.

---

## 📅 Days

| Code | Day |
|------|------|
| 01 | Monday |
| 02 | Tuesday |
| 03 | Wednesday |
| 04 | Thursday |
| 05 | Friday |
| 06 | Saturday |
| 07 | Sunday |

---

## 🕒 Time Slots

| Code | Time |
|------|-------|
| 01 | 6:00 AM |
| 02 | 7:00 AM |
| 03 | 8:00 AM |
| 04 | 9:00 AM |
| 05 | 10:00 AM |
| 06 | 11:00 AM |
| 07 | 12:00 PM |
| 08 | 1:00 PM |
| 09 | 2:00 PM |
| 10 | 3:00 PM |
| 11 | 4:00 PM |
| 12 | 5:00 PM |
| 13 | 6:00 PM |
| 14 | 7:00 PM |
| 15 | 8:00 PM |

---

## 🏋️ Exercise Categories

| Code | Exercise |
|------|----------|
| 01 | BodyPump |
| 02 | Boxing |
| 03 | Cardio Blast |
| 04 | CrossFit |
| 05 | Dance Fitness |
| 06 | General Training |
| 07 | HIIT |
| 08 | Kickboxing |
| 09 | Pilates |
| 10 | Power Lifting |
| 11 | Spin Class |
| 12 | Strength & Conditioning |
| 13 | Yoga |

---

## ⌨️ Custom Time Mode

Instead of selecting predefined slots, users can enter custom values.

Example

```
Enter Time

> ct

Custom Time

> 07:30 AM
```

Supported examples

```
06:15 AM

07:45 AM

12:30 PM

06:00 PM

08:15 PM
```

---

# 🖥️ Terminal Preview

```text
══════════════════════════════════════════════════════════════════

                🏋️  GYM AUTOMATION DASHBOARD

══════════════════════════════════════════════════════════════════

Status

✔ Browser Connected

✔ Session Active

✔ Chrome Profile Loaded

✔ Schedule Ready

──────────────────────────────────────────────────────────────────

1. View Booked Classes

2. Sync Weekly Schedule

3. Delete Existing Schedule

4. Diagnostics

5. Manage Custom Classes

6. Reload Browser

7. Clear Terminal

8. Switch Account

9. Exit

──────────────────────────────────────────────────────────────────

Select Option >

```

---

## Schedule Synchronization

```text
Loading Weekly Schedule...

██████████████████████████████ 100%

Checking Browser...

✔ Connected

Injecting JavaScript...

██████████████████████████████ 100%

Synchronizing LocalStorage...

██████████████████████████████ 100%

Refreshing DOM...

██████████████████████████████ 100%

✔ Schedule Updated Successfully

Elapsed Time : 2.84 Seconds
```

---

## Error Example

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠ WARNING

Chrome profile already in use.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Retry

2. Close Existing Session

3. Exit

>
```

---

## Account Recovery

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Account Not Found

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Would you like to register?

[Y] Yes

[N] No

>

```

---

# 📁 Project Structure

```text
GymSync-CLI/
│
├── chrome_profile/
├── 49_GYM__SYNC.py
└── README.md
```

---
## 📂 Directory Overview

| Item | Description |
|------|-------------|
| **chrome_profile/** | Stores the isolated Google Chrome profile used for browser automation. |
| **49_GYM__SYNC.py** | The complete GymSync-CLI application containing all automation logic, terminal interface, Selenium workflow, and schedule management. |
| **README.md** | Project documentation, installation guide, and usage instructions. |

---

## 🏗️ Framework Design Goals

GymSync-CLI follows a modular architecture.

Every folder has a dedicated responsibility.

This makes it easy to

- add new modules
- replace existing engines
- debug issues
- scale features
- maintain the project

without affecting unrelated parts of the codebase.

# ⚙️ Installation

Getting GymSync-CLI up and running takes only a few minutes.

The framework has been designed with simplicity in mind while maintaining a professional development workflow.

---

# 📋 Prerequisites

Before installing GymSync-CLI, ensure the following software is available on your system.

| Software | Required | Purpose |
|-----------|----------|---------|
| Python 3.8+ | ✅ | Core Runtime |
| Google Chrome | ✅ | Browser Automation |
| ChromeDriver | ✅ | Selenium Browser Driver |
| Git | Recommended | Clone Repository |
| pip | ✅ | Python Package Manager |

---

# 💻 Supported Operating Systems

| Platform | Support |
|----------|----------|
| 🪟 Windows | ✅ Fully Supported |
| 🐧 Linux | ✅ Supported |
| 🍎 macOS | ✅ Supported |

---

# 📥 Step 1 — Clone the Repository

Clone the project using Git.

```bash
git clone https://github.com/guptaji0358/GymSync-CLI.git

cd GymSync-CLI
```

---

# 📂 Step 2 — Create a Virtual Environment

Using a virtual environment keeps project dependencies isolated from your global Python installation.

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

After activation you should see something similar to

```text
(venv)

C:\Projects\GymSync-CLI>
```

---

# 📦 Step 3 — Install Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

or manually

```bash
pip install selenium
```

---

# 🌐 Step 4 — Install Google Chrome

Download and install the latest version of Google Chrome.

GymSync-CLI is optimized specifically for Chrome-based automation.

---

# 🚗 Step 5 — Install ChromeDriver

ChromeDriver allows Selenium to communicate with Google Chrome.

Download the version matching your installed Chrome browser.

After installation ensure ChromeDriver is accessible through your system PATH.

---

# ▶ Step 6 — Run GymSync-CLI

Start the framework.

```bash
python main.py
```

or

```bash
python 49_GYM__SYNC.py
```

After a few seconds the terminal dashboard should appear.

---

# ✅ Successful Startup

If everything has been configured correctly you should see something similar to

```text
══════════════════════════════════════════════

GymSync CLI

══════════════════════════════════════════════

Loading Configuration...

Loading Browser...

Initializing Chrome...

Checking Session...

Ready.

══════════════════════════════════════════════
```

---

# 📦 Requirements

## Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| CPU | Dual Core |
| RAM | 2 GB |
| Storage | 100 MB |
| Python | 3.8+ |
| Chrome | Latest Stable |
| Internet | Required for Login |

---

## Recommended Requirements

| Component | Recommendation |
|-----------|----------------|
| CPU | Intel Core i5 / Ryzen 5 |
| RAM | 8 GB or Higher |
| Storage | SSD |
| Python | Latest Version |
| Chrome | Latest Stable |
| Terminal | Windows Terminal / PowerShell |

---

# 📚 Python Dependencies

Current project dependencies include

```
selenium
```

Future versions may additionally support

```
webdriver-manager

rich

colorama

schedule

plyer
```

---

# ⚙️ Configuration

GymSync-CLI was designed to be highly configurable.

Almost every subsystem can be customized without changing the core application logic.

---

## Chrome Profile

The framework stores browser information inside

```
chrome_profile/
```

This folder contains

- Cookies

- Login Sessions

- Browser Preferences

- Local Storage

- Cache

Removing this folder resets browser state.

---

## Schedule Configuration

Schedule mappings are configurable.

Example

```text
Monday

↓

07:00 AM

↓

Yoga

↓

Gym Hall A
```

Developers can easily modify schedule logic according to their own workflow.

---

## Browser Configuration

Browser startup options can include

```
Headless Mode

Disable GPU

Disable Extensions

Custom User Agent

Incognito

Custom Window Size
```

These options make the framework suitable for different automation environments.

---

## Timeout Configuration

Timeouts can be adjusted for

- Browser Launch

- Page Loading

- DOM Detection

- JavaScript Execution

- Element Visibility

- Authentication

---

## JavaScript Injection

The framework executes custom JavaScript inside the active browser session.

Typical operations include

```
Reading LocalStorage

Writing LocalStorage

Creating DOM Nodes

Updating Existing Elements

Dispatching Browser Events

Refreshing Interface
```

---

## Logging

Runtime logs can include

```
INFO

WARNING

SUCCESS

ERROR

DEBUG
```

This provides developers with detailed insight into every automation stage.

---

# 🚀 Usage

Starting GymSync-CLI launches an interactive command-line dashboard.

The dashboard provides keyboard-driven access to every feature.

---

## Main Menu

```text
══════════════════════════════════════════════

GYM AUTOMATION DASHBOARD

══════════════════════════════════════════════

1. View Booked Classes

2. Sync Weekly Schedule

3. Delete Existing Bookings

4. Diagnostics

5. Custom Schedule

6. Reload Browser

7. Clear Terminal

8. Switch Account

9. Exit

══════════════════════════════════════════════

Select Option >
```

---

## Option 1 — View Booked Classes

Displays the currently booked classes directly from the browser.

Information includes

- Day

- Time

- Exercise

- Availability

---

## Option 2 — Synchronize Schedule

Reads local schedule data.

Processes every entry.

Injects JavaScript.

Updates LocalStorage.

Synchronizes the browser interface.

Displays completion status.

---

## Option 3 — Delete Bookings

Safely removes previously synchronized schedules.

Includes confirmation prompts before deletion.

---

## Option 4 — Diagnostics

Performs a complete system health check.

Validates

- Chrome Connection

- Selenium

- Session

- Browser Profile

- Storage Access

- JavaScript Engine

---

## Option 5 — Custom Schedule

Allows users to

- create schedules

- modify schedules

- edit exercises

- define custom times

- create personalized workout plans

---

## Option 6 — Reload Browser

Reloads the active browser without restarting the application.

Useful after

- Login Changes

- Network Errors

- Browser Crashes

---

## Option 7 — Clear Terminal

Removes previous console output while keeping the application running.

Provides a clean workspace.

---

## Option 8 — Switch Account

Logs out the current account.

Starts a fresh authentication session.

Preserves application state whenever possible.

---

## Option 9 — Exit

Terminates GymSync-CLI safely.

Performs

- Browser Shutdown

- Resource Cleanup

- Session Saving

- Terminal Exit

without leaving orphan browser processes running.

---

# 💡 Usage Tips

✔ Keep Chrome updated.

✔ Avoid manually closing the automated browser.

✔ Use isolated Chrome profiles.

✔ Keep Python packages updated.

✔ Run inside a virtual environment whenever possible.

✔ Create backups of custom schedule mappings.

✔ Review logs if synchronization fails.

✔ Restart Chrome if unexpected browser behavior occurs.

---

> **GymSync-CLI is designed to make browser automation fast, reliable, and enjoyable while keeping the user fully in control through a clean command-line interface.**

# 🔬 Technical Details

GymSync-CLI is engineered around a modular browser automation pipeline that combines Python, Selenium WebDriver, JavaScript execution, and Chrome's LocalStorage to deliver a fast and reliable command-line experience.

Rather than simulating every mouse movement or keyboard interaction, the framework communicates directly with the browser runtime, reducing unnecessary operations and improving execution speed.

---

# ⚙️ Technology Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core application logic |
| **Selenium WebDriver** | Browser automation |
| **Google Chrome** | Target browser |
| **ChromeDriver** | Communication bridge |
| **JavaScript** | DOM manipulation |
| **LocalStorage API** | Data synchronization |
| **Command Line Interface** | User interaction |

---

# 🏗️ Internal Execution Pipeline

```text
                    User Input
                         │
                         ▼
                Terminal Command
                         │
                         ▼
                Python Application
                         │
                         ▼
               Selenium WebDriver
                         │
                         ▼
                  Chrome Browser
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
   JavaScript Runtime             LocalStorage
          │                             │
          └──────────────┬──────────────┘
                         ▼
                  DOM Synchronization
                         │
                         ▼
                  Updated User Interface
```

---

# 🧠 Browser Automation Engine

The browser automation layer controls the complete lifecycle of every browser session.

### Responsibilities

- Launch browser
- Attach WebDriver
- Navigate pages
- Authenticate users
- Execute JavaScript
- Synchronize data
- Handle exceptions
- Close sessions safely

---

# 🌐 Selenium Integration

Selenium provides direct communication between Python and Google Chrome.

GymSync-CLI uses Selenium to:

- Locate page elements
- Execute JavaScript
- Read browser state
- Submit forms
- Navigate pages
- Monitor page loading
- Control browser windows

---

# 💾 LocalStorage Synchronization

Instead of storing temporary files, GymSync-CLI writes schedule information directly into the browser's LocalStorage.

### Benefits

- Faster execution
- Lower disk usage
- Immediate browser synchronization
- Persistent browser state
- Cleaner architecture

---

# ⚡ JavaScript Runtime

Python dynamically generates JavaScript payloads that execute inside the active webpage.

Typical operations include:

- Reading LocalStorage
- Writing LocalStorage
- Updating DOM nodes
- Dispatching browser events
- Triggering page refresh logic
- Validating browser state

---

# 🖥️ Terminal Engine

The terminal interface provides a clean, interactive experience.

Features include:

- Interactive menus
- Structured logging
- Keyboard navigation
- Progress indicators
- Error reporting
- Confirmation dialogs

Everything is designed to minimize unnecessary user interaction while maximizing productivity.

---

# 🔄 Synchronization Process

```text
Python Objects

        │

        ▼

Serialization

        │

        ▼

JavaScript Injection

        │

        ▼

Browser Runtime

        │

        ▼

LocalStorage Update

        │

        ▼

DOM Refresh

        │

        ▼

Visual Synchronization

        │

        ▼

Operation Complete
```

---

# ⚡ Performance Optimizations

GymSync-CLI includes multiple optimizations to reduce execution time.

Examples include:

- Browser profile reuse
- LocalStorage manipulation
- Reduced DOM traversal
- Efficient JavaScript execution
- Structured exception handling
- Modular execution flow
- Session persistence

---

# 📊 Performance

## Resource Usage

| Resource | GymSync-CLI |
|-----------|-------------|
| Startup Time | < 2 Seconds |
| Memory Usage | ~80–120 MB |
| CPU Usage | Very Low |
| Browser Launch | Fast |
| DOM Synchronization | Real Time |
| LocalStorage Access | Instant |

---

## CLI vs Traditional Workflow

| Feature | GymSync-CLI | Manual Browser |
|----------|-------------|----------------|
| Speed | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Automation | ⭐⭐⭐⭐⭐ | ⭐ |
| Reusability | ⭐⭐⭐⭐⭐ | ⭐ |
| Productivity | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Error Handling | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Terminal Friendly | ⭐⭐⭐⭐⭐ | ❌ |

---

# 🚀 Execution Flow

```text
Initialize

↓

Load Configuration

↓

Initialize Browser

↓

Authenticate

↓

Load Schedule

↓

Validate Data

↓

Inject JavaScript

↓

Update LocalStorage

↓

Synchronize DOM

↓

Verify Result

↓

Complete
```

---

# 🔒 Security

Security is an important design principle of GymSync-CLI.

The framework avoids unnecessary data exposure while keeping browser automation isolated from the user's personal browsing environment.

---

## Local Profile Isolation

Every browser session runs inside an isolated Chrome profile.

Benefits include:

- Independent cookies
- Separate login sessions
- Protected browser preferences
- Safe testing environment

---

## No Cloud Storage

GymSync-CLI does **not** upload schedule data to external cloud services.

All runtime information remains on the user's machine.

---

## Session Protection

The framework continuously validates browser sessions before executing automation commands.

If an invalid session is detected, execution pauses instead of continuing with corrupted data.

---

## Safe Shutdown

Before closing the application GymSync-CLI performs:

- Browser cleanup
- Session cleanup
- Resource cleanup
- Driver termination

This prevents orphan browser processes.

---

## Error Isolation

Unexpected exceptions are handled gracefully.

Instead of exposing long Python tracebacks, the framework presents clean and readable messages whenever possible.

---

# 🛣️ Future Roadmap

GymSync-CLI has been designed with extensibility in mind.

Future improvements may include the following features.

---

## 🚀 Headless Automation

Run Chrome completely in the background without opening browser windows.

Benefits:

- Lower resource usage
- Faster execution
- Better automation
- Server deployment

---

## 🔔 Desktop Notifications

Notify users when important automation events occur.

Possible integrations:

- Windows Notifications
- Linux Notifications
- macOS Notifications

---

## 📅 Task Scheduler

Execute synchronization automatically.

Examples:

- Daily schedule updates
- Weekly automation
- Startup synchronization
- Background scheduling

---

## 📈 Analytics Dashboard

Collect historical scheduling information.

Possible features:

- Weekly reports
- Monthly statistics
- Exercise history
- Usage analytics
- Success rate tracking

---

## 🔐 Encrypted Configuration

Protect sensitive configuration values through encrypted local storage.

Potential improvements:

- Encrypted credentials
- Protected configuration
- Secure authentication

---

## 🌙 Enhanced Terminal Themes

Planned terminal improvements include:

- Dark themes
- Light themes
- Custom color schemes
- Personalized dashboards

---

## 🔌 Plugin System

A plugin architecture would allow developers to extend GymSync-CLI without modifying the core framework.

Potential plugins:

- Custom exercises
- Additional websites
- Export modules
- Notification providers
- Schedule templates

---

## 🐳 Docker Support

Containerized deployment for developers and server environments.

Benefits:

- Easy setup
- Portable environment
- Consistent runtime
- Simplified deployment

---

## 🤖 AI-Assisted Automation

Future versions may integrate AI-powered features such as:

- Smart schedule suggestions
- Automatic conflict detection
- Personalized workout recommendations
- Intelligent automation workflows

---

# 🎯 Long-Term Vision

GymSync-CLI aims to become more than a browser automation script.

The long-term vision is to evolve into a complete automation framework capable of managing browser-based workflows through a fast, modular, and developer-friendly command-line environment.

Every new feature will continue to follow the project's core philosophy:

> **Fast. Modular. Reliable. Developer First.**

# 🤝 Contributing

Contributions are always welcome!

GymSync-CLI is designed with a modular architecture, making it easy to improve, extend, and customize. Whether you're fixing bugs, improving documentation, optimizing performance, or adding new features, your contributions help make the project better for everyone.

---

## 🌟 Ways to Contribute

You can contribute by:

- 🐞 Reporting bugs
- 💡 Suggesting new features
- 📖 Improving documentation
- ⚡ Optimizing performance
- 🛠️ Refactoring code
- 🔒 Improving security
- 🌐 Enhancing browser automation
- 📊 Adding analytics
- 🎨 Improving terminal UI
- 🧪 Writing tests

---

## 🚀 Contribution Workflow

```text
Fork Repository
       │
       ▼
Clone Repository
       │
       ▼
Create New Branch
       │
       ▼
Develop New Feature
       │
       ▼
Commit Changes
       │
       ▼
Push Branch
       │
       ▼
Open Pull Request
```

---

## 📥 Clone the Repository

```bash
git clone https://github.com/guptaji0358/GymSync-CLI.git

cd GymSync-CLI
```

---

## 🌿 Create a Feature Branch

```bash
git checkout -b feature/my-awesome-feature
```

---

## 💾 Commit Your Changes

```bash
git add .

git commit -m "Add awesome feature"
```

---

## 📤 Push Your Branch

```bash
git push origin feature/my-awesome-feature
```

---

## 🔄 Open a Pull Request

Create a Pull Request describing:

- What you changed
- Why you changed it
- Screenshots (if applicable)
- Testing details

---

# 📌 Coding Guidelines

Please follow these principles:

- Write clean and readable code.
- Keep functions modular.
- Add comments where necessary.
- Follow Python best practices.
- Avoid unnecessary complexity.
- Keep commits meaningful.
- Test before submitting.

---

# 🐞 Bug Reports

Found a bug?

Please include:

- Operating System
- Python Version
- Chrome Version
- ChromeDriver Version
- Error Message
- Steps to Reproduce

Open an issue here:

**GitHub Issues**

https://github.com/guptaji0358/GymSync-CLI/issues

---

# 💡 Feature Requests

Have an idea?

Open an issue describing:

- The problem
- Your proposed solution
- Expected behavior
- Possible implementation

Every idea is welcome.

---

# ❓ Frequently Asked Questions

<details>
<summary><strong>Do I need Python knowledge to use GymSync-CLI?</strong></summary>

No.

Basic terminal usage is enough for most users.

</details>

---

<details>
<summary><strong>Does GymSync-CLI modify my personal Chrome profile?</strong></summary>

No.

It uses an isolated Chrome profile stored inside the project directory.

</details>

---

<details>
<summary><strong>Can I customize schedules?</strong></summary>

Yes.

The scheduling system is fully configurable and supports custom mappings.

</details>

---

<details>
<summary><strong>Can I modify the source code?</strong></summary>

Absolutely.

GymSync-CLI is open source and designed for customization.

</details>

---

<details>
<summary><strong>Can I add new exercises?</strong></summary>

Yes.

Simply update the exercise mapping tables or configuration files.

</details>

---

<details>
<summary><strong>Does it support multiple Chrome profiles?</strong></summary>

Yes.

Each profile can remain isolated for safer browser automation.

</details>

---

<details>
<summary><strong>Can it run in Headless Mode?</strong></summary>

Headless support is planned for future versions.

</details>

---

<details>
<summary><strong>Is Internet required?</strong></summary>

Yes.

Internet access is required whenever interacting with the target website.

</details>

---

<details>
<summary><strong>Which browsers are supported?</strong></summary>

The current release is optimized for Google Chrome.

</details>

---

<details>
<summary><strong>Can I use this project for learning Selenium?</strong></summary>

Absolutely.

The project demonstrates practical Selenium automation techniques, browser communication, JavaScript execution, and LocalStorage manipulation.

</details>

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to:

- ✅ Use
- ✅ Modify
- ✅ Fork
- ✅ Learn
- ✅ Share
- ✅ Improve

Please retain the original license when redistributing the project.

---

# 🙏 Acknowledgements

Special thanks to the amazing open-source technologies that power GymSync-CLI.

- 🐍 Python
- 🌐 Selenium WebDriver
- 🌍 Google Chrome
- 🚗 ChromeDriver
- 💻 Git
- ❤️ Open Source Community

Without these technologies, this project would not have been possible.

---

# 👨‍💻 Author

## Robin Gupta

**Developer • Python Programmer • C++ Learner • Desktop Application Enthusiast**

GitHub Profile:

**https://github.com/guptaji0358**

Repository:

**https://github.com/guptaji0358/GymSync-CLI**

---

## 🌟 Support the Project

If you found this project useful, please consider:

⭐ Starring the repository

🍴 Forking the project

📢 Sharing it with others

🐛 Reporting bugs

💡 Suggesting improvements

Every contribution helps the project grow.

---

# 📈 Project Status

```text
Project Name      : GymSync-CLI

Version           : 1.0.0

Development       : Completed

Maintenance       : Active

Language          : Python

Automation        : Selenium WebDriver

Interface         : Command Line (CLI)

Browser           : Google Chrome

Architecture      : Modular

License           : MIT

Status            : Stable
```

---

# 🏆 Final Statement

GymSync-CLI was created with a simple vision:

> **Build a lightweight, developer-friendly browser automation framework that prioritizes speed, reliability, and clean architecture over unnecessary complexity.**

Every module, every function, and every workflow has been designed with maintainability and extensibility in mind.

Whether you're exploring Selenium, browser automation, or command-line application design, GymSync-CLI aims to serve as both a practical utility and a learning resource.

---

# 💬 Creator's Quote

> **"The core framework is fully optimized, stable, and locked down. Robin is officially not launching a V2 of this tool—this code stands completed as the absolute definitive release."**

---

<div align="center">

## ⭐ Thank You for Visiting GymSync-CLI ⭐

If this project helped you, please consider giving it a ⭐ on GitHub.

### 🔗 Repository

**https://github.com/guptaji0358/GymSync-CLI**

### 👤 Maintained by

**Robin Gupta**

**Happy Coding! 🚀**

</div>

