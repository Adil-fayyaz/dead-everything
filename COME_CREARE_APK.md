# 📦 Come Creare il File APK

## 🔍 Dove si Trova l'APK?

L'APK **non esiste ancora** - devi compilarlo prima!

Dopo la compilazione, si troverà in:
```
bin/hackerreporter-2.0-arm64-v8a-debug.apk
bin/hackerreporter-2.0-armeabi-v7a-debug.apk
```

---

## 🚀 COME CREARE L'APK

### ⚠️ IMPORTANTE: Serve Linux!

Per creare l'APK serve:
- **Linux** (Ubuntu/Debian) o **WSL su Windows**
- **8GB+ RAM**
- **20GB+ spazio libero**
- **Buona connessione internet**

---

## 📋 METODO 1: Su Linux (Ubuntu/Debian)

### Step 1: Installa Dipendenze

```bash
# Aggiorna sistema
sudo apt update && sudo apt upgrade -y

# Installa dipendenze base
sudo apt install -y \
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
    uuid-dev

# Installa Cython
pip3 install --upgrade Cython==0.29.36

# Installa Buildozer
pip3 install --upgrade buildozer

# Aggiungi al PATH (se necessario)
export PATH=$PATH:~/.local/bin
```

### Step 2: Clona Repository

```bash
cd ~
git clone https://github.com/Adil-fayyaz/dead-everything.git
cd dead-everything
```

### Step 3: Build APK

```bash
# Inizializza buildozer (prima volta)
buildozer init

# Build APK debug (può richiedere 30-60 minuti!)
buildozer -v android debug

# Questo farà:
# - Scaricare Android SDK/NDK (~5-10GB)
# - Scaricare Python-for-Android
# - Compilare tutte le dipendenze
# - Creare APK
```

### Step 4: Trova l'APK

```bash
# Lista file APK
ls -lh bin/*.apk

# Troverai:
# bin/hackerreporter-2.0-arm64-v8a-debug.apk
# bin/hackerreporter-2.0-armeabi-v7a-debug.apk

# Dimensione: ~50-100 MB per architettura
```

### Step 5: Invia l'APK

```bash
# Copia APK in Downloads
cp bin/hackerreporter-2.0-arm64-v8a-debug.apk ~/Downloads/

# Oppure trasferisci via USB/cloud
```

---

## 🪟 METODO 2: Su Windows (WSL)

### Step 1: Installa WSL

```powershell
# Apri PowerShell come Amministratore
wsl --install

# Riavvia computer
```

### Step 2: Apri WSL Ubuntu

```bash
# Dopo il riavvio, apri Ubuntu
# Segui i passi del METODO 1 dentro WSL
```

### Step 3: Accedi ai File Windows

```bash
# I file Windows sono in /mnt/c/
cd /mnt/c/Users/TuoNome/Downloads

# Oppure clona nel filesystem Linux (più veloce)
cd ~
git clone https://github.com/Adil-fayyaz/dead-everything.git
cd dead-everything
```

---

## 🌐 METODO 3: Cloud Build (Online)

### Opzione A: GitHub Actions (Automatico)

Creo un file per build automatico su GitHub Actions? Così l'APK viene compilato automaticamente!

### Opzione B: Servizi Cloud

Puoi usare:
- **Google Cloud Platform** (free tier)
- **AWS EC2** (free tier)
- **DigitalOcean** ($5/mese)
- **GitPod** (free tier)

---

## 📱 METODO 4: Chiedi a Qualcuno con Linux

Se non hai Linux, puoi:
1. Chiedere a qualcuno con Linux di compilare
2. Usare un servizio cloud
3. Usare una VM (VirtualBox/VMware)

---

## 🎯 QUICK BUILD (Copia e Incolla)

```bash
# Setup completo
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip build-essential git openjdk-11-jdk unzip wget curl zlib1g-dev libffi-dev
pip3 install --upgrade pip Cython==0.29.36 buildozer
export PATH=$PATH:~/.local/bin

# Clona e build
cd ~
git clone https://github.com/Adil-fayyaz/dead-everything.git
cd dead-everything
buildozer init
buildozer -v android debug

# APK sarà in bin/
ls -lh bin/*.apk
```

---

## 📦 DOPO LA COMPILAZIONE

### Trova l'APK:

```bash
cd ~/dead-everything
ls -lh bin/*.apk
```

### Copia l'APK:

```bash
# In Downloads
cp bin/hackerreporter-2.0-arm64-v8a-debug.apk ~/Downloads/

# O copia entrambi (per compatibilità)
cp bin/*.apk ~/Downloads/
```

### Invia l'APK:

1. **Email**: Allega APK (se < 25MB)
2. **WhatsApp/Telegram**: Invia come file
3. **Google Drive/Dropbox**: Condividi link
4. **USB**: Trasferisci fisicamente
5. **Cloud Storage**: Upload su qualsiasi servizio

---

## ⚠️ IMPORTANTE

### Quale APK Usare?

- **arm64-v8a**: Per telefoni moderni (2016+)
- **armeabi-v7a**: Per telefoni vecchi (2010-2016)
- **Entrambi**: Copia entrambi per compatibilità massima

### Primo Build

- ⏱️  **Tempo**: 30-60 minuti
- 📦 **Download**: 5-10 GB
- 💾 **Spazio**: 20GB+ necessario

### Build Successivi

- ⏱️  **Tempo**: 5-10 minuti (cache)
- 📦 **Download**: Minimo
- 💾 **Spazio**: Stesso

---

## 🔧 TROUBLESHOOTING

### Errore: "Buildozer not found"

```bash
pip3 install --upgrade buildozer
export PATH=$PATH:~/.local/bin
```

### Errore: "Java not found"

```bash
sudo apt install -y openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### Errore: "Out of memory"

- Chiudi altre applicazioni
- Usa una macchina con più RAM
- Aumenta swap: `sudo swapon --show`

### Build Lento

- Usa connessione internet veloce
- Primo build è sempre lento
- Build successivi sono più veloci (cache)

### APK Non Funziona su Android

1. Controlla architettura (arm64-v8a o armeabi-v7a)
2. Controlla Android version (minimo 5.0 / API 21)
3. Abilita "Installa da fonti sconosciute"
4. Controlla permessi (Internet, Storage)

---

## 📝 CHECKLIST

Prima di buildare:

- [ ] Linux o WSL installato
- [ ] 8GB+ RAM disponibile
- [ ] 20GB+ spazio libero
- [ ] Buona connessione internet
- [ ] Buildozer installato (`buildozer --version`)
- [ ] Java JDK installato (`java --version`)
- [ ] Repository clonato
- [ ] In directory corretta

---

## 🎯 RIEPILOGO RAPIDO

1. **Hai Linux?** → Vai a METODO 1
2. **Hai Windows?** → Installa WSL → Vai a METODO 1
3. **Non hai nulla?** → Usa cloud o chiedi a qualcuno

**Comando finale:**
```bash
buildozer -v android debug
```

**APK sarà in:**
```
bin/hackerreporter-2.0-arm64-v8a-debug.apk
```

---

## 🚀 PRONTO!

Dopo il build, l'APK sarà in `bin/` e potrai inviarlo al tuo amico!

**Buon build!** 🔥

---

**Created by Infinity X White devels team** 🚀
