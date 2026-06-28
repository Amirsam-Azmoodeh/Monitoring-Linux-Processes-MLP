# 🖥️ MLP - Monitoring Linux Processes

> **A lightweight, real-time process monitoring tool for Linux**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=mit)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey?style=for-the-badge&logo=linux)](https://linux.org)
[![Made With ❤️](https://img.shields.io/badge/Made%20With-❤️-red?style=for-the-badge)](https://github.com/yourusername/mlp)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge&logo=github)](https://github.com/yourusername/mlp/pulls)

---

## 📖 Table of Contents

- [✨ Why MLP?](#-why-mlp)
- [🚀 Features](#-features)
- [🛠️ How It Works](#️-how-it-works)
- [📦 Installation](#-installation)
- [⚡ Quick Start](#-quick-start)
- [📸 Screenshots](#-screenshots)
- [📚 Usage](#-usage)
- [📁 Project Structure](#️-project-structure)
- [🔧 Technical Details](#-technical-details)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## ✨ Why MLP?

**Ever wondered what `top` or `htop` do under the hood?**

MLP (Monitoring Linux Processes) is a **minimal, educational, and functional** process monitor that reads system information directly from the `/proc` virtual filesystem — the same source that tools like `top`, `ps`, and `htop` use.

This project was built as a learning experience to understand:
- How the Linux `/proc` filesystem works
- How to calculate CPU usage per process
- How to read memory and system statistics
- How to build a real-time terminal UI

---

## 🚀 Features

### 📊 Real-time Monitoring
- 🔄 Updates every **1 second**
- 📈 Shows **top 20 processes** by CPU usage
- 🎨 **Color-coded** CPU and memory usage
  - 🔴 > 50% (Red)
  - 🟡 25-50% (Yellow)
  - 🟢 < 25% (Green)

### 📋 Comprehensive Information
| Category | Details |
|----------|---------|
| **System** | Uptime, Load Average (1, 5, 15 min) |
| **Memory** | Total, Free, Used with percentage |
| **CPU** | Number of cores |
| **Processes** | Total count and status breakdown |
| **Per Process** | PID, User, Status, CPU%, MEM%, Runtime, Command |

### 🎯 Process Status Codes
| Status | Meaning | Color |
|--------|---------|-------|
| **R** | Running | 🟢 Green |
| **S** | Sleeping | 🔵 Blue |
| **T** | Stopped | 🟡 Yellow |
| **Z** | Zombie | 🔴 Red |
| **X** | Dead | 🔴 Red |

### ⚡ Performance
- No external dependencies
- Pure Python standard library
- Minimal CPU overhead
- Lightweight memory usage

---

## 🛠️ How It Works

### Data Source: `/proc` Filesystem

Linux exposes system and process information through the virtual `/proc` filesystem:

/proc/
├── uptime # System uptime in seconds
├── loadavg # Load average (1, 5, 15 min)
├── meminfo # Memory information
├── [PID]/ # Process directory
│ ├── stat # Process statistics
│ └── status # Process status (includes UID)
text


### CPU Calculation

CPU usage is calculated by tracking the difference in CPU time between updates:

```python
cpu_percent = (cpu_time_diff / real_time_diff) * 100

This is the same method used by top and htop!
Memory Calculation

Memory usage (RSS - Resident Set Size) is read from /proc/[PID]/stat and converted to a percentage of total system memory.
📦 Installation
Prerequisites

    🐧 Linux (uses /proc filesystem)

    🐍 Python 3.8 or higher

Step 1: Clone the Repository
bash

git clone https://github.com/yourusername/mlp.git
cd mlp

Step 2: Make it Executable (Optional)
bash

chmod +x mlp.py

Step 3: Run the Monitor
bash

python3 mlp.py

⚡ Quick Start
bash

# Clone and run in one go
git clone https://github.com/yourusername/mlp.git
cd mlp
python3 mlp.py

# Press Ctrl+C to exit

That's all! No installation, no dependencies, just pure Python.
📸 Screenshots
Main Interface
text

=====================================================================================
System Uptime: 12:34:56
Load Average: 0.45  0.32  0.28
Memory: Total: 15.6GB | Free: 8.2GB | Used: 7.4GB (47.4%)
CPU Cores: 8 | Processes: 234
R:003  S:226  T:002  Z:001  X:002
=====================================================================================

   PID  USER         S  %CPU  %MEM       TIME  COMMAND
-------------------------------------------------------------------------------------
  1234  amirsam      R  45.2   12.3   1:23:45  chrome
  5678  root         S  12.5    5.6   0:45:12  python3
  9012  amirsam      S   8.3    3.4   0:12:34  code
  ...
-------------------------------------------------------------------------------------
Top 20 processes by CPU usage | Refresh: 1s | Press Ctrl+C to exit

Color Legend

    🔴 Red: High usage (CPU > 50%, MEM > 50%)

    🟡 Yellow: Medium usage (CPU > 25%, MEM > 25%)

    🟢 Green: Low usage (CPU < 25%, MEM < 25%)

📚 Usage
Command Line
bash

# Standard usage
python3 mlp.py

# With different refresh rate (modify the code)
# Change time.sleep(1) to time.sleep(N) where N is seconds

Keyboard Shortcuts
Key	Action
Ctrl+C	Exit the monitor gracefully
📁 Project Structure
text

mlp/
├── 📄 mlp.py               # Main application (entry point)
├── 📄 get_data.py          # Data collection from /proc
├── 📄 calculate.py         # CPU, memory, runtime calculations
├── 📄 README.md            # This file
├── 📄 LICENSE              # MIT License
├── 📄 requirements.txt     # Dependencies (none needed)
└── 📄 .gitignore           # Git ignore file

Module Breakdown
mlp.py (Main)

    Role: Application entry point and UI rendering

    Functions:

        format_uptime() - Human-readable uptime

        format_memory() - Human-readable memory

        get_color() - Status color mapping

        clear_screen() - Terminal clear

        main() - Main loop

get_data.py (Data Collection)

    Role: Read system data from /proc

    Functions:

        uptime() - System uptime

        meminfo() - Memory information

        loadavg() - Load average

        stat(pid) - Process statistics

calculate.py (Calculations)

    Role: Process metrics calculations

    Functions:

        proc_runtime() - Process runtime

        proc_memory() - Memory percentage

        proc_cpu() - CPU usage percentage

    Constants:

        clk_tck - Clock ticks per second

        page_size - Memory page size

🔧 Technical Details
CPU Calculation Method
python

cpu_diff_ticks = total_cpu_time - prev_cpu_time
real_time_diff = current_real_time - prev_real_time
cpu_percent = (cpu_diff_ticks / clk_tck / real_time_diff) * 100

Memory Calculation Method
python

rss_bytes = rss_pages * page_size
mem_percent = (rss_bytes / total_memory) * 100

Process States (from /proc/[PID]/stat)
State	Description
R	Running
S	Sleeping (interruptible)
D	Disk sleep (uninterruptible)
T	Stopped
Z	Zombie
X	Dead
🤝 Contributing

I ❤️ contributions! Here's how you can help:
📋 Ways to Contribute

    🐛 Report bugs - Open an issue

    💡 Suggest features - I'm open to ideas

    📝 Improve documentation - Fix typos, add examples

    🔧 Submit PRs - Fix issues or add features

🚀 Development Process

    Fork the repository

    Create a branch: git checkout -b feature/amazing-feature

    Make your changes

    Test: python3 mlp.py

    Commit: git commit -m 'Add amazing feature'

    Push: git push origin feature/amazing-feature

    Open a Pull Request

💡 Feature Ideas

    Sorting by memory, PID, or time

    Filtering by user or status

    Network statistics

    Disk I/O monitoring

    Export to CSV/JSON

    Command-line arguments (-u, -m, -p)

    Color themes

    Process tree view

📄 License

Copyright 2024 Amirsam Azmoodeh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
📬 Contact

Amirsam Azmoodeh

https://img.shields.io/badge/Email-amirsamazmoodeh%2540gmail.com-red?style=for-the-badge&logo=gmail
https://img.shields.io/badge/LinkedIn-Amirsam%2520Azmoodeh-blue?style=for-the-badge&logo=linkedin
https://img.shields.io/badge/GitHub-AmirsamAzmoodeh-black?style=for-the-badge&logo=github
🙏 Acknowledgments

    Linux /proc Filesystem - The heart of this tool

    Python Community - For the excellent standard library

    All Contributors - Who help improve this project

📚 Further Reading

    Linux /proc Filesystem Documentation

    Understanding Linux Process States

    Python os.sysconf() Documentation

    How top Works

🌟 Show Your Support

If you found this project helpful or interesting, please give it a ⭐ on GitHub!

https://img.shields.io/github/stars/yourusername/mlp?style=social

Made with ❤️ and ☕ by Amirsam Azmoodeh

"Understanding how your system works is the first step to mastering it!" 🖥️