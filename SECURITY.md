# Security Policy

## 🔒 Security Considerations

This tool is designed for **EDUCATIONAL and RESEARCH purposes ONLY**.

### ⚠️ Important Security Warnings

1. **Anonymity is NOT guaranteed** - Even with Tor/Proxy, you can be tracked
2. **Platforms detect automation** - Advanced anti-bot systems exist
3. **Accounts can be banned** - Use test accounts, NOT main accounts
4. **Legal consequences** - Misuse may result in legal action
5. **No 100% protection** - Perfect anonymity doesn't exist

## 🛡️ Anonymity Features

The tool includes multiple anonymity features:

- **Tor Network Support** - Routes traffic through Tor
- **Proxy Rotation** - Automatic proxy switching
- **Fingerprint Randomization** - Browser fingerprint spoofing
- **Encrypted Credentials** - AES-256 encryption
- **IP/DNS Leak Protection** - Prevents leaks
- **WebRTC Leak Protection** - Blocks WebRTC leaks

**However**, these features do NOT guarantee complete anonymity.

## 🔐 Credential Security

- Credentials are encrypted with AES-256
- Master password required for encryption
- Credentials never stored in plain text
- Session cookies stored securely

**Best Practices:**
- Use strong master password
- Don't share credentials files
- Use different accounts per platform
- Clear credentials after use

## 🚨 Reporting Security Vulnerabilities

If you discover a security vulnerability:

1. **DO NOT** open a public issue
2. Email maintainers privately with:
   - Description of vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)
3. Allow time for response before disclosure

## ⚠️ Security Warnings

### DO:
✅ Use Tor for maximum anonymity
✅ Use proxy rotation
✅ Encrypt credentials
✅ Use test accounts
✅ Clear cookies/cache after sessions
✅ Test for IP/DNS leaks
✅ Use different accounts per platform

### DON'T:
❌ Use your main accounts
❌ Store credentials in plain text
❌ Share proxy files
❌ Use without anonymity on public networks
❌ Trust 100% anonymity
❌ Use for illegal activities
❌ Ignore security warnings

## 📊 Anonymity Levels

| Level | Score | Protection |
|-------|-------|------------|
| MAXIMUM | 95/100 | Tor + Proxy + Full Fingerprint |
| HIGH | 75/100 | Proxy + Fingerprint |
| MEDIUM | 50/100 | Fingerprint Only |
| LOW | 30/100 | Basic Protection |
| NONE | 0/100 | No Protection (NOT RECOMMENDED) |

## 🔍 Security Testing

Before using:

1. **Test IP Leak:**
```bash
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip
```

2. **Test DNS Leak:**
```bash
# Check DNS queries
# Use tools like dnsleaktest.com
```

3. **Test WebRTC Leak:**
- Use browser extensions
- Check IP addresses
- Verify no leaks

## 📞 Security Support

For security-related questions:
- Check `ANONYMITY_GUIDE.md`
- Review security best practices
- Test your setup before use

---

**Remember**: Security is YOUR responsibility. Use at your own risk!
