# 📦 SCARICA APK ANDROID

## 🚀 METODO RAPIDO - GitHub Actions (AUTOMATICO)

L'APK viene compilato automaticamente su GitHub!

### Step 1: Vai su GitHub Actions

**Link diretto:**
https://github.com/Adil-fayyaz/dead-everything/actions

### Step 2: Trigger Build (se necessario)

1. Vai su: https://github.com/Adil-fayyaz/dead-everything/actions/workflows/build-apk.yml
2. Click su **"Run workflow"** (se disponibile)
3. Seleziona branch **"main"**
4. Click **"Run workflow"**

### Step 3: Aspetta Build (30-60 minuti)

1. Vai su: https://github.com/Adil-fayyaz/dead-everything/actions
2. Click sull'ultimo workflow **"Build Android APK"**
3. Aspetta che diventi **verde ✅** (può richiedere 30-60 minuti)

### Step 4: Download APK

1. Scroll in basso nella pagina del workflow
2. Trova sezione **"Artifacts"**
3. Click su **"hackerreporter-apk"**
4. Download ZIP
5. Estrai ZIP → Troverai l'APK dentro!

**APK sarà:**
- `hackerreporter-2.0-arm64-v8a-debug.apk` (telefoni moderni)
- `hackerreporter-2.0-armeabi-v7a-debug.apk` (telefoni vecchi)

---

## 📱 INSTALLAZIONE APK SU ANDROID

### Step 1: Trasferisci APK sul Telefono

- **Email**: Invia APK come allegato
- **WhatsApp/Telegram**: Invia come file
- **Google Drive**: Upload e scarica sul telefono
- **USB**: Copia APK sul telefono

### Step 2: Installa APK

1. Apri **File Manager** sul telefono
2. Trova il file APK
3. Tap sull'APK
4. Se richiesto, abilita **"Installa da fonti sconosciute"**
5. Click **"Installa"**
6. Click **"Apri"** quando installato

### Step 3: Permessi

L'app richiederà permessi:
- ✅ **Internet** (necessario)
- ✅ **Storage** (per salvare log)

---

## 🔧 SE GITHUB ACTIONS NON FUNZIONA

### Opzione 1: Build Locale (Linux/WSL)

```bash
# Su Linux o WSL
cd ~/dead-everything
chmod +x build_apk.sh
./build_apk.sh

# APK sarà in: bin/hackerreporter-2.0-arm64-v8a-debug.apk
```

### Opzione 2: Chiedi a Qualcuno con Linux

Condividi il repository e chiedi di eseguire:
```bash
./build_apk.sh
```

---

## ⚠️ IMPORTANTE

1. **Prima build**: Richiede 30-60 minuti
2. **Download**: 5-10 GB (Android SDK/NDK)
3. **Spazio**: 20GB+ necessario
4. **Android**: Minimo Android 5.0 (API 21)

---

## 📋 CHECKLIST

Prima di scaricare:

- [ ] GitHub Actions workflow completato (verde ✅)
- [ ] Artifacts disponibili
- [ ] APK scaricato
- [ ] APK trasferito sul telefono
- [ ] "Installa da fonti sconosciute" abilitato

---

## 🎯 LINK DIRETTI

- **GitHub Actions**: https://github.com/Adil-fayyaz/dead-everything/actions
- **Workflow Build**: https://github.com/Adil-fayyaz/dead-everything/actions/workflows/build-apk.yml
- **Repository**: https://github.com/Adil-fayyaz/dead-everything

---

## 🆘 PROBLEMI?

### APK non disponibile su GitHub?

1. Verifica che il workflow sia completato (verde ✅)
2. Controlla che non ci siano errori
3. Riprova a triggerare il workflow

### APK non si installa?

1. Abilita "Installa da fonti sconosciute"
2. Verifica Android 5.0+
3. Prova l'altro APK (arm64-v8a o armeabi-v7a)

---

**L'APK sarà disponibile su GitHub Actions dopo il build!** 🚀

---

**Created by Infinity X White devels team** 🔥
