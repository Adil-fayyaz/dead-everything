# 🐧 Guida Completa Termux - Prima Installazione

## 📱 Installazione su Termux per la Prima Volta

Questa guida ti aiuterà passo-passo a installare il tool su Termux (Android) dalla prima volta!

---

## 📋 PREREQUISITI

Prima di iniziare, assicurati di avere:

1. **Smartphone Android** (Android 7.0 o superiore)
2. **Connessione Internet** (WiFi consigliato)
3. **Termux App** - Scarica da:
   - **F-Droid** (consigliato): https://f-droid.org/packages/com.termux/
   - **GitHub Releases**: https://github.com/termux/termux-app/releases
4. **Circa 500MB di spazio libero**

---

## 🚀 STEP 1: INSTALLARE TERMUX

### Opzione A: Da F-Droid (Consigliato)

1. Vai su: https://f-droid.org/
2. Scarica l'APK di F-Droid
3. Installa F-Droid
4. Apri F-Droid
5. Cerca "Termux"
6. Clicca "Installa"
7. Aspetta il download e installazione

### Opzione B: Da GitHub

1. Vai su: https://github.com/termux/termux-app/releases
2. Scarica l'ultimo APK (termux-app_v*.apk)
3. Installa l'APK (abilita "Installa da fonti sconosciute" se richiesto)

---

## 🔧 STEP 2: PRIMA CONFIGURAZIONE TERMUX

Apri Termux e segui questi passaggi:

### 2.1 Aggiorna i Pacchetti

```bash
pkg update
```

Ti chiederà conferma: premi **Y** e poi **Enter**

```bash
pkg upgrade
```

Anche qui: premi **Y** e poi **Enter**

**Aspetta qualche minuto** per il completamento.

### 2.2 Installa Python

```bash
pkg install python
```

Premi **Y** quando richiesto.

### 2.3 Installa Altri Pacchetti Necessari

```bash
pkg install git wget curl nano vim
```

Premi **Y** quando richiesto.

### 2.4 Installa Tor (per Anonimato)

```bash
pkg install tor
```

Premi **Y** quando richiesto.

---

## 📦 STEP 3: INSTALLARE LE DIPENDENZE PYTHON

### 3.1 Aggiorna pip

```bash
pip install --upgrade pip
```

### 3.2 Installa le Librerie Necessarie

```bash
pip install colorama requests selenium webdriver-manager cryptography PySocks stem
```

**Nota**: Questo può richiedere alcuni minuti. Aspetta il completamento.

### 3.3 Verifica Installazione

```bash
python3 --version
```

Dovresti vedere: `Python 3.x.x`

```bash
pip list | grep selenium
```

Dovresti vedere `selenium` nella lista.

---

## 💾 STEP 4: CONFIGURA STORAGE

### 4.1 Concedi Permessi di Storage

```bash
termux-setup-storage
```

Ti apparirà una finestra di Android che chiede permessi. Clicca **"Consenti"** o **"Allow"**.

### 4.2 Verifica Storage

```bash
ls ~/storage
```

Dovresti vedere directory come `downloads`, `shared`, ecc.

---

## 📥 STEP 5: SCARICA IL CODICE

Hai 3 opzioni per ottenere il codice:

### Opzione A: Download da GitHub (Consigliato)

```bash
cd ~/storage/downloads
```

```bash
wget https://github.com/Adil-fayyaz/dead-everything/archive/refs/heads/main.zip
```

Se wget non funziona, usa curl:

```bash
curl -L -o INSTA-REPORT.zip https://github.com/Adil-fayyaz/dead-everything/archive/refs/heads/main.zip
```

```bash
unzip main.zip
```

o se hai scaricato INSTA-REPORT.zip:

```bash
unzip INSTA-REPORT.zip
```

```bash
cd dead-everything-main
```

### Opzione B: Clone con Git (Se disponibile)

```bash
cd ~/storage/downloads
```

```bash
git clone https://github.com/Adil-fayyaz/dead-everything.git
```

```bash
cd dead-everything
```

### Opzione C: Sposta File Manualmente

Se hai già scaricato i file sul telefono:

```bash
cd ~/storage/downloads
```

Trova la cartella del progetto e spostala:

```bash
mv INSTA-REPORT-main ~/
```

```bash
cd ~/INSTA-REPORT-main
```

---

## ⚙️ STEP 6: INSTALLAZIONE AUTOMATICA (Script Setup)

### 6.1 Rendi Eseguibile lo Script

```bash
chmod +x termux_setup.sh
```

### 6.2 Esegui lo Script di Setup

```bash
./termux_setup.sh
```

Oppure:

```bash
bash termux_setup.sh
```

**Lo script farà:**
- ✅ Verificare le installazioni
- ✅ Creare le directory necessarie
- ✅ Configurare l'ambiente
- ✅ Creare script di avvio rapido

---

## 🔍 STEP 7: VERIFICA INSTALLAZIONE

### 7.1 Verifica Python Packages

```bash
python3 -c "import colorama, requests, selenium, cryptography; print('✅ Tutti i pacchetti installati!')"
```

Se vedi "✅ Tutti i pacchetti installati!" = OK!

### 7.2 Verifica Struttura File

```bash
ls -la
```

Dovresti vedere:
- `anonymous_reporter.py`
- `multi_platform_reporter.py`
- `termux_reporter.py`
- `requirements.txt`
- `README.md`
- `platforms/` (directory)
- ecc.

### 7.3 Verifica Tor (Opzionale)

```bash
tor --version
```

Dovresti vedere la versione di Tor.

---

## 🔒 STEP 8: CONFIGURARE ANONIMATO (Opzionale ma Consigliato)

### 8.1 Avvia Tor in Background

```bash
tor &
```

### 8.2 Verifica Tor Funziona

```bash
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

Se funziona, vedrai un JSON con `"IsTor": true`

### 8.3 Ferma Tor (se necessario)

```bash
pkill tor
```

---

## 🚀 STEP 9: PRIMO UTILIZZO

### 9.1 Naviga nella Directory

```bash
cd ~/dead-everything-main
```

o

```bash
cd ~/dead-everything
```

(dipende da come hai scaricato)

### 9.2 Test Rapido

```bash
python3 --version
```

```bash
python3 -c "print('✅ Python funziona!')"
```

### 9.3 Avvia il Tool (Prima Volta)

**Opzione 1: Con Anonimato (Consigliato)**

```bash
# Prima avvia Tor
tor &

# Aspetta 3-5 secondi
sleep 5

# Poi avvia il tool
python3 anonymous_reporter.py
```

**Opzione 2: Senza Anonimato (Più Veloce)**

```bash
python3 multi_platform_reporter.py
```

**Opzione 3: Termux Optimized**

```bash
python3 termux_reporter.py
```

---

## ⚙️ STEP 10: CONFIGURAZIONE INIZIALE

Alla prima esecuzione:

1. **Leggi gli avvertimenti** - Premi **sì** o **y** se accetti
2. **Scegli livello anonimato**:
   - `1` = MAXIMUM (Tor + Proxy)
   - `2` = HIGH (Proxy)
   - `3` = MEDIUM (Fingerprint)
   - `4` = LOW (Base)
3. **Inserisci credenziali** (username e password)
4. **Scegli piattaforma** (Instagram, TikTok, ecc.)
5. **Inserisci target** (username da reportare)
6. **Scegli paese e motivo**

---

## 📝 STEP 11: CREARE SCRIPT DI AVVIO RAPIDO

### 11.1 Crea Script con Anonimato

```bash
nano ~/start_reporter.sh
```

Incolla questo:

```bash
#!/bin/bash
cd ~/dead-everything-main  # Modifica se la tua directory è diversa

# Avvia Tor in background se non è già avviato
if ! pgrep -x "tor" > /dev/null; then
    echo "🔒 Avvio Tor..."
    tor &
    sleep 5
fi

# Avvia il reporter
python3 anonymous_reporter.py
```

Salva: **Ctrl+X**, poi **Y**, poi **Enter**

### 11.2 Rendi Eseguibile

```bash
chmod +x ~/start_reporter.sh
```

### 11.3 Crea Script Quick (Senza Tor)

```bash
nano ~/quick_reporter.sh
```

Incolla:

```bash
#!/bin/bash
cd ~/dead-everything-main  # Modifica se la tua directory è diversa
python3 multi_platform_reporter.py
```

Salva: **Ctrl+X**, **Y**, **Enter**

```bash
chmod +x ~/quick_reporter.sh
```

### 11.4 Usa gli Script

```bash
~/start_reporter.sh
```

o

```bash
~/quick_reporter.sh
```

---

## 🔧 STEP 12: AGGIUNGERE ALIAS (Opzionale ma Utile)

### 12.1 Apri .bashrc

```bash
nano ~/.bashrc
```

### 12.2 Aggiungi alla Fine del File

Premi **Ctrl+V** per scorrere in fondo, poi incolla:

```bash
# INSTA-REPORT aliases
alias reporter='cd ~/dead-everything-main && python3 anonymous_reporter.py'
alias quick-reporter='cd ~/dead-everything-main && python3 multi_platform_reporter.py'
alias start-tor='tor &'
alias stop-tor='pkill tor'
alias check-tor='curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip'
```

**Importante**: Sostituisci `dead-everything-main` con il nome della tua directory se diverso!

Salva: **Ctrl+X**, **Y**, **Enter**

### 12.3 Ricarica .bashrc

```bash
source ~/.bashrc
```

### 12.4 Ora Puoi Usare i Comandi Brevi

```bash
reporter        # Avvia con anonimato
quick-reporter  # Avvia senza anonimato
start-tor       # Avvia Tor
stop-tor        # Ferma Tor
check-tor       # Verifica Tor
```

---

## 🎯 RIEPILOGO COMANDI COMPLETI (Copia e Incolla)

### Installazione Completa (Copia Tutto)

```bash
# 1. Aggiorna pacchetti
pkg update && pkg upgrade

# 2. Installa dipendenze
pkg install python git wget curl nano tor

# 3. Aggiorna pip
pip install --upgrade pip

# 4. Installa Python packages
pip install colorama requests selenium webdriver-manager cryptography PySocks stem

# 5. Setup storage
termux-setup-storage

# 6. Vai in downloads
cd ~/storage/downloads

# 7. Scarica il codice (scegli UNO dei metodi)
# Metodo A: wget
wget https://github.com/Adil-fayyaz/dead-everything/archive/refs/heads/main.zip
unzip main.zip
cd dead-everything-main

# OPPURE Metodo B: git clone
# git clone https://github.com/Adil-fayyaz/dead-everything.git
# cd dead-everything

# 8. Rendi eseguibile setup script
chmod +x termux_setup.sh

# 9. Esegui setup (opzionale ma consigliato)
./termux_setup.sh

# 10. Verifica installazione
python3 --version
python3 -c "import selenium; print('✅ OK!')"

# 11. Test Tor (opzionale)
tor &
sleep 5
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
pkill tor

# 12. Primo utilizzo
python3 anonymous_reporter.py
```

---

## ❓ TROUBLESHOOTING (Risoluzione Problemi)

### Problema: "pkg: command not found"

**Soluzione:**
```bash
apt update && apt upgrade
apt install python git wget curl nano
```

### Problema: "pip: command not found"

**Soluzione:**
```bash
pkg install python
python3 -m pip install --upgrade pip
```

### Problema: "Permission denied" su script

**Soluzione:**
```bash
chmod +x nome_script.sh
```

### Problema: "Storage permission denied"

**Soluzione:**
```bash
termux-setup-storage
```
Poi clicca "Consenti" nella finestra Android.

### Problema: "Module not found" (es. selenium)

**Soluzione:**
```bash
pip install selenium
# oppure per tutti
pip install -r requirements.txt
```

### Problema: "Tor connection failed"

**Soluzione:**
```bash
# Verifica se Tor è installato
pkg install tor

# Avvia Tor
tor &

# Aspetta 5 secondi
sleep 5

# Verifica
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

### Problema: "Out of memory"

**Soluzione:**
- Chiudi altre app
- Riavvia Termux
- Usa WiFi invece di dati mobili

### Problema: "Slow performance"

**Soluzione:**
- Usa WiFi
- Chiudi app in background
- Usa proxy invece di Tor (più veloce)

---

## 📚 COMANDI UTILI QUOTIDIANI

### Avviare il Tool

```bash
# Con anonimato (Tor)
cd ~/dead-everything-main
tor &
sleep 5
python3 anonymous_reporter.py

# Senza anonimato (veloce)
cd ~/dead-everything-main
python3 multi_platform_reporter.py

# Con script (dopo setup)
~/start_reporter.sh
```

### Gestire Tor

```bash
# Avvia Tor
tor &

# Verifica Tor
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip

# Ferma Tor
pkill tor
```

### Aggiornare

```bash
# Aggiorna pacchetti Termux
pkg update && pkg upgrade

# Aggiorna Python packages
pip install --upgrade colorama requests selenium webdriver-manager cryptography PySocks stem

# Aggiorna codice (se usi git)
cd ~/dead-everything-main
git pull
```

### Verifica Sistema

```bash
# Versione Python
python3 --version

# Pacchetti installati
pip list

# Spazio disco
df -h

# Processi attivi
ps aux
```

---

## 🎓 GUIDA PASSO-PASSO PRIMA ESECUZIONE

### 1. Apri Termux

Tocca l'icona Termux sul telefono.

### 2. Vai nella Directory del Tool

```bash
cd ~/dead-everything-main
```

(Oppure la directory dove hai estratto il codice)

### 3. Avvia Tor (Opzionale ma Consigliato)

```bash
tor &
```

Aspetta 3-5 secondi.

### 4. Avvia il Tool

```bash
python3 anonymous_reporter.py
```

### 5. Segui le Istruzioni sullo Schermo

1. Leggi gli avvertimenti
2. Scegli livello anonimato (consiglio: `2` per HIGH)
3. Inserisci username e password
4. Scegli piattaforma (es: `1` per Instagram)
5. Inserisci username target da reportare
6. Scegli paese
7. Scegli motivo del report
8. Attendi completamento

### 6. Vedi i Risultati

Il tool mostrerà:
- Progress dei report
- Report inviati con successo
- Report falliti
- Statistiche finali

---

## 📱 SUGGERIMENTI PER ANDROID

### Performance

- ✅ Usa **WiFi** invece di dati mobili (più veloce e stabile)
- ✅ Chiudi altre app prima di usare il tool
- ✅ Usa **headless mode** (sempre attivo su Termux)
- ✅ **Battery**: Aspettati alto consumo (normale per automazione)

### Anonimato

- ✅ **Tor**: Massimo anonimato ma più lento
- ✅ **Proxy**: Buon anonimato e più veloce
- ✅ **Fingerprint**: Sempre consigliato
- ✅ **WiFi pubblico**: Usa sempre anonimato

### Storage

- ✅ I log sono salvati in `logs/`
- ✅ Screenshot errori in `screenshots_errors/`
- ✅ Sessioni salvate in `sessions/`
- ✅ Credenziali cifrate in `encrypted_credentials/`

---

## ✅ CHECKLIST FINALE

Prima di usare il tool, verifica:

- [ ] Termux installato
- [ ] Python installato (`python3 --version`)
- [ ] Pacchetti Python installati (`pip list`)
- [ ] Storage configurato (`ls ~/storage`)
- [ ] Codice scaricato (`ls ~/dead-everything-main`)
- [ ] Tor installato (opzionale) (`tor --version`)
- [ ] Test funzionamento (`python3 -c "import selenium; print('OK')"`)

Se tutti i check sono OK, sei pronto! 🎉

---

## 🆘 AIUTO

### Hai Problemi?

1. **Leggi i log**: `cat ~/dead-everything-main/logs/*.log`
2. **Guarda screenshot errori**: `ls ~/dead-everything-main/screenshots_errors/`
3. **Verifica installazione**: `python3 -c "import selenium, colorama, requests; print('OK')"`
4. **Rileggi questa guida**
5. **Controlla README.md** per documentazione completa

### Comandi di Verifica Rapida

```bash
# Tutto ok?
python3 --version && \
pip list | grep selenium && \
ls ~/dead-everything-main && \
echo "✅ Installazione OK!"
```

---

## 🎉 PRONTO!

Ora hai tutto installato e configurato! Puoi iniziare a usare il tool!

**Ricorda:**
- ⚠️ Usa solo per scopi educativi
- ⚠️ Usa account di test, NON account principali
- ⚠️ Rispetta i delay minimi tra report
- ⚠️ Usa responsabilmente

**Buon utilizzo!** 🚀
