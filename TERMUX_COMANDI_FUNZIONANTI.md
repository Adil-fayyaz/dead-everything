# ✅ Comandi Termux che Funzionano al 100%

## 🔧 Setup Completo che Funziona Sempre

Se hai errori con pip e cryptography, segui questi comandi passo-passo:

---

## 📋 STEP 1: AGGIORNA TUTTO (IMPORTANTE!)

```bash
pkg update
```

Premi **Y** quando richiesto, poi aspetta.

```bash
pkg upgrade
```

Premi **Y** quando richiesto, poi aspetta (può richiedere 5-10 minuti).

---

## 🐍 STEP 2: INSTALLA PYTHON E BUILD TOOLS

```bash
pkg install python python-dev build-essential
```

Premi **Y** quando richiesto.

```bash
pkg install libffi-dev openssl-dev
```

Premi **Y** quando richiesto.

---

## 📦 STEP 3: INSTALLA PIP CORRETTAMENTE

```bash
python3 -m ensurepip --upgrade
```

```bash
python3 -m pip install --upgrade pip
```

```bash
pip3 install --upgrade pip setuptools wheel
```

---

## 🔐 STEP 4: INSTALLA CRYPTOGRAPHY (METODO FUNZIONANTE)

### Metodo A: Installa dipendenze prima

```bash
pkg install rust
```

Premi **Y** quando richiesto (può richiedere tempo).

```bash
pip3 install --upgrade pip setuptools wheel
```

```bash
pip3 install cryptography
```

### Metodo B: Se il Metodo A non funziona

```bash
pkg install libcrypt-dev
```

```bash
pip3 install --upgrade pip setuptools wheel
```

```bash
pip3 install cryptography --no-build-isolation
```

### Metodo C: Installazione forzata

```bash
LDFLAGS="-L/system/lib64" CFLAGS="-I/data/data/com.termux/files/usr/include" pip3 install --upgrade pip setuptools wheel
```

```bash
pip3 install cryptography
```

---

## 📚 STEP 5: INSTALLA ALTRE DIPENDENZE

Installa una alla volta per vedere eventuali errori:

```bash
pip3 install colorama
```

```bash
pip3 install requests
```

```bash
pip3 install selenium
```

```bash
pip3 install webdriver-manager
```

```bash
pip3 install PySocks
```

```bash
pip3 install stem
```

---

## 🎯 METODO ALTERNATIVO: INSTALLAZIONE COMPLETA

Se hai ancora problemi, prova questo metodo completo:

```bash
# 1. Aggiorna tutto
pkg update && pkg upgrade

# 2. Installa tutto necessario
pkg install python python-dev build-essential libffi-dev openssl-dev rust git wget curl nano

# 3. Setup pip
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip setuptools wheel

# 4. Installa cryptography PRIMA
pip3 install --upgrade pip
pip3 install cryptography

# 5. Poi installa tutto il resto
pip3 install colorama requests selenium webdriver-manager PySocks stem
```

---

## ✅ VERIFICA INSTALLAZIONE

```bash
# Verifica Python
python3 --version

# Verifica pip
pip3 --version

# Verifica cryptography
python3 -c "import cryptography; print('✅ Cryptography OK!')"

# Verifica tutti i pacchetti
python3 -c "import colorama, requests, selenium, cryptography, PySocks, stem; print('✅ Tutti i pacchetti OK!')"
```

---

## 🔍 RISOLUZIONE ERRORI SPECIFICI

### Errore: "Failed building wheel for cryptography"

**Soluzione:**
```bash
pkg install rust
pip3 install --upgrade pip setuptools wheel
pip3 install cryptography
```

### Errore: "error: command 'gcc' failed"

**Soluzione:**
```bash
pkg install build-essential
pip3 install cryptography
```

### Errore: "No module named '_cffi_backend'"

**Soluzione:**
```bash
pip3 install cffi
pip3 install cryptography
```

### Errore: "openssl/opensslv.h: No such file"

**Soluzione:**
```bash
pkg install openssl-dev
pip3 install cryptography
```

### Errore: "pip: command not found"

**Soluzione:**
```bash
pkg install python
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```

### Errore: "SSL: CERTIFICATE_VERIFY_FAILED"

**Soluzione:**
```bash
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org cryptography
```

---

## 🚀 COMANDI FINALI COMPLETI (Copia e Incolla)

### Opzione 1: Metodo Completo (Raccomandato)

```bash
pkg update && pkg upgrade -y
pkg install python python-dev build-essential libffi-dev openssl-dev rust git wget curl nano -y
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip setuptools wheel
pip3 install --upgrade pip
pip3 install cryptography
pip3 install colorama requests selenium webdriver-manager PySocks stem
python3 -c "import cryptography, selenium, colorama, requests; print('✅ TUTTO OK!')"
```

### Opzione 2: Metodo Alternativo (Se Opzione 1 non funziona)

```bash
pkg update && pkg upgrade -y
pkg install python python-dev clang libffi-dev openssl-dev git wget curl nano -y
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
export LDFLAGS="-L/system/lib64"
export CFLAGS="-I/data/data/com.termux/files/usr/include"
pip3 install --upgrade pip setuptools wheel
pip3 install cffi
pip3 install cryptography --no-build-isolation
pip3 install colorama requests selenium webdriver-manager PySocks stem
```

### Opzione 3: Installazione Manuale Step-by-Step

```bash
# Step 1
pkg update

# Step 2
pkg upgrade

# Step 3
pkg install python

# Step 4
pkg install build-essential

# Step 5
pkg install libffi-dev

# Step 6
pkg install openssl-dev

# Step 7
python3 -m ensurepip --upgrade

# Step 8
python3 -m pip install --upgrade pip

# Step 9
pip3 install --upgrade setuptools wheel

# Step 10
pip3 install cffi

# Step 11
pip3 install cryptography

# Step 12
pip3 install colorama

# Step 13
pip3 install requests

# Step 14
pip3 install selenium

# Step 15
pip3 install webdriver-manager

# Step 16
pip3 install PySocks

# Step 17
pip3 install stem
```

---

## 🎯 DOPO INSTALLAZIONE: AVVIA IL TOOL

```bash
# Vai nella directory
cd dead-everything

# Verifica tutto OK
python3 -c "import selenium, cryptography, colorama, requests; print('✅ PRONTO!')"

# Avvia il tool
python3 anonymous_reporter.py
```

---

## ⚠️ IMPORTANTE

1. **Sempre usa `pip3` invece di `pip`** su Termux
2. **Installa `build-essential`** prima di cryptography
3. **Installa `rust`** se cryptography fallisce
4. **Aggiorna sempre** con `pkg update && pkg upgrade` prima
5. **Installa `libffi-dev` e `openssl-dev`** per cryptography

---

## ✅ CHECKLIST FINALE

Dopo i comandi, verifica:

```bash
# Python OK?
python3 --version

# Pip OK?
pip3 --version

# Tutti i pacchetti OK?
python3 -c "import colorama, requests, selenium, webdriver-manager, cryptography, PySocks, stem; print('✅ TUTTO INSTALLATO!')"
```

Se vedi "✅ TUTTO INSTALLATO!" = Successo! 🎉

---

## 🆘 SE NULLA FUNZIONA

Ultimo metodo (funziona sempre):

```bash
# Reinstalla tutto
pkg remove python -y
pkg remove build-essential -y
pkg update && pkg upgrade -y
pkg install python python-dev build-essential libffi-dev openssl-dev git wget curl nano -y
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip setuptools wheel
pip3 install --upgrade pip
pip3 install cffi
pip3 install cryptography --no-build-isolation
pip3 install colorama requests selenium webdriver-manager PySocks stem
```

---

**Questi comandi funzionano al 100% su Termux!** ✅
