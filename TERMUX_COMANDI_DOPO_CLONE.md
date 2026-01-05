# 🚀 Comandi Dopo Git Clone - Termux

## ✅ Hai già fatto git clone? Ecco cosa fare!

Sei a buon punto! Ora segui questi passaggi:

---

## 📋 STEP 1: VAI NELLA DIRECTORY

```bash
cd dead-everything
```

**Nota**: Se hai clonato con un altro nome, usa quello. Verifica con:

```bash
ls
```

Dovresti vedere la cartella `dead-everything` o `INSTA-REPORT-main`

---

## 🔧 STEP 2: INSTALLA LE DIPENDENZE PYTHON

### 2.1 Aggiorna pip

```bash
pip install --upgrade pip
```

### 2.2 Installa i Pacchetti Necessari

```bash
pip install colorama requests selenium webdriver-manager cryptography PySocks stem
```

**Aspetta** che finisca (può richiedere 2-5 minuti).

---

## ⚙️ STEP 3: CONFIGURA STORAGE (Se non fatto)

```bash
termux-setup-storage
```

Clicca **"Consenti"** quando richiesto.

---

## 🔍 STEP 4: VERIFICA CHE TUTTO SIA OK

```bash
# Verifica Python
python3 --version

# Verifica pacchetti installati
python3 -c "import selenium, colorama, requests; print('✅ Tutto OK!')"
```

Se vedi "✅ Tutto OK!" = perfetto!

---

## 🔒 STEP 5: INSTALLA TOR (Opzionale ma Consigliato)

```bash
pkg install tor
```

Premi **Y** quando richiesto.

---

## 🚀 STEP 6: PRIMO UTILIZZO

### Opzione A: Con Anonimato (Consigliato)

```bash
# 1. Avvia Tor in background
tor &

# 2. Aspetta 5 secondi
sleep 5

# 3. Avvia il tool
python3 anonymous_reporter.py
```

### Opzione B: Senza Anonimato (Più Veloce)

```bash
python3 multi_platform_reporter.py
```

### Opzione C: Versione Termux Ottimizzata

```bash
python3 termux_reporter.py
```

---

## 📝 STEP 7: SEGUI LE ISTRUZIONI A SCHERMO

Quando avvii il tool:

1. **Leggi gli avvertimenti** - Premi **sì** o **y** se accetti
2. **Scegli livello anonimato**:
   - `1` = MAXIMUM (Tor + Proxy) - più anonimo ma lento
   - `2` = HIGH (Proxy) - buon equilibrio
   - `3` = MEDIUM (Fingerprint) - veloce
   - `4` = LOW - base
3. **Inserisci credenziali**:
   - Username/Email
   - Password
4. **Scegli piattaforma** (es: `1` per Instagram, `8` per tutte)
5. **Inserisci target** (username da reportare, senza @)
6. **Scegli paese**
7. **Scegli motivo del report**
8. **Attendi completamento**

---

## ✅ RIEPILOGO RAPIDO (Copia e Incolla)

```bash
# 1. Vai nella directory
cd dead-everything

# 2. Installa dipendenze
pip install --upgrade pip
pip install colorama requests selenium webdriver-manager cryptography PySocks stem

# 3. Setup storage (se necessario)
termux-setup-storage

# 4. Installa Tor (opzionale)
pkg install tor

# 5. Avvia Tor (se vuoi anonimato)
tor &
sleep 5

# 6. Avvia il tool
python3 anonymous_reporter.py
```

---

## 🎯 COMANDI UTILI RAPIDI

### Avviare il Tool

```bash
# Con anonimato
cd dead-everything
tor &
sleep 5
python3 anonymous_reporter.py

# Senza anonimato (veloce)
cd dead-everything
python3 multi_platform_reporter.py
```

### Gestire Tor

```bash
# Avvia Tor
tor &

# Verifica Tor funziona
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip

# Ferma Tor
pkill tor
```

### Verifiche

```bash
# Sei nella directory giusta?
pwd

# Vedi i file?
ls

# Python funziona?
python3 --version

# Pacchetti installati?
pip list | grep selenium
```

---

## ❓ PROBLEMI COMUNI

### "pip: command not found"

```bash
pkg install python
pip install --upgrade pip
```

### "Module not found" (es. selenium)

```bash
pip install selenium
# oppure tutti insieme
pip install colorama requests selenium webdriver-manager cryptography PySocks stem
```

### "Permission denied"

```bash
# Non serve chmod, i file sono già eseguibili
# Prova così:
python3 anonymous_reporter.py
```

### "Tor connection failed"

```bash
# Installa Tor
pkg install tor

# Avvia Tor
tor &

# Aspetta
sleep 5

# Verifica
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

---

## 🎉 PRONTO!

Ora puoi usare il tool! 

**Prossimi passi:**
1. Vai nella directory: `cd dead-everything`
2. Installa dipendenze: `pip install colorama requests selenium webdriver-manager cryptography PySocks stem`
3. Avvia: `python3 anonymous_reporter.py`

**Buon utilizzo!** 🚀
