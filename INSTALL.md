# 📦 Installation Guide

Complete installation instructions for all platforms.

---

## 🖥️ Desktop Installation

### Windows

```cmd
# 1. Install Python 3.7+ from python.org
# 2. Install Google Chrome browser

# 3. Open Command Prompt or PowerShell
# 4. Clone repository
git clone https://github.com/yourusername/INSTA-REPORT.git
cd INSTA-REPORT-main

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run tool
python anonymous_reporter.py
```

### Linux (Ubuntu/Debian)

```bash
# 1. Update packages
sudo apt update && sudo apt upgrade -y

# 2. Install Python and dependencies
sudo apt install -y python3 python3-pip git chromium-browser

# 3. Clone repository
git clone https://github.com/yourusername/INSTA-REPORT.git
cd INSTA-REPORT-main

# 4. Install Python packages
pip3 install -r requirements.txt

# 5. Run tool
python3 anonymous_reporter.py
```

### macOS

```bash
# 1. Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install Python and Chrome
brew install python3
brew install --cask google-chrome

# 3. Clone repository
git clone https://github.com/yourusername/INSTA-REPORT.git
cd INSTA-REPORT-main

# 4. Install Python packages
pip3 install -r requirements.txt

# 5. Run tool
python3 anonymous_reporter.py
```

---

## 📱 Termux/Android Installation

### Step 1: Install Termux

**Option A: F-Droid (Recommended)**
1. Download F-Droid: https://f-droid.org/
2. Install F-Droid
3. Search for "Termux" in F-Droid
4. Install Termux

**Option B: GitHub Releases**
1. Visit: https://github.com/termux/termux-app/releases
2. Download latest APK
3. Install APK (enable "Install from Unknown Sources" if needed)

### Step 2: Run Setup Script

```bash
# 1. Open Termux
# 2. Download or copy the code to Termux
# Option A: Download directly
wget https://github.com/yourusername/INSTA-REPORT/archive/main.zip
unzip main.zip
cd INSTA-REPORT-main

# Option B: Use git (if available)
git clone https://github.com/yourusername/INSTA-REPORT.git
cd INSTA-REPORT-main

# 3. Make script executable
chmod +x termux_setup.sh

# 4. Run setup
./termux_setup.sh

# 5. Grant storage permission when prompted
termux-setup-storage
```

### Step 3: Start Using

```bash
# Start Tor (for anonymity - optional)
tor &

# Run reporter
python3 anonymous_reporter.py
```

**Full Guide:** See `TERMUX_GUIDE.md` for complete Termux documentation

---

## 🔒 Anonymity Setup

### Tor Installation

#### Windows
1. Download Tor Browser: https://www.torproject.org/download/
2. Install and run Tor Browser
3. Tor runs on port 9050 automatically

#### Linux
```bash
sudo apt install tor
sudo systemctl start tor
sudo systemctl enable tor

# Verify
sudo systemctl status tor
```

#### macOS
```bash
brew install tor
brew services start tor

# Verify
brew services list | grep tor
```

#### Termux/Android
```bash
pkg install tor
tor &

# Verify
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

### Proxy Setup

1. Create `proxies.txt`:
```bash
cp proxies.txt.example proxies.txt
nano proxies.txt
```

2. Add proxies (one per line):
```
http://proxy1.com:8080
socks5://proxy2.com:1080
http://user:pass@proxy3.com:3128
```

3. Tool validates proxies automatically on startup

---

## 📋 Dependencies

### Required Python Packages

All packages are in `requirements.txt`:

```
colorama>=0.4.6
requests>=2.31.0
selenium>=4.15.0
webdriver-manager>=4.0.1
cryptography>=41.0.0
PySocks>=1.7.1
stem>=1.8.2
```

### System Requirements

**Desktop:**
- Python 3.7+
- Google Chrome browser
- 2GB RAM minimum
- Stable internet connection

**Termux/Android:**
- Android 7.0+
- Termux app
- 2GB RAM minimum
- WiFi recommended

---

## ✅ Verification

After installation, verify everything works:

```bash
# 1. Check Python version
python3 --version  # Should be 3.7+

# 2. Check packages
python3 -c "import selenium, colorama, cryptography; print('✅ All packages installed')"

# 3. Test tool (without running)
python3 -c "from anonymity_manager import AnonymityManager; print('✅ Tool imports successfully')"

# 4. Check Tor (if installed)
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

---

## 🐛 Troubleshooting

### Python Not Found

**Windows:**
- Add Python to PATH during installation
- Or use `py` instead of `python`

**Linux/macOS:**
- Use `python3` instead of `python`
- Install Python 3: `sudo apt install python3` (Linux) or `brew install python3` (macOS)

### Package Installation Fails

```bash
# Upgrade pip first
pip install --upgrade pip

# Install packages individually
pip install colorama
pip install requests
pip install selenium
pip install webdriver-manager
pip install cryptography
pip install PySocks
pip install stem
```

### Chrome/Chromium Issues

**Desktop:**
- Install Google Chrome: https://www.google.com/chrome/
- ChromeDriver is auto-downloaded by webdriver-manager

**Termux:**
- ChromeDriver is auto-downloaded
- Headless mode is used (no GUI)

### Tor Not Working

**Check if Tor is running:**
```bash
# Linux/macOS
sudo systemctl status tor

# Termux
ps aux | grep tor
```

**Start Tor:**
```bash
# Linux
sudo systemctl start tor

# macOS
brew services start tor

# Termux
tor &
```

**Verify Tor connection:**
```bash
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

### Permission Errors (Termux)

```bash
# Grant storage permission
termux-setup-storage

# Make scripts executable
chmod +x *.sh
chmod +x *.py
```

---

## 📚 Next Steps

After installation:

1. **Configure anonymity** - See `ANONYMITY_GUIDE.md`
2. **Setup Termux** - See `TERMUX_GUIDE.md` (if on Android)
3. **Read platform guide** - See `PLATFORMS_GUIDE.md`
4. **Configure settings** - Edit `config.json`
5. **Start reporting** - Run `python3 anonymous_reporter.py`

---

## 🔄 Updating

### Update Code
```bash
git pull origin main
```

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Update Termux Packages
```bash
pkg update && pkg upgrade
pip install --upgrade -r requirements.txt
```

---

## 📞 Need Help?

1. Check `README.md` - Main documentation
2. Check `ANONYMITY_GUIDE.md` - Anonymity setup
3. Check `TERMUX_GUIDE.md` - Termux/Android setup
4. Check `PLATFORMS_GUIDE.md` - Platform-specific guide
5. Check logs in `logs/` directory
6. Check error screenshots in `screenshots_errors/`

---

**Installation complete! Ready to use!** 🎉
