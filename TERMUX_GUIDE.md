# 🐧 Complete Termux/Android Installation Guide

## 📱 Termux Setup - Android Devices

This guide will help you install and run the Multi-Platform Social Media Reporter on Android using Termux with **full anonymity support**.

---

## 📋 Prerequisites

1. **Android Device** (Android 7.0+ recommended)
2. **Termux App** (download from F-Droid or GitHub)
   - **F-Droid**: https://f-droid.org/packages/com.termux/
   - **GitHub**: https://github.com/termux/termux-app/releases
3. **Internet Connection** (WiFi recommended)
4. **Storage Permission** (will be requested during setup)

---

## 🚀 Quick Installation

### Step 1: Install Termux

1. Download Termux from F-Droid (recommended) or GitHub
2. Install the APK
3. Open Termux app

### Step 2: Run Setup Script

```bash
# Download the setup script
curl -O https://raw.githubusercontent.com/your-repo/INSTA-REPORT/main/termux_setup.sh

# Or if you have the files locally:
cd ~/storage/downloads
# Navigate to where you extracted INSTA-REPORT-main
cd INSTA-REPORT-main

# Make script executable
chmod +x termux_setup.sh

# Run setup
./termux_setup.sh
```

### Step 3: Grant Storage Permission

The script will automatically request storage permission. Grant it when prompted.

### Step 4: Navigate to Code Directory

```bash
cd ~/INSTA-REPORT-main
# or wherever you placed the code
```

### Step 5: Start Using

```bash
# With anonymity (recommended)
python3 anonymous_reporter.py

# Quick start (faster, less anonymous)
python3 multi_platform_reporter.py
```

---

## 🔧 Manual Installation (Alternative)

If the script doesn't work, install manually:

### 1. Update Packages

```bash
pkg update && pkg upgrade
```

### 2. Install Required Packages

```bash
pkg install -y \
    python \
    git \
    wget \
    curl \
    tor \
    openssl \
    nano
```

### 3. Install Python Dependencies

```bash
pip install --upgrade pip

pip install \
    colorama \
    requests \
    selenium \
    webdriver-manager \
    cryptography \
    PySocks \
    stem
```

### 4. Setup Storage

```bash
termux-setup-storage
```

### 5. Create Directories

```bash
mkdir -p ~/social-reporter/{sessions,logs,encrypted_credentials,screenshots_errors}
```

---

## 🔒 Anonymity Setup for Termux

### Option 1: Tor (Maximum Anonymity)

#### Install Tor:

```bash
pkg install tor
```

#### Start Tor:

```bash
# Start in background
tor &

# Check if running
ps aux | grep tor
```

#### Verify Tor Connection:

```bash
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

You should see `"IsTor": true`

#### Stop Tor:

```bash
pkill tor
```

### Option 2: Proxy (High Anonymity)

#### Create Proxy File:

```bash
nano ~/proxies.txt
```

Add your proxies (one per line):
```
http://proxy1.com:8080
socks5://proxy2.com:1080
http://user:pass@proxy3.com:3128
```

Save: `Ctrl+X`, then `Y`, then `Enter`

#### Test Proxy:

The tool will automatically validate proxies on startup.

---

## ⚙️ Configuration for Termux

### Termux-Specific Settings

The tool automatically detects Termux and enables:
- ✅ Headless mode (no GUI)
- ✅ Mobile-optimized screen resolution (720x1280)
- ✅ Android user agent
- ✅ Optimized Chrome options

### config.json - Termux Section

Create or edit `~/social-reporter/termux_config.json`:

```json
{
    "termux": {
        "headless": true,
        "use_tor": true,
        "tor_port": 9050,
        "screen_resolution": "720x1280",
        "user_data_dir": "/data/data/com.termux/files/home/.cache/chromium",
        "disable_gpu": true,
        "no_sandbox": true,
        "disable_dev_shm": true
    }
}
```

---

## 🚀 Usage Examples

### Example 1: Maximum Anonymity (Tor)

```bash
# 1. Start Tor
tor &

# 2. Wait a few seconds
sleep 5

# 3. Run anonymous reporter
cd ~/INSTA-REPORT-main
python3 anonymous_reporter.py

# 4. Select anonymity level: 1 (MAXIMUM)
# 5. Tor will be detected automatically
```

### Example 2: High Anonymity (Proxy)

```bash
# 1. Make sure proxies.txt exists
nano ~/proxies.txt  # Add your proxies

# 2. Run anonymous reporter
cd ~/INSTA-REPORT-main
python3 anonymous_reporter.py

# 3. Select anonymity level: 2 (HIGH)
# 4. Proxies will be loaded and validated
```

### Example 3: Quick Start (Basic)

```bash
# Run without anonymity setup
cd ~/INSTA-REPORT-main
python3 multi_platform_reporter.py
```

---

## 🔧 Useful Aliases

Add to `~/.bashrc`:

```bash
# INSTA-REPORT aliases
alias reporter='cd ~/INSTA-REPORT-main && python3 anonymous_reporter.py'
alias quick-reporter='cd ~/INSTA-REPORT-main && python3 multi_platform_reporter.py'
alias start-tor='tor &'
alias stop-tor='pkill tor'
alias check-tor='curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip'
```

Reload:
```bash
source ~/.bashrc
```

---

## 📊 Performance Tips

### For Better Performance:

1. **Use WiFi** instead of mobile data
2. **Close other apps** to free memory
3. **Use proxy** instead of Tor (faster)
4. **Reduce report count** per session
5. **Increase delays** between reports
6. **Use headless mode** (always enabled on Termux)

### For Better Anonymity:

1. **Use Tor** (slower but more anonymous)
2. **Rotate proxies** frequently
3. **Enable fingerprint randomization**
4. **Encrypt credentials**
5. **Clear cookies/cache** after sessions
6. **Use different accounts** per platform

---

## 🐛 Troubleshooting

### Issue: Chrome/Chromium not found

**Solution:**
```bash
# ChromeDriver is downloaded automatically
# If issues, manually install:
pkg install chromium
```

### Issue: Tor connection failed

**Solution:**
```bash
# Check if Tor is running
ps aux | grep tor

# Start Tor
tor &

# Check logs
cat ~/.tor/logs/notice.log
```

### Issue: Permission denied

**Solution:**
```bash
# Grant storage permission
termux-setup-storage

# Make scripts executable
chmod +x *.sh
chmod +x *.py
```

### Issue: Import errors

**Solution:**
```bash
# Reinstall Python packages
pip install --upgrade --force-reinstall colorama requests selenium webdriver-manager cryptography PySocks stem
```

### Issue: Out of memory

**Solution:**
- Close other apps
- Reduce number of reports per session
- Use proxy instead of Tor
- Restart Termux

### Issue: Slow performance

**Solution:**
- Use WiFi instead of mobile data
- Reduce report count
- Increase delays between reports
- Use proxy instead of Tor
- Close background apps

---

## 🔒 Security Best Practices

### DO:
✅ Use Tor for maximum anonymity
✅ Use different accounts per platform
✅ Encrypt credentials
✅ Clear cookies/cache after sessions
✅ Use WiFi (more stable than mobile data)
✅ Keep Termux updated
✅ Use strong master password for encryption

### DON'T:
❌ Use your main accounts
❌ Share your proxies file
❌ Use without anonymity on public networks
❌ Store credentials in plain text
❌ Use for illegal activities
❌ Ignore warnings

---

## 📱 Termux-Specific Features

### Headless Mode
- Always enabled on Termux
- No GUI required
- Works perfectly on Android
- Lower resource usage

### Mobile Optimization
- Screen resolution: 720x1280
- Android user agent
- Optimized Chrome options
- Reduced memory usage

### Tor Integration
- Full Tor support
- Background Tor process
- Automatic connection check
- IP verification

### Proxy Support
- HTTP/HTTPS/SOCKS5
- Automatic rotation
- Validation before use
- Load from file or config

---

## 🔄 Updating

### Update Termux packages:

```bash
pkg update && pkg upgrade
```

### Update Python packages:

```bash
pip install --upgrade colorama requests selenium webdriver-manager cryptography PySocks stem
```

### Update code:

```bash
cd ~/INSTA-REPORT-main
git pull  # If using git
# Or re-download the code
```

---

## 📞 Support

### Common Issues:

1. **Tor not connecting**: Check if Tor is installed and running
2. **Import errors**: Reinstall Python packages
3. **Slow performance**: Use WiFi, close apps, use proxy instead of Tor
4. **Permission errors**: Run `termux-setup-storage`
5. **Chrome errors**: ChromeDriver is auto-downloaded, wait for it

### Getting Help:

1. Check logs in `~/INSTA-REPORT-main/logs/`
2. Review this guide
3. Check `ANONYMITY_GUIDE.md` for anonymity issues
4. Check `PLATFORMS_GUIDE.md` for platform-specific issues

---

## ⚠️ Important Notes

1. **Battery Usage**: High battery consumption expected
2. **Data Usage**: Can use significant mobile data
3. **Performance**: Slower than desktop/laptop
4. **Anonymity**: Works perfectly with Tor/Proxy
5. **Legal**: Same legal warnings apply on mobile
6. **Terms of Service**: Still violated on mobile
7. **Account Risk**: Accounts can still be banned

---

## 🎯 Quick Reference

```bash
# Start Tor
tor &

# Stop Tor
pkill tor

# Check Tor
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip

# Run with anonymity
cd ~/INSTA-REPORT-main && python3 anonymous_reporter.py

# Quick start
cd ~/INSTA-REPORT-main && python3 multi_platform_reporter.py

# Check requirements
python3 termux_reporter.py
```

---

## 📚 Additional Resources

- **Termux Wiki**: https://wiki.termux.com/
- **Tor Project**: https://www.torproject.org/
- **Termux Community**: https://github.com/termux/termux-app
- **ANONYMITY_GUIDE.md**: Complete anonymity guide
- **PLATFORMS_GUIDE.md**: Platform-specific guide

---

**Remember**: Use responsibly, legally, and ethically! 🛡️👻📱
