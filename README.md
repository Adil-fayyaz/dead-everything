# 🔥 Multi-Platform Social Media Reporter

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Multi--Platform-green.svg)](https://github.com)
[![Anonymity](https://img.shields.io/badge/Anonymity-Tor%20%7C%20Proxy-orange.svg)](https://www.torproject.org/)
[![License](https://img.shields.io/badge/License-GPL-blue.svg)](LICENSE)

**Advanced Multi-Platform Social Media Reporter** - A powerful tool for automating user reports across **7 major social media platforms** with complete anonymity support.

> 👨‍💻 **Created by [Infinity X White devels team](https://github.com/Adil-fayyaz)** 👨‍💻

> ⚠️ **CRITICAL LEGAL WARNING** ⚠️
> 
> This tool is for **EDUCATIONAL and RESEARCH purposes ONLY**. Using this tool violates Terms of Service of all platforms. Your accounts can be **PERMANENTLY BANNED**. Use at your own risk.

---

## 🌐 Supported Platforms

| Platform | Emoji | Status | Difficulty |
|----------|-------|--------|------------|
| **Instagram** | 📸 | ✅ Full Support | Easy |
| **TikTok** | 🎵 | ✅ Full Support | Easy |
| **Twitter/X** | 🐦 | ✅ Full Support | Medium |
| **Facebook** | 👥 | ✅ Full Support | Medium |
| **YouTube** | ▶️ | ✅ Full Support | Hard |
| **Reddit** | 🤖 | ✅ Full Support | Easy |
| **LinkedIn** | 💼 | ✅ Full Support | Hard |

---

## 🛡️ Features

### 🌐 Multi-Platform Support
- **7 Social Media Platforms** - Instagram, TikTok, Twitter/X, Facebook, YouTube, Reddit, LinkedIn
- **Multi-Platform Mode** - Report on all platforms simultaneously
- **Platform-Specific Optimizations** - Customized for each platform

### 🛡️ Advanced Anonymity & Privacy
- **Tor Network Support** - Route traffic through Tor for maximum anonymity
- **Proxy Rotation** - Automatic proxy rotation with validation
- **Fingerprint Randomization** - Complete browser fingerprint spoofing
- **Encrypted Credentials** - AES-256 encrypted credential storage
- **IP/DNS Leak Protection** - Prevents IP and DNS leaks
- **WebRTC Leak Protection** - Blocks WebRTC IP leaks
- **Anonymity Score** - Real-time anonymity level monitoring (0-100)

### ⚡ Advanced Functionality
- **Session Persistence** - Save and load login sessions
- **Anti-Detection Measures** - Random user agents, human-like behavior
- **Advanced Logging** - Detailed logs saved to files
- **Error Screenshots** - Automatic screenshots for debugging
- **Rate Limiting** - Configurable delays between reports
- **Batch Processing** - Process multiple targets

### 📱 Platform Support
- **Desktop** - Windows, Linux, macOS
- **Mobile** - Android via Termux (NEW!)

---

## 📋 Requirements

### Desktop (Windows/Linux/macOS)
- Python 3.7+
- Google Chrome browser
- ChromeDriver (auto-downloaded)
- Stable internet connection
- Required Python packages (see requirements.txt)

### Mobile (Android/Termux)
- Android 7.0+
- Termux app (from F-Droid or GitHub)
- Python 3.7+ (via Termux)
- Tor (optional, for anonymity)
- See `TERMUX_GUIDE.md` for complete setup

---

## 🚀 Quick Start

### Desktop Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/INSTA-REPORT.git
cd INSTA-REPORT-main

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the tool
python3 anonymous_reporter.py
```

### Termux/Android Installation

```bash
# 1. Install Termux from F-Droid or GitHub
# 2. Run setup script
chmod +x termux_setup.sh
./termux_setup.sh

# 3. Start Tor (for anonymity)
tor &

# 4. Run reporter
python3 anonymous_reporter.py
```

---

## 📖 Usage

### Option 1: Anonymous Reporter (Recommended)

```bash
python3 anonymous_reporter.py
```

**Features:**
- Full anonymity support (Tor/Proxy)
- Fingerprint randomization
- Encrypted credentials
- 5 anonymity levels
- Real-time anonymity score

### Option 2: Multi-Platform Reporter

```bash
python3 multi_platform_reporter.py
```

**Features:**
- Select one or multiple platforms
- All 7 platforms supported
- Detailed statistics
- Platform-specific optimization

### Option 3: Advanced Reporter (Instagram + TikTok)

```bash
python3 advanced_reporter.py
```

**Features:**
- Instagram and TikTok support
- Session management
- Anti-detection measures

### Option 4: Original (Instagram Only)

```bash
python3 insta-report.py
```

**Features:**
- Instagram only
- Basic functionality

---

## 🔒 Anonymity Setup

### Anonymity Levels

| Level | Score | Features |
|-------|-------|----------|
| **👻 MAXIMUM** | 95/100 | Tor + Proxy + Full Fingerprint + Encryption |
| **🛡️ HIGH** | 75/100 | Proxy Rotation + Fingerprint + Encryption |
| **🔐 MEDIUM** | 50/100 | Fingerprint Randomization + Encryption |
| **⚠️ LOW** | 30/100 | Basic Fingerprint Spoofing |
| **🚫 NONE** | 0/100 | No Protection (NOT RECOMMENDED) |

### Tor Setup

#### Windows:
1. Download [Tor Browser](https://www.torproject.org/download/)
2. Install and run Tor Browser
3. Tor runs on port 9050 by default

#### Linux:
```bash
sudo apt install tor
sudo systemctl start tor
sudo systemctl enable tor
```

#### macOS:
```bash
brew install tor
brew services start tor
```

#### Termux/Android:
```bash
pkg install tor
tor &
```

### Proxy Setup

1. Create `proxies.txt`:
```bash
cp proxies.txt.example proxies.txt
nano proxies.txt
```

2. Add your proxies (one per line):
```
http://proxy1.com:8080
socks5://proxy2.com:1080
http://user:pass@proxy3.com:3128
```

3. Tool validates and rotates proxies automatically

**Full Guide:** See `ANONYMITY_GUIDE.md` for complete anonymity documentation

---

## ⚙️ Configuration

### config.json

Main configuration file with settings for all platforms:

```json
{
    "instagram": {
        "default_delay": 30,
        "max_reports_per_session": 10,
        "headless": false
    },
    "tiktok": {
        "default_delay": 45,
        "max_reports_per_session": 10
    },
    "twitter": {
        "default_delay": 35,
        "max_reports_per_session": 8
    },
    "anonymity": {
        "enable_tor": false,
        "enable_proxy_rotation": false,
        "enable_fingerprint_randomization": true,
        "encrypt_credentials": false
    }
}
```

See `config.json` for all available options.

---

## 📁 Project Structure

```
INSTA-REPORT-main/
├── anonymous_reporter.py       # 🛡️ Anonymous version (Tor/Proxy)
├── termux_reporter.py          # 🐧 Termux/Android version
├── termux_setup.sh             # 🐧 Termux installation script
├── multi_platform_reporter.py  # 🌟 Multi-platform script (7 platforms)
├── advanced_reporter.py        # Advanced version (Instagram + TikTok)
├── insta-report.py             # Original (Instagram only)
├── social_reporter.py          # Base reporter class
├── anonymity_manager.py        # 🛡️ Anonymity manager
├── config.json                 # Configuration file
├── requirements.txt            # Python dependencies
├── proxies.txt.example         # Proxy list template
│
├── platforms/                  # Platform-specific implementations
│   ├── instagram_reporter.py
│   ├── tiktok_reporter.py
│   ├── twitter_reporter.py
│   ├── facebook_reporter.py
│   ├── youtube_reporter.py
│   ├── reddit_reporter.py
│   └── linkedin_reporter.py
│
├── docs/                       # Documentation
│   ├── ANONYMITY_GUIDE.md      # Complete anonymity guide
│   ├── TERMUX_GUIDE.md         # Termux/Android guide
│   └── PLATFORMS_GUIDE.md      # Platform-specific guide
│
├── sessions/                   # Saved sessions (auto-created)
├── encrypted_credentials/      # Encrypted credentials (auto-created)
├── logs/                       # Log files (auto-created)
└── screenshots_errors/         # Error screenshots (auto-created)
```

---

## 🐧 Termux/Android Support

Full support for Android devices via Termux with complete anonymity features!

### Quick Setup

```bash
# 1. Install Termux from F-Droid
# 2. Run setup script
./termux_setup.sh

# 3. Start Tor (for anonymity)
tor &

# 4. Run reporter
python3 anonymous_reporter.py
```

**Features:**
- ✅ Headless mode (no GUI required)
- ✅ Full Tor support
- ✅ Proxy rotation
- ✅ Mobile optimized
- ✅ All 7 platforms supported

**Full Guide:** See `TERMUX_GUIDE.md` for complete Termux documentation

---

## 📊 Platform-Specific Settings

| Platform | Default Delay | Max Reports | Recommended |
|----------|---------------|-------------|-------------|
| Instagram | 30s | 10 | 5-10 |
| TikTok | 45s | 10 | 5-10 |
| Twitter/X | 35s | 8 | 5-8 |
| Facebook | 40s | 8 | 5-8 |
| YouTube | 50s | 5 | 3-5 |
| Reddit | 35s | 10 | 5-10 |
| LinkedIn | 60s | 5 | 3-5 |

**Note:** Delays and limits are configurable in `config.json`

---

## ⚠️ Important Warnings

### Legal & Ethical

1. ⚠️ This tool **violates Terms of Service** of all platforms
2. 🚫 Your accounts **CAN BE PERMANENTLY BANNED**
3. ⚖️ Abuse may have **LEGAL CONSEQUENCES**
4. 💀 Use **AT YOUR OWN RISK**
5. 📚 **EDUCATIONAL USE ONLY**
6. 🛡️ **DO NOT USE FOR ILLEGAL ACTIVITIES**

### Technical

1. Platforms frequently update their interfaces (selectors may need updates)
2. Anti-bot systems are sophisticated (detection possible)
3. Anonymity does NOT guarantee 100% protection
4. Use test accounts, NOT your main accounts
5. Respect rate limits to avoid detection
6. Always use responsibly and ethically

---

## 🔧 Troubleshooting

### Common Issues

#### Login Failed
- Check credentials
- Platform may require 2FA/verification
- Try clearing sessions folder

#### Report Failed
- Platform updated interface (selectors need update)
- Increase delays in config.json
- Reduce max_reports_per_session
- Check error screenshots in `screenshots_errors/`

#### Tor/Proxy Not Working
- Verify Tor is running: `curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip`
- Check proxy format in `proxies.txt`
- Validate proxies before use

#### Termux Issues
- Run `termux-setup-storage` for permissions
- Install missing packages: `pkg install python git tor`
- Check `TERMUX_GUIDE.md` for detailed troubleshooting

### Getting Help

1. Check logs in `logs/` directory
2. Review error screenshots in `screenshots_errors/`
3. See documentation:
   - `ANONYMITY_GUIDE.md` - Anonymity setup
   - `TERMUX_GUIDE.md` - Termux/Android setup
   - `PLATFORMS_GUIDE.md` - Platform-specific guide
4. Check if platform updated their interface
5. Increase delays and reduce report count

---

## 📚 Documentation

- **README.md** - This file (main documentation)
- **ANONYMITY_GUIDE.md** - Complete anonymity guide (Tor, Proxy, Fingerprint)
- **TERMUX_GUIDE.md** - Complete Termux/Android guide
- **PLATFORMS_GUIDE.md** - Platform-specific guide and tips

---

## 🛠️ Advanced Features

### Session Management
- Sessions automatically saved after login
- Reload sessions to skip login step
- Stored in `sessions/` directory per platform

### Encrypted Credentials
- AES-256 encryption with master password
- Secure storage in `encrypted_credentials/`
- Never stored in plain text

### Logging
- All actions logged to `logs/` directory
- Daily log files with timestamps
- Both file and console output

### Error Screenshots
- Automatic screenshots on errors
- Saved to `screenshots_errors/` directory
- Helpful for debugging

### Proxy Rotation
- Automatic proxy switching every N reports
- Validation before use
- Supports HTTP, HTTPS, SOCKS5

---

## 📊 Statistics & Reporting

The tool provides comprehensive statistics:
- Per-platform success/failure rates
- Total reports sent across all platforms
- Detailed logs for each platform
- Error screenshots for debugging
- Session information
- Timing and performance metrics
- Anonymity score tracking

---

## 🔐 Security Best Practices

### DO:
✅ Use Tor for maximum anonymity
✅ Use different accounts per platform
✅ Encrypt credentials
✅ Clear cookies/cache after sessions
✅ Use proxy rotation
✅ Test for IP/DNS leaks before reporting
✅ Use test accounts, NOT main accounts
✅ Keep software updated

### DON'T:
❌ Use your main accounts
❌ Share your proxies file
❌ Store credentials in plain text
❌ Use for illegal activities
❌ Ignore warnings
❌ Use without anonymity on public networks
❌ Trust 100% anonymity

---

## 🚀 Performance Tips

### For Better Performance:
- Use WiFi instead of mobile data (Termux)
- Close other apps to free memory
- Use proxy instead of Tor (faster)
- Reduce report count per session
- Increase delays between reports

### For Better Anonymity:
- Use Tor (slower but more anonymous)
- Rotate proxies frequently
- Enable fingerprint randomization
- Encrypt credentials
- Clear cookies/cache after sessions

---

## 📦 Installation Commands

### Desktop (Linux/macOS)

```bash
# Clone repository
git clone https://github.com/yourusername/INSTA-REPORT.git
cd INSTA-REPORT-main

# Install dependencies
pip install -r requirements.txt

# Run tool
python3 anonymous_reporter.py
```

### Desktop (Windows)

```cmd
# Clone repository
git clone https://github.com/yourusername/INSTA-REPORT.git
cd INSTA-REPORT-main

# Install dependencies
pip install -r requirements.txt

# Run tool
python anonymous_reporter.py
```

### Termux/Android

```bash
# Run setup script
chmod +x termux_setup.sh
./termux_setup.sh

# Start Tor (optional)
tor &

# Run tool
python3 anonymous_reporter.py
```

---

## 🔄 Updating

### Update Code:
```bash
git pull origin main
```

### Update Dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Update Termux Packages:
```bash
pkg update && pkg upgrade
```

---

## 📝 License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

**THIS TOOL IS FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY.**

- The authors are NOT responsible for misuse of this tool
- Using this tool violates Terms of Service of all platforms
- Your accounts CAN and WILL be banned if detected
- Legal consequences may apply for abuse
- Use at your own risk
- DO NOT use for illegal activities, harassment, or cyberbullying

**By using this tool, you accept FULL RESPONSIBILITY for your actions.**

---

## 🙏 Credits

- **Created by**: [Infinity X White devels team](https://github.com/Adil-fayyaz)
- **Original Author**: @the_silent_hacker_raj
- **YouTube Channel**: Hacker Colony Official
- **Platforms**: All 7 platforms fully supported
- **Anonymity**: Tor, Proxy, Fingerprint support
- **Mobile**: Termux/Android support

---

> 👨‍💻 **Developed by Infinity X White devels team** 👨‍💻

---

## 📞 Support

For issues and questions:
1. Check documentation in `docs/` directory
2. Review logs in `logs/` directory
3. Check error screenshots in `screenshots_errors/`
4. Review platform-specific guides
5. Check if platform updated their interface

---

## 🌟 Features Summary

- ✅ **7 Social Media Platforms** - Instagram, TikTok, Twitter/X, Facebook, YouTube, Reddit, LinkedIn
- ✅ **Full Anonymity Support** - Tor, Proxy Rotation, Fingerprint Randomization
- ✅ **Multi-Platform Mode** - Report on all platforms simultaneously
- ✅ **Session Management** - Save and load sessions
- ✅ **Encrypted Credentials** - AES-256 encryption
- ✅ **Advanced Logging** - Detailed logs and screenshots
- ✅ **Termux/Android Support** - Full mobile support
- ✅ **Anti-Detection** - Human-like behavior, random delays
- ✅ **Rate Limiting** - Configurable delays
- ✅ **Error Handling** - Comprehensive error recovery

---

## 🎯 Quick Reference

```bash
# Anonymous Reporter (Recommended)
python3 anonymous_reporter.py

# Multi-Platform Reporter
python3 multi_platform_reporter.py

# Termux/Android
./termux_setup.sh
python3 anonymous_reporter.py

# Start Tor
tor &

# Check Tor
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

---

**Remember**: Use responsibly, legally, and ethically! 🛡️

**Stay Anonymous, Stay Safe, Stay Legal!** 👻🔒
