# 📝 Changelog

All notable changes to MLP (Monitoring Linux Processes) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-06-28

### 🎉 Initial Release

#### Added
- Real-time process monitoring
- System uptime display
- Load average display (1, 5, 15 min)
- Memory information (total, free, used)
- CPU core count display
- Process count and status breakdown
- Top 20 processes by CPU usage
- Color-coded CPU and memory usage
- Process status color coding
- Human-readable uptime format
- Human-readable memory format
- Auto-refresh every 1 second
- Ctrl+C graceful exit

#### Technical
- Reads from `/proc` filesystem
- CPU usage calculation with delta tracking
- Memory usage calculation from RSS
- Process runtime calculation
- No external dependencies
- Python standard library only

#### Known Issues
- First iteration of CPU usage shows 0.0% (needs two samples)
- No command-line arguments support
- No sorting options

## [0.1.0] - 2024-06-15

### 🎬 Initial Development

#### Added
- Basic project structure
- Data collection from `/proc`
- Preliminary calculations
- Prototype UI