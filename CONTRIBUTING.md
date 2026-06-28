# 🤝 Contributing to MLP

First off, thank you for considering contributing to MLP! 🎉

## 📋 Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and inclusive.

## 🚀 How Can I Contribute?

### 🐛 Reporting Bugs

- **Use a clear title** describing the issue
- **Describe the steps** to reproduce
- **Describe what you expected** vs what happened
- **Include screenshots** if possible
- **Mention your Linux distribution** and Python version

### 💡 Suggesting Enhancements

- **A clear title**
- **A step-by-step description** of the enhancement
- **Examples** of how it would be used
- **Why it would be useful** for others

### 🔧 Pull Requests

1. **Fork** the repository
2. **Create a branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test**: `python3 mlp.py`
5. **Commit**: `git commit -m 'Add amazing feature'`
6. **Push**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

## 📝 Development Setup

### Prerequisites
- 🐧 Linux
- 🐍 Python 3.8+

### Setup
```bash
git clone https://github.com/your-username/mlp.git
cd mlp
python3 mlp.py

🧪 Testing
bash

# Test data collection
python3 -c "from get_data import loadavg, meminfo, uptime; print(loadavg(), meminfo(), uptime())"

# Test CPU calculation
python3 -c "from calculate import proc_cpu; print(proc_cpu('1', 0, 0, 0, 0, 8))"

📚 Code Style

    Follow PEP 8

    Use 4 spaces for indentation

    Maximum line length: 100 characters

    Use descriptive variable names

    Add docstrings for functions

Docstring Example
python

def proc_cpu(pid, utime, stime, cutime, cstime, cores_count):
    """
    Calculate CPU usage percentage for a process.
    
    Args:
        pid: Process ID
        utime: User time in ticks
        stime: System time in ticks
        cutime: Child user time in ticks
        cstime: Child system time in ticks
        cores_count: Number of CPU cores
        
    Returns:
        float: CPU usage percentage (0-100)
    """

💡 Feature Ideas

Looking for something to work on? Here are some ideas:
Easy

    Add -h or --help command-line argument

    Add version number display

    Improve error messages

Medium

    Add sorting by memory, PID, or time

    Add filtering by user or status

    Add network statistics

    Export to CSV/JSON

Advanced

    Add process tree view

    Add color themes

    Add disk I/O monitoring

    Add command-line arguments for refresh rate

❓ Questions?

Feel free to open an issue or contact:

    Email: amirsamazmoodeh@gmail.com

    LinkedIn: Amirsam Azmoodeh

🙏 Thank You!

Your contributions are appreciated! 🎉