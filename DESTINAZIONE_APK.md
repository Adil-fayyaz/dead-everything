# 📦 Destinazione APK - Dove Trovare il File

## 🎯 DESTINAZIONE APK

Dopo il build, l'APK si trova in:

```
bin/hackerreporter-2.0-arm64-v8a-debug.apk
bin/hackerreporter-2.0-armeabi-v7a-debug.apk
```

**Percorso completo:**
- **Linux/WSL**: `~/dead-everything/bin/hackerreporter-2.0-arm64-v8a-debug.apk`
- **Windows**: `C:\Users\TuoNome\dead-everything\bin\hackerreporter-2.0-arm64-v8a-debug.apk`

---

## 🚀 COME CREARE L'APK

### Metodo 1: Script Automatico (Raccomandato)

#### Su Linux:

```bash
cd ~/dead-everything
chmod +x build_apk.sh
./build_apk.sh
```

#### Su Windows (WSL):

```cmd
# Doppio click su: build_apk_wsl.bat
# OPPURE
build_apk_wsl.bat
```

### Metodo 2: GitHub Actions (Automatico)

L'APK viene compilato automaticamente quando pushi su GitHub!

1. **Push su GitHub:**
```bash
git push origin main
```

2. **Vai su GitHub:**
   - Repository: https://github.com/Adil-fayyaz/dead-everything
   - Tab "Actions"
   - Click sull'ultimo workflow
   - Download APK da "Artifacts"

3. **Destinazione GitHub:**
   - Tab "Actions" → Ultimo workflow → "Artifacts" → Download

### Metodo 3: Manuale

```bash
# Setup
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip build-essential git openjdk-11-jdk
pip3 install Cython==0.29.36 buildozer

# Build
cd ~/dead-everything
buildozer init
buildozer -v android debug

# APK sarà in: bin/
```

---

## 📍 DOVE SI TROVA L'APK

### Dopo Build Locale:

```
~/dead-everything/
└── bin/
    ├── hackerreporter-2.0-arm64-v8a-debug.apk    ← TELEFONI MODERNI
    └── hackerreporter-2.0-armeabi-v7a-debug.apk ← TELEFONI VECCHI
```

### Dopo Build GitHub Actions:

1. Vai su: https://github.com/Adil-fayyaz/dead-everything/actions
2. Click sull'ultimo workflow (verde ✅)
3. Scroll in basso → "Artifacts"
4. Click "hackerreporter-apk"
5. Download ZIP con APK dentro

---

## 📤 COME INVIARE L'APK

### Copia in Downloads:

```bash
cp bin/hackerreporter-2.0-arm64-v8a-debug.apk ~/Downloads/
```

### Invia via:

- ✅ **WhatsApp/Telegram**: Invia come file
- ✅ **Email**: Allega APK (se < 25MB)
- ✅ **Google Drive**: Upload e condividi link
- ✅ **Dropbox**: Upload e condividi link
- ✅ **USB**: Copia fisicamente

---

## 🎯 QUALE APK USARE?

- **arm64-v8a**: Telefoni moderni (2016+)
  - Samsung Galaxy S7+, iPhone 6s+, ecc.
  - **Usa questo per la maggior parte dei telefoni!**

- **armeabi-v7a**: Telefoni vecchi (2010-2016)
  - Samsung Galaxy S3-S6, ecc.
  - Solo se arm64-v8a non funziona

**Consiglio**: Invia **entrambi** per compatibilità massima!

---

## ✅ VERIFICA APK

```bash
# Lista APK
ls -lh bin/*.apk

# Dimensione dovrebbe essere ~50-100 MB
# Se è molto piccolo (< 10MB), il build è fallito!
```

---

## 🔧 TROUBLESHOOTING

### APK non trovato?

```bash
# Verifica directory
pwd
ls -la bin/

# Se bin/ non esiste, il build non è completato
```

### Build fallito?

```bash
# Controlla log
cat .buildozer/android/platform/build/build.log

# Riprova
buildozer clean
buildozer -v android debug
```

### APK non si installa su Android?

1. Abilita "Installa da fonti sconosciute"
2. Verifica architettura (arm64-v8a o armeabi-v7a)
3. Verifica Android version (minimo 5.0 / API 21)
4. Controlla permessi (Internet, Storage)

---

## 📋 CHECKLIST

Prima di cercare l'APK:

- [ ] Build completato senza errori
- [ ] Directory `bin/` esiste
- [ ] File `.apk` presente in `bin/`
- [ ] Dimensione APK ~50-100 MB
- [ ] Nome file: `hackerreporter-2.0-*-debug.apk`

---

## 🎉 RIEPILOGO

**Destinazione APK:**
```
bin/hackerreporter-2.0-arm64-v8a-debug.apk
```

**Percorso completo:**
- Linux: `~/dead-everything/bin/`
- Windows: `C:\Users\TuoNome\dead-everything\bin\`
- GitHub: Actions → Artifacts → Download

**Dopo il build, l'APK è pronto per essere inviato!** 🚀

---

**Created by Infinity X White devels team** 🔥
