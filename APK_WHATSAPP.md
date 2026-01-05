# 📱 APK per WhatsApp - Destinazione e Condivisione

## 🎯 DESTINAZIONE APK

### Dopo Build Locale (Linux/WSL):

**Percorso completo:**
```
~/dead-everything/bin/hackerreporter-2.0-arm64-v8a-debug.apk
```

**Su Windows (se usi WSL):**
```
C:\Users\TuoNome\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu*\LocalState\rootfs\home\TuoNome\dead-everything\bin\hackerreporter-2.0-arm64-v8a-debug.apk
```

**Oppure più semplice:**
- Apri WSL
- Esegui: `cd ~/dead-everything && ls -lh bin/*.apk`
- Copia il percorso mostrato

---

### Dopo Build GitHub Actions:

**Destinazione:**
1. Vai su: https://github.com/Adil-fayyaz/dead-everything/actions
2. Click sul workflow completato (verde ✅)
3. Scroll in basso → "Artifacts"
4. Click "hackerreporter-apk"
5. **Download ZIP** → Salva dove vuoi (es: Downloads)
6. **Estrai ZIP** → APK dentro!

**Percorso tipico dopo download:**
```
C:\Users\TuoNome\Downloads\hackerreporter-apk\hackerreporter-2.0-arm64-v8a-debug.apk
```

---

## 📤 COME CONDIVIDERE SU WHATSAPP

### Metodo 1: Da Telefono Android (Diretto)

**Step 1: Trasferisci APK sul Telefono**

**Opzione A: Email**
1. Invia APK come allegato email
2. Apri email sul telefono
3. Download APK

**Opzione B: Google Drive**
1. Upload APK su Google Drive
2. Apri Google Drive sul telefono
3. Download APK

**Opzione C: USB**
1. Collega telefono via USB
2. Copia APK nella cartella Download del telefono
3. Scollega USB

**Opzione D: Bluetooth**
1. Attiva Bluetooth su PC e telefono
2. Invia APK via Bluetooth
3. Accetta sul telefono

**Step 2: Condividi su WhatsApp**

1. Apri **File Manager** sul telefono
2. Vai in **Download** (o dove hai salvato l'APK)
3. **Tap lungo** sull'APK
4. Seleziona **"Condividi"** o **"Share"**
5. Scegli **WhatsApp**
6. Seleziona contatto o gruppo
7. **Invia** ✅

---

### Metodo 2: Da PC a WhatsApp Web

**Step 1: Trasferisci APK sul Telefono**

1. Invia APK via email/Drive/USB (come sopra)
2. Scarica APK sul telefono

**Step 2: Condividi da Telefono**

1. Apri WhatsApp sul telefono
2. Vai al contatto/gruppo
3. Click su **📎** (allegato)
4. Scegli **"Documento"** o **"File"**
5. Seleziona l'APK
6. **Invia** ✅

---

### Metodo 3: WhatsApp Desktop (Condividi Link)

**Se l'APK è su Google Drive:**

1. Upload APK su Google Drive
2. Click destro → **"Ottieni link"**
3. Copia link
4. Apri WhatsApp Desktop
5. Incolla link nel messaggio
6. **Invia** ✅

---

## 📍 PERCORSI RAPIDI

### Se APK è su PC (Windows):

```powershell
# Trova APK
Get-ChildItem -Path "C:\Users\$env:USERNAME\Downloads" -Filter "*.apk" -Recurse

# Oppure se in WSL:
wsl ls -lh ~/dead-everything/bin/*.apk
```

### Se APK è su Telefono:

```
/storage/emulated/0/Download/hackerreporter-2.0-arm64-v8a-debug.apk
```

---

## 🎯 PROCEDURA COMPLETA

### 1. Ottieni APK

**Da GitHub Actions:**
- Vai su: https://github.com/Adil-fayyaz/dead-everything/actions
- Download da Artifacts
- Estrai ZIP
- APK dentro!

**Da Build Locale:**
- Esegui: `./build_apk.sh`
- APK in: `bin/hackerreporter-2.0-arm64-v8a-debug.apk`

### 2. Trasferisci sul Telefono

**Metodo più veloce:**
1. Upload su Google Drive
2. Apri Drive sul telefono
3. Download APK

### 3. Condividi su WhatsApp

1. Apri **File Manager** sul telefono
2. Trova APK in **Download**
3. **Tap lungo** → **Condividi** → **WhatsApp**
4. Seleziona contatto/gruppo
5. **Invia** ✅

---

## 📋 CHECKLIST

Prima di condividere:

- [ ] APK compilato (GitHub Actions o locale)
- [ ] APK scaricato/trasferito sul telefono
- [ ] APK in cartella accessibile (Download)
- [ ] WhatsApp installato sul telefono
- [ ] Contatto/gruppo selezionato

---

## ⚠️ IMPORTANTE

1. **Dimensione APK**: ~50-100 MB
   - WhatsApp permette file fino a 100MB
   - Se più grande, usa Google Drive + link

2. **Formato**: Deve essere `.apk`
   - Non `.zip` (estrai prima!)

3. **Permessi**: 
   - Il destinatario deve abilitare "Installa da fonti sconosciute"

---

## 🚀 METODO PIÙ VELOCE

1. **GitHub Actions** → Download APK
2. **Google Drive** → Upload APK
3. **Telefono** → Download da Drive
4. **WhatsApp** → Condividi da File Manager

**Tempo totale**: 5-10 minuti (dopo che APK è pronto)

---

## 📱 ALTERNATIVA: Condividi Link GitHub

Se l'APK è troppo grande per WhatsApp:

1. Vai su: https://github.com/Adil-fayyaz/dead-everything/actions
2. Click sul workflow completato
3. Copia link della pagina
4. Condividi link su WhatsApp
5. Il destinatario scarica l'APK da GitHub

---

## ✅ RIEPILOGO

**Destinazione APK:**
- **GitHub**: Artifacts → Download ZIP → Estrai
- **Locale**: `bin/hackerreporter-2.0-arm64-v8a-debug.apk`

**Per WhatsApp:**
1. Trasferisci APK sul telefono (Drive/Email/USB)
2. Apri File Manager → Download
3. Tap lungo APK → Condividi → WhatsApp
4. Invia ✅

**L'APK è pronto per essere condiviso su WhatsApp!** 📱

---

**Created by Infinity X White devels team** 🔥
