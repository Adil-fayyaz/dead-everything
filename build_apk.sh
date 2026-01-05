#!/bin/bash
# 🔥 Script Automatico per Build APK 🔥
# Created by Infinity X White devels team

set -e  # Exit on error

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🔥 BUILD APK AUTOMATICO - HACKER REPORTER 🔥            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo -e "${RED}❌ ERRORE: Questo script richiede Linux!${NC}"
    echo -e "${YELLOW}💡 Su Windows, usa WSL: wsl --install${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Sistema operativo: Linux${NC}"
echo ""

# Check if in correct directory
if [ ! -f "buildozer.spec" ]; then
    echo -e "${RED}❌ ERRORE: buildozer.spec non trovato!${NC}"
    echo -e "${YELLOW}💡 Assicurati di essere nella directory dead-everything${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Directory corretta${NC}"
echo ""

# Step 1: Update system
echo -e "${YELLOW}📦 Step 1: Aggiornamento sistema...${NC}"
sudo apt-get update -qq
sudo apt-get upgrade -y -qq

# Step 2: Install dependencies
echo -e "${YELLOW}📦 Step 2: Installazione dipendenze sistema...${NC}"
sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    unzip \
    wget \
    curl \
    openjdk-11-jdk \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libdb5.3-dev \
    libbz2-dev \
    libexpat1-dev \
    liblzma-dev \
    libffi-dev \
    uuid-dev \
    libssl-dev \
    > /dev/null 2>&1

echo -e "${GREEN}✅ Dipendenze installate${NC}"

# Step 3: Install Python packages
echo -e "${YELLOW}📦 Step 3: Installazione Python packages...${NC}"
pip3 install --upgrade pip --quiet
pip3 install Cython==0.29.36 --quiet
pip3 install buildozer --quiet

echo -e "${GREEN}✅ Python packages installati${NC}"

# Step 4: Setup Buildozer
echo -e "${YELLOW}📦 Step 4: Setup Buildozer...${NC}"
buildozer init || true

# Step 5: Build APK
echo ""
echo -e "${YELLOW}🔥 Step 5: BUILD APK IN CORSO...${NC}"
echo -e "${YELLOW}⏱️  Questo richiede 30-60 minuti...${NC}"
echo ""

# Add to PATH
export PATH=$PATH:~/.local/bin

# Build
buildozer -v android debug

# Step 6: Check results
echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  ✅ BUILD COMPLETATO!                                      ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ -f "bin/hackerreporter-2.0-arm64-v8a-debug.apk" ]; then
    echo -e "${GREEN}✅ APK creato con successo!${NC}"
    echo ""
    echo -e "${YELLOW}📦 File APK:${NC}"
    ls -lh bin/*.apk
    echo ""
    echo -e "${GREEN}📍 DESTINAZIONE APK:${NC}"
    echo -e "${GREEN}   $(pwd)/bin/hackerreporter-2.0-arm64-v8a-debug.apk${NC}"
    if [ -f "bin/hackerreporter-2.0-armeabi-v7a-debug.apk" ]; then
        echo -e "${GREEN}   $(pwd)/bin/hackerreporter-2.0-armeabi-v7a-debug.apk${NC}"
    fi
    echo ""
    echo -e "${YELLOW}📤 Per copiare in Downloads:${NC}"
    echo -e "${YELLOW}   cp bin/*.apk ~/Downloads/${NC}"
else
    echo -e "${RED}❌ ERRORE: APK non trovato!${NC}"
    echo -e "${YELLOW}💡 Controlla i log per errori${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}🎉 APK pronto per essere inviato!${NC}"
echo ""
