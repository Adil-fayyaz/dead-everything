# 📱 Kivy App Installation Guide

## 🔥 Hacker-Style GUI App for Multi-Platform Reporter

This guide covers installation on **Kali Linux**, **Termux (Android)**, and building **Android APK**.

---

## 🖥️ DESKTOP INSTALLATION (Kali Linux / Ubuntu / Debian)

### Step 1: Install System Dependencies

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and build tools
sudo apt install -y python3 python3-pip python3-dev git

# Install Kivy dependencies
sudo apt install -y \
    build-essential \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    libgstreamer1.0-dev \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

# Install Chrome/Chromium for Selenium
sudo apt install -y chromium-browser
```

### Step 2: Clone Repository

```bash
cd ~
git clone https://github.com/Adil-fayyaz/dead-everything.git
cd dead-everything
```

### Step 3: Install Python Dependencies

```bash
# Upgrade pip
pip3 install --upgrade pip

# Install app requirements
pip3 install -r requirements_app.txt

# Or install manually
pip3 install kivy kivymd colorama requests selenium webdriver-manager cryptography PySocks stem pillow
```

### Step 4: Run the App

```bash
python3 app_main.py
```

---

## 📱 TERMUX INSTALLATION (Android)

### Step 1: Install Termux

Download from:
- **F-Droid**: https://f-droid.org/packages/com.termux/
- **GitHub**: https://github.com/termux/termux-app/releases

### Step 2: Setup Termux

```bash
# Update packages
pkg update && pkg upgrade -y

# Install dependencies
pkg install -y python python-dev git build-essential libffi-dev openssl-dev

# Install additional packages
pkg install -y mesa zlib libjpeg-turbo libpng sdl2 sdl2-image sdl2-mixer sdl2-ttf
```

### Step 3: Install Python Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install Cython (required for Kivy)
pip install Cython==0.29.36

# Install Kivy
pip install kivy

# Install other dependencies
pip install kivymd colorama requests selenium webdriver-manager cryptography PySocks stem pillow
```

### Step 4: Clone Repository

```bash
cd ~/storage/downloads
git clone https://github.com/Adil-fayyaz/dead-everything.git
cd dead-everything
```

### Step 5: Run the App

```bash
python app_main.py
```

**Note**: On Termux, the app runs in headless mode optimized for mobile.

---

## 📦 BUILD ANDROID APK

### Prerequisites

- **Linux** (Ubuntu/Debian recommended) or **WSL on Windows**
- **8GB+ RAM**
- **20GB+ free disk space**
- **Good internet connection**

### Step 1: Install Buildozer

```bash
# Install system dependencies
sudo apt update
sudo apt install -y \
    python3-pip \
    build-essential \
    git \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    libgstreamer1.0-dev \
    openjdk-11-jdk \
    unzip \
    zip \
    autoconf \
    libtool \
    pkg-config

# Install Buildozer
pip3 install --upgrade buildozer

# Install Cython
pip3 install --upgrade Cython==0.29.36
```

### Step 2: Prepare Project

```bash
cd ~/dead-everything

# Buildozer spec file is already included (buildozer.spec)
# You can customize it if needed
```

### Step 3: Build APK (Debug)

```bash
# Initialize buildozer (first time only)
buildozer init

# Build debug APK
buildozer -v android debug

# This will:
# - Download Android SDK/NDK
# - Download Python-for-Android
# - Compile all dependencies
# - Create APK file
#
# ⚠️  This can take 30-60 minutes on first build!
```

### Step 4: Build APK (Release)

```bash
# Build release APK (unsigned)
buildozer android release

# Sign APK (optional, for Play Store)
# You'll need to create a keystore first
```

### Step 5: Find APK

```bash
# APK location
ls -lh bin/

# You'll find:
# hackerreporter-2.0-arm64-v8a-debug.apk
# hackerreporter-2.0-armeabi-v7a-debug.apk
```

### Step 6: Install APK on Android

**Method A: USB**
```bash
# Enable USB debugging on Android
# Connect phone via USB

# Install APK
adb install bin/hackerreporter-2.0-arm64-v8a-debug.apk
```

**Method B: Transfer File**
- Copy APK to phone
- Open file manager
- Tap APK file
- Allow "Install from Unknown Sources"
- Install

---

## 🎯 QUICK START COMMANDS

### Kali Linux / Ubuntu

```bash
# Complete setup
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip git chromium-browser
git clone https://github.com/Adil-fayyaz/dead-everything.git
cd dead-everything
pip3 install -r requirements_app.txt
python3 app_main.py
```

### Termux

```bash
# Complete setup
pkg update && pkg upgrade -y
pkg install -y python git build-essential libffi-dev openssl-dev
pip install --upgrade pip
pip install kivy kivymd colorama requests selenium webdriver-manager cryptography PySocks stem
git clone https://github.com/Adil-fayyaz/dead-everything.git
cd dead-everything
python app_main.py
```

### Build APK

```bash
# On Linux
sudo apt install -y python3-pip build-essential git openjdk-11-jdk
pip3 install --upgrade buildozer Cython==0.29.36
cd ~/dead-everything
buildozer -v android debug
```

---

## 🔧 TROUBLESHOOTING

### Error: "Kivy not found"

```bash
pip3 install --upgrade kivy
```

### Error: "SDL2 not found" (Termux)

```bash
pkg install -y sdl2 sdl2-image sdl2-mixer sdl2-ttf
```

### Error: "Buildozer command not found"

```bash
pip3 install --upgrade buildozer
export PATH=$PATH:~/.local/bin
```

### Error: "Java not found" (Building APK)

```bash
sudo apt install -y openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### Error: "Out of memory" (Building APK)

- Close other applications
- Use a machine with more RAM
- Build on a cloud VM

### App crashes on Android

- Check Android version (minimum Android 5.0 / API 21)
- Check permissions (Internet, Storage)
- Check logs: `adb logcat | grep python`

---

## ⚙️ CUSTOMIZATION

### Change App Name

Edit `buildozer.spec`:
```ini
title = Your App Name
```

### Change Package Name

Edit `buildozer.spec`:
```ini
package.name = yourappname
package.domain = com.yourdomain
```

### Change App Icon

1. Create icon (512x512 PNG)
2. Save as `icon.png` in project root
3. Edit `buildozer.spec`:
```ini
icon.filename = %(source.dir)s/icon.png
```

### Change Splash Screen

1. Create splash (1280x720 PNG)
2. Save as `presplash.png` in project root
3. Edit `buildozer.spec`:
```ini
presplash.filename = %(source.dir)s/presplash.png
```

---

## 📊 APP FEATURES

### ✅ Working Features

- 🎯 Multi-platform selection (7 platforms)
- 🔐 Credential input with encryption
- 🛡️  Anonymity configuration
- 📊 Real-time progress tracking
- 📝 Live logging
- 📈 Statistics dashboard
- 🎨 Hacker-style dark theme
- 📱 Mobile-optimized UI

### 🔄 Integration with Backend

The app uses the existing Python scripts:
- `multi_platform_reporter.py`
- `anonymity_manager.py`
- Platform-specific reporters

All features from the CLI version work in the app!

---

## 🚀 PERFORMANCE

### Desktop (Kali Linux)
- Fast and responsive
- Full Selenium support
- All features available

### Termux (Android)
- Optimized for mobile
- Headless browser mode
- Lower resource usage

### Android APK
- Native Android app
- Installable without Termux
- Best user experience

---

## 📝 NOTES

1. **First build takes long** - Buildozer downloads SDK/NDK (5-10GB)
2. **Use WiFi** - Building requires good internet
3. **Selenium on Android** - Requires ChromeDriver (included)
4. **Permissions** - App needs Internet and Storage permissions
5. **Test accounts** - Always use test accounts, never main accounts

---

## 🆘 SUPPORT

### Check Logs

**Desktop:**
```bash
python3 app_main.py 2>&1 | tee app.log
```

**Termux:**
```bash
python app_main.py 2>&1 | tee app.log
```

**Android APK:**
```bash
adb logcat | grep python
```

### Common Issues

1. **Kivy not starting**: Install all SDL2 dependencies
2. **Selenium errors**: Install ChromeDriver
3. **Build fails**: Check Java and Android SDK
4. **App crashes**: Check permissions and logs

---

## ✅ CHECKLIST

Before running the app:

- [ ] Python 3.7+ installed
- [ ] Kivy installed (`pip3 list | grep kivy`)
- [ ] All dependencies installed
- [ ] Chrome/Chromium installed (for Selenium)
- [ ] Repository cloned
- [ ] In correct directory

Before building APK:

- [ ] Linux or WSL
- [ ] 8GB+ RAM
- [ ] 20GB+ free space
- [ ] Good internet
- [ ] Buildozer installed
- [ ] Java JDK installed
- [ ] buildozer.spec configured

---

## 🎉 READY!

Now you can:
1. Run the app on desktop: `python3 app_main.py`
2. Run on Termux: `python app_main.py`
3. Build APK: `buildozer android debug`
4. Install APK on Android

**Enjoy the hacker-style GUI!** 🔥👻

---

**Created by Infinity X White devels team** 🚀
