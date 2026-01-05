# 🌐 Multi-Platform Reporter - Complete Guide

## 📋 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run multi-platform reporter
python3 multi_platform_reporter.py
```

## 🎯 Supported Platforms Overview

| Platform | Emoji | Difficulty | Recommended Delay | Max Reports | Notes |
|----------|-------|------------|-------------------|-------------|-------|
| Instagram | 📸 | Easy | 30s | 10 | Most stable |
| TikTok | 🎵 | Easy | 45s | 10 | Good detection |
| Twitter/X | 🐦 | Medium | 35s | 8 | 2FA support |
| Facebook | 👥 | Medium | 40s | 8 | Checkpoint handling |
| YouTube | ▶️ | Hard | 50s | 5 | Google login |
| Reddit | 🤖 | Easy | 35s | 10 | Simple interface |
| LinkedIn | 💼 | Hard | 60s | 5 | Strictest detection |

## 🔧 Platform-Specific Setup

### Instagram (📸)
- **Login**: Username/Email + Password
- **Target Format**: `@username` or `username`
- **Report Types**: Fake Account, Adult Content, Hate Speech, Harassment, Violence, Spam
- **Notes**: Most reliable platform, good session persistence

### TikTok (🎵)
- **Login**: Username/Email/Phone + Password
- **Target Format**: `@username` or `username`
- **Report Types**: Fake Account, Inappropriate Content, Harassment, Violence, Spam, Hateful Behavior
- **Notes**: Requires longer delays, good anti-bot detection

### Twitter/X (🐦)
- **Login**: Username/Email/Phone + Password
- **Target Format**: `@username` or `username`
- **Report Types**: Spam, Abusive, Fake Account, Impersonation, Misleading Info, Hateful Content
- **Notes**: May require username verification, supports 2FA

### Facebook (👥)
- **Login**: Email/Phone + Password
- **Target Format**: `username` or profile name
- **Report Types**: Fake Account, Harassment, Hate Speech, Violence, Spam, Inappropriate Content
- **Notes**: May trigger security checkpoints, save login info popup

### YouTube (▶️)
- **Login**: Google Email + Password (Google Account)
- **Target Format**: `@channelname` or `channelname`
- **Report Types**: Spam/Misleading, Hateful Content, Harassment, Violent Content, Child Safety, Rights Infringement
- **Notes**: Uses Google login, requires longer delays, strictest

### Reddit (🤖)
- **Login**: Username + Password
- **Target Format**: `username` (without u/)
- **Report Types**: Spam, Harassment, Threatening Violence, Hate, Impersonation, Prohibited Content
- **Notes**: Simple interface, good success rate

### LinkedIn (💼)
- **Login**: Email + Password
- **Target Format**: `username` (from profile URL)
- **Report Types**: Fake Profile, Harassment, Inappropriate Content, Spam, Scam/Fraud, Hate Speech
- **Notes**: Most restrictive, may require security verification, professional network

## 🎮 Usage Examples

### Example 1: Single Platform (Instagram)
```bash
python3 multi_platform_reporter.py

# Select: 1 (Instagram)
# Enter credentials
# Enter target: targetuser
# Select country and reason
```

### Example 2: Multiple Platforms
```bash
python3 multi_platform_reporter.py

# Select: 1,3,6 (Instagram, Twitter, Reddit)
# Enter credentials (same for all or per-platform)
# Enter target: targetuser
# Select country
# Select reason for each platform
```

### Example 3: ALL Platforms
```bash
python3 multi_platform_reporter.py

# Select: 8 (ALL PLATFORMS)
# Enter credentials
# Enter target: targetuser
# Select country
# Select reasons for each platform
```

## ⚙️ Configuration Tips

### Optimal Settings per Platform

**Instagram:**
```json
{
    "default_delay": 30,
    "max_reports_per_session": 10,
    "headless": false
}
```

**TikTok:**
```json
{
    "default_delay": 45,
    "max_reports_per_session": 10,
    "headless": false
}
```

**Twitter/X:**
```json
{
    "default_delay": 35,
    "max_reports_per_session": 8,
    "headless": false
}
```

**Facebook:**
```json
{
    "default_delay": 40,
    "max_reports_per_session": 8,
    "headless": false
}
```

**YouTube:**
```json
{
    "default_delay": 50,
    "max_reports_per_session": 5,
    "headless": false
}
```

**Reddit:**
```json
{
    "default_delay": 35,
    "max_reports_per_session": 10,
    "headless": false
}
```

**LinkedIn:**
```json
{
    "default_delay": 60,
    "max_reports_per_session": 5,
    "headless": false
}
```

## 🛡️ Anti-Detection Best Practices

1. **Use Realistic Delays**: Don't go below minimum recommended delays
2. **Session Persistence**: Let the tool save sessions to reduce logins
3. **Different Accounts**: Use different accounts for different platforms
4. **Headless Mode**: Keep `headless: false` for better success rate
5. **Proxy Rotation**: Enable proxy for enhanced privacy (optional)
6. **User-Agent Rotation**: Tool automatically rotates user agents
7. **Human-like Behavior**: Tool includes random delays and human-like typing

## 📊 Expected Success Rates

| Platform | Success Rate | Notes |
|----------|--------------|-------|
| Instagram | 85-95% | Very reliable |
| TikTok | 80-90% | Good reliability |
| Twitter/X | 75-85% | May require verification |
| Facebook | 70-80% | Security checkpoints |
| YouTube | 60-75% | Google security |
| Reddit | 85-95% | Very reliable |
| LinkedIn | 50-70% | Strictest detection |

## 🚨 Troubleshooting

### Login Failed
- **Instagram/TikTok**: Check credentials, may need to verify via email/SMS
- **Twitter**: May require username verification
- **Facebook**: Security checkpoint - wait 15 seconds
- **YouTube**: Google 2FA - disable or use app password
- **LinkedIn**: Security verification - may need manual intervention

### Report Failed
- **All Platforms**: Increase delay in config.json
- **Selector Not Found**: Platform updated UI - selectors need update
- **Too Many Requests**: Reduce max_reports_per_session
- **Account Banned**: Use different account, increase delays

### Session Not Loading
- Delete `sessions/` folder and login fresh
- Check if cookies are enabled
- Try without headless mode

## 📝 Logs and Debugging

- **Logs**: Check `logs/` directory for detailed logs
- **Screenshots**: Check `screenshots_errors/` for error screenshots
- **Console Output**: Real-time colored output shows progress

## ⚠️ Legal and Ethical Considerations

1. **Educational Purpose Only**: This tool is for learning automation
2. **Terms of Service**: Using this violates all platform ToS
3. **Account Risks**: Your accounts WILL be banned if detected
4. **Legal Consequences**: Abuse may result in legal action
5. **Ethical Use**: DO NOT use for harassment or illegal activities
6. **Responsibility**: You accept FULL responsibility for your actions

## 🎓 Learning Objectives

This tool teaches:
- Web automation with Selenium
- Multi-platform integration
- Anti-detection techniques
- Session management
- Error handling and logging
- Browser automation best practices
- Social media platform architectures

## 🔄 Updates and Maintenance

Platforms frequently update their interfaces. If selectors stop working:

1. Check platform's current HTML structure
2. Update selectors in respective `platforms/*_reporter.py` files
3. Test with small number of reports first
4. Update config.json delays if needed

## 📞 Support

For issues:
1. Check logs in `logs/` directory
2. Check error screenshots in `screenshots_errors/`
3. Review this guide
4. Check if platform updated their interface
5. Increase delays and reduce report count

---

**Remember**: This tool is powerful but comes with serious risks. Use responsibly and only for educational purposes!
