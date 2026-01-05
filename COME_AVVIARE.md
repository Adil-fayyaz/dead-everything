# 🚀 Come Avviare l'Interfaccia di Report

## ✅ Guida Completa per Avviare il Tool

Se l'interfaccia non si avvia, segui questa guida!

---

## 🎯 METODO 1: Script di Avvio Semplice (Raccomandato)

### Usa lo script `start.py`:

```bash
cd dead-everything
python3 start.py
```

**Lo script:**
- ✅ Verifica che tutte le dipendenze siano installate
- ✅ Mostra un menu per scegliere quale script avviare
- ✅ Avvia automaticamente l'interfaccia corretta

---

## 📋 METODO 2: Avviare Direttamente gli Script

### Opzione A: Reporter Multi-Piattaforma (Consigliato)

```bash
cd dead-everything
python3 multi_platform_reporter.py
```

**Supporta:**
- Instagram
- TikTok
- Twitter/X
- Facebook
- YouTube
- Reddit
- LinkedIn

---

### Opzione B: Con Anonimato

```bash
cd dead-everything
python3 anonymous_reporter.py
```

**Caratteristiche:**
- ✅ Multi-piattaforma
- ✅ Tor support
- ✅ Proxy rotation
- ✅ Fingerprint randomization

---

### Opzione C: Reporter Originale (Solo Instagram)

```bash
cd dead-everything
python3 insta-report.py
```

**Supporta solo Instagram**

---

### Opzione D: Advanced Reporter (Instagram + TikTok)

```bash
cd dead-everything
python3 advanced_reporter.py
```

**Supporta Instagram e TikTok**

---

### Opzione E: Termux Optimized

```bash
cd dead-everything
python3 termux_reporter.py
```

**Ottimizzato per Termux/Android**

---

## 🔍 VERIFICA DIPENDENZE PRIMA DI AVVIARE

### Verifica che tutto sia installato:

```bash
python3 -c "import colorama, requests, selenium, cryptography; print('✅ OK!')"
```

### Se vedi errori, installa le dipendenze:

```bash
pip3 install colorama requests selenium webdriver-manager cryptography PySocks stem
```

---

## ❓ PROBLEMI COMUNI E SOLUZIONI

### Errore: "No module named 'colorama'"

**Soluzione:**
```bash
pip3 install colorama requests selenium webdriver-manager cryptography PySocks stem
```

---

### Errore: "No module named 'selenium'"

**Soluzione:**
```bash
pip3 install selenium webdriver-manager
```

---

### Errore: "No module named 'cryptography'"

**Soluzione:**
```bash
# Su Termux
pkg install build-essential libffi-dev openssl-dev rust
pip3 install cryptography

# Su Linux/Windows
pip3 install cryptography
```

---

### Errore: "chromedriver not found"

**Soluzione:**
Il webdriver-manager dovrebbe installarlo automaticamente. Se non funziona:

```bash
pip3 install --upgrade webdriver-manager
```

---

### Errore: "Permission denied"

**Soluzione:**
```bash
# Su Termux/Linux
chmod +x start.py
python3 start.py

# Oppure
python3 multi_platform_reporter.py
```

---

### Errore: "config.json not found"

**Soluzione:**
Il file `config.json` dovrebbe essere nella directory. Verifica:

```bash
ls -la config.json
```

Se non c'è, clona di nuovo il repository:

```bash
git clone https://github.com/Adil-fayyaz/dead-everything.git
cd dead-everything
```

---

### Errore: "Import error" o "Module not found"

**Soluzione completa:**
```bash
# 1. Vai nella directory
cd dead-everything

# 2. Installa tutte le dipendenze
pip3 install --upgrade pip
pip3 install colorama requests selenium webdriver-manager cryptography PySocks stem

# 3. Verifica
python3 -c "import colorama, requests, selenium, cryptography; print('✅ OK!')"

# 4. Avvia
python3 multi_platform_reporter.py
```

---

## 🎯 COMANDI RAPIDI (Copia e Incolla)

### Setup Completo + Avvio

```bash
# 1. Vai nella directory
cd dead-everything

# 2. Installa dipendenze (se necessario)
pip3 install colorama requests selenium webdriver-manager cryptography PySocks stem

# 3. Verifica installazione
python3 -c "import colorama, requests, selenium, cryptography; print('✅ OK!')"

# 4. Avvia con script di avvio
python3 start.py

# OPPURE avvia direttamente
python3 multi_platform_reporter.py
```

---

## 📱 SU TERMUX (Android)

```bash
# 1. Vai nella directory
cd dead-everything

# 2. Installa dipendenze
pip3 install colorama requests selenium webdriver-manager cryptography PySocks stem

# 3. Avvia
python3 termux_reporter.py

# OPPURE
python3 multi_platform_reporter.py

# OPPURE con anonimato
tor &
sleep 5
python3 anonymous_reporter.py
```

---

## ✅ CHECKLIST PRIMA DI AVVIARE

Prima di avviare, verifica:

- [ ] Sei nella directory corretta (`cd dead-everything`)
- [ ] Python installato (`python3 --version`)
- [ ] Dipendenze installate (`pip3 list | grep selenium`)
- [ ] File config.json presente (`ls config.json`)
- [ ] Script Python presente (`ls *.py`)

---

## 🚀 COSA FARE QUANDO SI AVVIA

Quando avvii il tool:

1. **Leggi gli avvertimenti** - Premi **sì** o **y** se accetti
2. **Scegli piattaforma** (se richiesto)
3. **Scegli livello anonimato** (se richiesto):
   - `1` = MAXIMUM (Tor + Proxy)
   - `2` = HIGH (Proxy)
   - `3` = MEDIUM (Fingerprint)
   - `4` = LOW (Base)
4. **Inserisci credenziali**:
   - Username/Email
   - Password
5. **Inserisci target** (username da reportare, senza @)
6. **Scegli paese**
7. **Scegli motivo del report**
8. **Attendi completamento**

---

## 📝 ESEMPIO DI AVVIO CORRETTO

```bash
$ cd dead-everything
$ python3 multi_platform_reporter.py

🔥 INSTA-REPORT - Multi-Platform Reporter
==========================================

⚠️  WARNING: This tool automates reporting on social media platforms...
Do you understand and accept the risks? (yes/no): yes

🌐 Select platforms:
1. Instagram
2. TikTok
...
8. All platforms

👉 Select (1-8): 1

🔐 Enter your credentials:
📧 Username/Email: tuousername
🔒 Password: ********

🎯 Enter target username to report:
@targetuser

...
```

---

## 🆘 SE NULLA FUNZIONA

### 1. Verifica Python

```bash
python3 --version
```

Deve essere Python 3.7+

### 2. Reinstalla Dipendenze

```bash
pip3 uninstall colorama requests selenium webdriver-manager cryptography PySocks stem -y
pip3 install colorama requests selenium webdriver-manager cryptography PySocks stem
```

### 3. Verifica File

```bash
ls -la *.py
ls -la config.json
ls -la platforms/
```

### 4. Prova Script Direttamente

```bash
python3 -c "print('Python funziona!')"
python3 -c "import colorama; print('Colorama OK!')"
python3 -c "import selenium; print('Selenium OK!')"
```

### 5. Controlla Errori Specifici

```bash
python3 multi_platform_reporter.py 2>&1 | head -50
```

Questo mostra i primi 50 errori se ce ne sono.

---

## ✅ SOLUZIONE RAPIDA FINALE

Se hai ancora problemi, usa questo comando completo:

```bash
cd dead-everything && \
pip3 install --upgrade pip && \
pip3 install colorama requests selenium webdriver-manager cryptography PySocks stem && \
python3 -c "import colorama, requests, selenium, cryptography; print('✅ OK!')" && \
python3 multi_platform_reporter.py
```

---

**Ora dovresti riuscire ad avviare l'interfaccia!** 🎉

Se hai ancora problemi, dimmi quale errore vedi esattamente!
