# 🛡️ Complete Anonymity Guide - Anonymous Reporter

## ⚠️ CRITICAL DISCLAIMER

**ANONYMITY DOES NOT GUARANTEE 100% PROTECTION!**

Even with all anonymity features enabled:
- You can still be tracked by sophisticated systems
- Platforms have advanced anti-bot detection
- Your accounts can be linked to your identity
- Legal authorities can request data from providers
- Anonymity does NOT protect you from the law

**USE ONLY FOR LEGAL, EDUCATIONAL PURPOSES!**

---

## 🎯 Anonymity Levels

### Level 1: 👻 MAXIMUM (Recommended)
- **Tor Network** - Routes traffic through Tor
- **Proxy Rotation** - Changes proxy every N reports
- **Full Fingerprint Randomization** - Complete browser fingerprint spoofing
- **Encrypted Credentials** - Stores credentials encrypted
- **WebRTC Leak Protection** - Prevents WebRTC IP leaks
- **DNS Leak Protection** - Prevents DNS leaks
- **Canvas Fingerprinting Protection** - Blocks canvas fingerprinting

**Protection Level: 95/100**

### Level 2: 🛡️ HIGH
- **Proxy Rotation** - Multiple proxies
- **Fingerprint Randomization** - Browser fingerprint spoofing
- **Encrypted Credentials** - Secure storage
- **IP Leak Protection** - Basic IP protection

**Protection Level: 75/100**

### Level 3: 🔐 MEDIUM
- **Fingerprint Randomization** - Basic fingerprint spoofing
- **Encrypted Credentials** - Secure storage
- **User-Agent Rotation** - Random user agents

**Protection Level: 50/100**

### Level 4: ⚠️ LOW
- **Basic Fingerprint** - Minimal protection
- **User-Agent Rotation** - Random user agents only

**Protection Level: 30/100**

### Level 5: 🚫 NONE (NOT RECOMMENDED)
- **No Protection** - Your real IP and identity exposed

**Protection Level: 0/100**

---

## 🔧 Setup Instructions

### 1. Install Tor (For Maximum Anonymity)

#### Windows:
```bash
# Download Tor Browser from https://www.torproject.org/download/
# Install and run Tor Browser
# Tor will run on port 9050 by default
```

#### Linux:
```bash
sudo apt update
sudo apt install tor
sudo systemctl start tor
sudo systemctl enable tor

# Verify Tor is running
sudo systemctl status tor
```

#### Mac:
```bash
brew install tor
brew services start tor
```

### 2. Configure Proxies

#### Option A: Add to config.json
```json
{
    "anonymity": {
        "proxy_list": [
            "http://proxy1.example.com:8080",
            "socks5://proxy2.example.com:1080",
            "http://username:password@proxy3.example.com:3128"
        ]
    }
}
```

#### Option B: Create proxies.txt
```
http://proxy1.example.com:8080
socks5://proxy2.example.com:1080
http://username:password@proxy3.example.com:3128
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Basic Usage
```bash
python3 anonymous_reporter.py
```

### Step-by-Step:

1. **Select Anonymity Level**
   - Choose from 1-5 based on your needs
   - Maximum (1) recommended for best protection

2. **Tor Setup** (if Maximum selected)
   - Tool checks if Tor is running
   - If not, you'll be prompted to install/start Tor
   - Fallback to proxy if Tor unavailable

3. **Proxy Configuration** (if HIGH/MAXIMUM)
   - Tool validates proxies automatically
   - Invalid proxies are skipped
   - Best proxy is selected automatically

4. **Anonymity Status**
   - Tool shows your anonymity status
   - Current IP address
   - Tor/Proxy status
   - Anonymity score (0-100)

5. **Continue with Reporting**
   - Proceed with normal platform selection
   - All traffic routed through Tor/Proxy
   - Fingerprint randomized automatically

---

## 🔐 Features Explained

### Tor Network
- Routes all traffic through Tor network
- Changes IP address automatically
- Provides strong anonymity
- Slower than direct connection

**How to verify:**
```bash
# Check your Tor IP
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

### Proxy Rotation
- Automatically changes proxy every N reports
- Validates proxies before use
- Skips dead proxies
- Supports HTTP, HTTPS, SOCKS5

**Proxy Format:**
```
http://proxy.com:8080
https://proxy.com:443
socks5://proxy.com:1080
http://user:pass@proxy.com:8080
```

### Fingerprint Randomization
Randomizes:
- User-Agent
- Screen Resolution
- Color Depth
- Timezone
- Language
- Platform
- Hardware Concurrency
- Device Memory
- Canvas Fingerprint
- WebGL Vendor/Renderer

### Encrypted Credentials
- Stores credentials encrypted with AES-256
- Requires master password
- Credentials never stored in plain text
- Protected from file access

### WebRTC Leak Protection
- Prevents WebRTC from leaking real IP
- Disables WebRTC entirely (optional)
- Blocks non-proxied UDP

### DNS Leak Protection
- Routes DNS through Tor/Proxy
- Prevents DNS queries from leaking
- Uses secure DNS servers

---

## 📊 Anonymity Score Calculation

| Feature | Points |
|---------|--------|
| Tor Active | +40 |
| Proxy Active | +30 |
| Fingerprint Randomization | +20 |
| Encrypted Credentials | +10 |
| No IP Leak | +10 |
| **Maximum** | **100** |

---

## 🛠️ Advanced Configuration

### config.json - Anonymity Section

```json
{
    "anonymity": {
        "enable_tor": false,
        "tor_port": 9050,
        "enable_proxy_rotation": false,
        "proxy_list": [],
        "proxy_validation": true,
        "proxy_rotation_interval": 3,
        "enable_fingerprint_randomization": true,
        "enable_webrtc_leak_protection": true,
        "enable_dns_leak_protection": true,
        "enable_canvas_fingerprinting_protection": true,
        "encrypt_credentials": false,
        "master_password_required": false,
        "clear_cookies_on_exit": true,
        "clear_cache_on_exit": true,
        "use_private_mode": true,
        "disable_webgl": false,
        "randomize_screen_resolution": true,
        "randomize_timezone": true,
        "randomize_language": true,
        "enable_ip_leak_check": true,
        "enable_dns_leak_check": true,
        "anonymity_level": "high"
    }
}
```

### Options Explained:

- `enable_tor`: Use Tor network
- `tor_port`: Tor SOCKS port (default 9050)
- `enable_proxy_rotation`: Rotate proxies automatically
- `proxy_validation`: Validate proxies before use
- `proxy_rotation_interval`: Change proxy every N reports
- `enable_fingerprint_randomization`: Randomize browser fingerprint
- `enable_webrtc_leak_protection`: Prevent WebRTC leaks
- `enable_dns_leak_protection`: Prevent DNS leaks
- `encrypt_credentials`: Encrypt stored credentials
- `clear_cookies_on_exit`: Clear cookies after session
- `clear_cache_on_exit`: Clear cache after session

---

## 🔍 Leak Testing

### Check IP Leak
```python
from anonymity_manager import AnonymityManager

anon = AnonymityManager()
no_leak, ip = anon.check_ip_leak()
print(f"IP: {ip}, No Leak: {no_leak}")
```

### Check DNS Leak
```python
anon.check_dns_leak()
```

### Get Anonymity Score
```python
score = anon.get_anonymity_score()
print(f"Anonymity Score: {score}/100")
```

---

## 🚨 Security Best Practices

### DO:
✅ Use Tor for maximum anonymity
✅ Rotate proxies frequently
✅ Use encrypted credentials
✅ Clear cookies/cache after each session
✅ Use different accounts for different platforms
✅ Test for IP/DNS leaks before reporting
✅ Use VPN + Tor for extra protection (optional)
✅ Keep software updated

### DON'T:
❌ Use your main accounts
❌ Use free/public proxies (often logged)
❌ Reuse the same proxy for multiple sessions
❌ Login to personal accounts during session
❌ Use for illegal activities
❌ Trust 100% anonymity
❌ Ignore warnings and errors
❌ Use without understanding risks

---

## 🔗 Recommended Services

### Tor
- **Official**: https://www.torproject.org/
- **Free**: Yes
- **Anonymity**: Excellent
- **Speed**: Slow

### Paid Proxy Services
- **Bright Data** (formerly Luminati)
- **Smartproxy**
- **Oxylabs**
- **IPRoyal**

### VPN Services (Extra Layer)
- **Mullvad** - Anonymous, no logs
- **ProtonVPN** - Privacy-focused
- **IVPN** - No logs policy

---

## 🐛 Troubleshooting

### Tor Not Connecting
```bash
# Check if Tor is running
sudo systemctl status tor  # Linux
# or check Tor Browser is open (Windows/Mac)

# Restart Tor
sudo systemctl restart tor  # Linux
```

### Proxy Not Working
- Check proxy format is correct
- Verify proxy is not dead
- Try different proxy
- Check firewall settings

### IP Leak Detected
- Restart Tor/Proxy
- Clear browser cache
- Check WebRTC is disabled
- Use different proxy

### Low Anonymity Score
- Enable Tor
- Add more proxies
- Enable all protection features
- Check for leaks

---

## 📈 Performance Impact

| Feature | Speed Impact | Anonymity Gain |
|---------|--------------|----------------|
| Tor | -70% | +40 points |
| Proxy | -30% | +30 points |
| Fingerprint | -5% | +20 points |
| Encryption | -2% | +10 points |

**Trade-off**: More anonymity = Slower performance

---

## ⚖️ Legal Considerations

1. **Anonymity ≠ Legal Immunity**
   - Laws still apply
   - Authorities can investigate
   - Providers can be subpoenaed

2. **Use Cases**
   - Educational research
   - Security testing (authorized)
   - Privacy protection (legal)

3. **Prohibited Uses**
   - Harassment
   - Cyberbullying
   - Illegal activities
   - Terms of Service violations

4. **Consequences**
   - Account bans
   - Legal action
   - Criminal charges (if illegal)

---

## 📞 Support

For anonymity issues:
1. Check Tor is running
2. Validate proxies
3. Test for leaks
4. Review logs in `logs/` directory
5. Check anonymity score

---

**Remember**: Perfect anonymity doesn't exist. Use responsibly and legally!

**Stay Safe, Stay Anonymous, Stay Legal!** 🛡️👻🔒
