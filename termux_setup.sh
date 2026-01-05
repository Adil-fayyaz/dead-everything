#!/bin/bash

# INSTA-REPORT Multi-Platform Reporter - Termux Setup Script
# For Android devices with Termux

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  🐧 INSTA-REPORT TERMUX SETUP - Android Installation 🐧    ║"
echo "║  🛡️  With Full Anonymity Support 🛡️                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if running on Termux
if [ ! -d "$PREFIX" ]; then
    echo -e "${RED}❌ Error: This script must be run in Termux!${NC}"
    exit 1
fi

echo -e "${CYAN}✅ Termux detected! Starting installation...${NC}"
echo ""

# Update packages
echo -e "${YELLOW}📦 Updating packages...${NC}"
pkg update -y && pkg upgrade -y

# Install required packages
echo -e "${YELLOW}📦 Installing required packages...${NC}"
pkg install -y \
    python \
    git \
    wget \
    curl \
    proot \
    openssl \
    openssh \
    termux-api \
    tor \
    nano \
    vim

# Install Python packages
echo -e "${YELLOW}🐍 Installing Python packages...${NC}"
pip install --upgrade pip

pip install \
    colorama \
    requests \
    selenium \
    webdriver-manager \
    cryptography \
    PySocks \
    stem

# Install Chrome/Chromium for Android
echo -e "${YELLOW}🌐 Installing Chromium for Android...${NC}"

# Try to install via pkg (if available in termux)
if pkg install -y chromium 2>/dev/null; then
    echo -e "${GREEN}✅ Chromium installed via pkg${NC}"
else
    echo -e "${YELLOW}⚠️  Chromium not available via pkg${NC}"
    echo -e "${CYAN}💡 Using headless Chrome via webdriver-manager${NC}"
    echo -e "${CYAN}💡 ChromeDriver will be downloaded automatically${NC}"
fi

# Setup storage permissions
echo -e "${YELLOW}📁 Setting up storage permissions...${NC}"
if [ ! -d ~/storage ]; then
    termux-setup-storage
    echo -e "${GREEN}✅ Storage permissions granted${NC}"
else
    echo -e "${GREEN}✅ Storage already configured${NC}"
fi

# Create directories
echo -e "${YELLOW}📁 Creating directories...${NC}"
mkdir -p ~/social-reporter/{sessions,logs,encrypted_credentials,screenshots_errors}

# Check if already cloned
if [ -d "INSTA-REPORT-main" ]; then
    echo -e "${YELLOW}⚠️  INSTA-REPORT-main already exists${NC}"
    read -p "Update existing installation? (y/n): " update
    if [ "$update" = "y" ]; then
        cd INSTA-REPORT-main
        git pull 2>/dev/null || echo -e "${YELLOW}⚠️  Not a git repo, skipping pull${NC}"
        cd ..
    fi
else
    echo -e "${CYAN}📥 If you have the code, place it in INSTA-REPORT-main/${NC}"
    echo -e "${CYAN}📥 Or clone from GitHub (if repository is public)${NC}"
fi

# Setup Tor
echo -e "${YELLOW}🔒 Setting up Tor...${NC}"
if command -v tor &> /dev/null; then
    echo -e "${GREEN}✅ Tor is installed${NC}"
    echo -e "${CYAN}💡 To start Tor: tor${NC}"
    echo -e "${CYAN}💡 To run in background: tor &${NC}"
else
    echo -e "${RED}❌ Tor installation failed${NC}"
    echo -e "${YELLOW}💡 Install manually: pkg install tor${NC}"
fi

# Create termux-specific config
echo -e "${YELLOW}⚙️  Creating Termux configuration...${NC}"
cat > ~/social-reporter/termux_config.json << 'EOF'
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
EOF

echo -e "${GREEN}✅ Termux config created${NC}"

# Create startup script
echo -e "${YELLOW}📝 Creating startup script...${NC}"
cat > ~/start_reporter.sh << 'EOF'
#!/bin/bash

cd ~/INSTA-REPORT-main || cd ~/social-reporter

# Start Tor in background if not running
if ! pgrep -x "tor" > /dev/null; then
    echo "🔒 Starting Tor..."
    tor &
    sleep 3
fi

# Run the reporter
python3 anonymous_reporter.py "$@"
EOF

chmod +x ~/start_reporter.sh

echo -e "${GREEN}✅ Startup script created: ~/start_reporter.sh${NC}"

# Create quick start script
cat > ~/quick_reporter.sh << 'EOF'
#!/bin/bash

cd ~/INSTA-REPORT-main || cd ~/social-reporter

# Quick start without Tor (faster but less anonymous)
python3 multi_platform_reporter.py "$@"
EOF

chmod +x ~/quick_reporter.sh

echo -e "${GREEN}✅ Quick start script created: ~/quick_reporter.sh${NC}"

# Setup aliases
echo -e "${YELLOW}📝 Setting up aliases...${NC}"
if ! grep -q "alias reporter=" ~/.bashrc 2>/dev/null; then
    echo "" >> ~/.bashrc
    echo "# INSTA-REPORT aliases" >> ~/.bashrc
    echo "alias reporter='~/start_reporter.sh'" >> ~/.bashrc
    echo "alias quick-reporter='~/quick_reporter.sh'" >> ~/.bashrc
    echo "alias start-tor='tor &'" >> ~/.bashrc
    echo "alias stop-tor='pkill tor'" >> ~/.bashrc
    echo -e "${GREEN}✅ Aliases added to ~/.bashrc${NC}"
    echo -e "${CYAN}💡 Run: source ~/.bashrc to reload${NC}"
else
    echo -e "${YELLOW}⚠️  Aliases already exist${NC}"
fi

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  ✅ INSTALLATION COMPLETE! ✅                              ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}📋 Next Steps:${NC}"
echo -e "${CYAN}1. Navigate to the code directory:${NC}"
echo -e "   ${YELLOW}cd ~/INSTA-REPORT-main${NC}"
echo ""
echo -e "${CYAN}2. Start Tor (for anonymity):${NC}"
echo -e "   ${YELLOW}tor &${NC}"
echo ""
echo -e "${CYAN}3. Run the reporter:${NC}"
echo -e "   ${YELLOW}python3 anonymous_reporter.py${NC}"
echo -e "   ${YELLOW}or: reporter${NC} (after reloading bashrc)"
echo ""
echo -e "${CYAN}4. Quick start (without Tor):${NC}"
echo -e "   ${YELLOW}python3 multi_platform_reporter.py${NC}"
echo -e "   ${YELLOW}or: quick-reporter${NC}"
echo ""
echo -e "${YELLOW}⚠️  Important Notes:${NC}"
echo -e "${YELLOW}- Use headless mode (enabled by default)${NC}"
echo -e "${YELLOW}- Tor is recommended for anonymity${NC}"
echo -e "${YELLOW}- Make sure ChromeDriver is compatible with Android${NC}"
echo ""
echo -e "${GREEN}🎉 Setup complete! Happy reporting!${NC}"
