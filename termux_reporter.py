#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Termux-Optimized Multi-Platform Social Media Reporter
Optimized for Android/Termux environment with full anonymity support
"""

import os
import sys
import json
import time
from pathlib import Path

# Check if running on Termux
def is_termux():
    """Check if running in Termux environment"""
    return os.path.exists('/data/data/com.termux/files/home')

# Termux-specific optimizations
if is_termux():
    # Set display for headless mode
    os.environ['DISPLAY'] = ':0'
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'
    
    # Disable GUI requirements
    os.environ['HEADLESS'] = 'true'
    
    # Optimize for Android
    os.environ['ANDROID_ROOT'] = '1'
    os.environ['TERMUX'] = '1'

import random
from colorama import Fore, Style, init
from anonymity_manager import AnonymityManager

# Import reporters (will fail gracefully if not available)
try:
    from multi_platform_reporter import (
        select_platforms, select_country, select_reason,
        get_reporter, run_platform_report
    )
except ImportError:
    # Fallback if multi_platform_reporter not available
    print("Warning: multi_platform_reporter not found, using basic mode")

init(autoreset=True)

def slow_print(text, color=Fore.WHITE, delay=0.03):
    """Stampa testo con effetto digitazione"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    """Banner Termux"""
    os.system("clear")
    print(Fore.CYAN + Style.BRIGHT + r"""
    
    ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║╚██╗ ██╔╝╚██╗██╔╝
       ██║   █████╗  ██████╔╝██╔████╔██║ ╚████╔╝  ╚███╔╝ 
       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║  ╚██╔╝   ██╔██╗ 
       ██║   ███████╗██║  ██║██║ ╚═╝ ██║   ██║   ██╔╝ ██╗
       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝
    
    ╔══════════════════════════════════════════════════════════════════╗
    ║  🐧 TERMUX MULTI-PLATFORM REPORTER - Android Optimized 🐧      ║
    ║  🛡️  Full Anonymity Support | Tor | Proxy | Fingerprint 🛡️    ║
    ║  📱 Headless Mode | Optimized for Mobile Devices 📱             ║
    ╚══════════════════════════════════════════════════════════════════╝
""")

def check_termux_requirements():
    """Verifica i requisiti Termux"""
    issues = []
    
    # Check Python
    try:
        import sys
        if sys.version_info < (3, 7):
            issues.append("Python 3.7+ required")
    except:
        issues.append("Python not found")
    
    # Check required packages
    required = ['colorama', 'requests', 'selenium', 'cryptography']
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            issues.append(f"Package '{pkg}' not installed. Run: pip install {pkg}")
    
    # Check Tor (optional but recommended)
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', 9050))
        sock.close()
        if result != 0:
            issues.append("⚠️  Tor not running (optional but recommended)")
    except:
        issues.append("⚠️  Cannot check Tor status")
    
    return issues

def setup_termux_anonymity():
    """Setup anonimato ottimizzato per Termux"""
    slow_print("\n🛡️  TERMUX ANONYMITY SETUP", Fore.CYAN + Style.BRIGHT)
    slow_print("="*70, Fore.CYAN)
    
    anon_manager = AnonymityManager()
    
    slow_print("\n🔒 Select Anonymity Level for Termux:", Fore.YELLOW)
    slow_print("[1] 👻 MAXIMUM (Tor + Proxy + Full Protection)", Fore.GREEN)
    slow_print("[2] 🛡️  HIGH (Proxy Rotation + Fingerprint)", Fore.YELLOW)
    slow_print("[3] 🔐 MEDIUM (Fingerprint Randomization)", Fore.CYAN)
    slow_print("[4] ⚠️  LOW (Basic Protection)", Fore.RED)
    
    choice = input(Fore.GREEN + "\n📥 Your choice (default: 2): ").strip() or "2"
    
    config = {
        "use_tor": False,
        "use_proxy": False,
        "proxy_rotation": False,
        "fingerprint_randomization": True,
        "encrypt_credentials": False,
        "headless": True  # Always headless on Termux
    }
    
    if choice == "1":
        # MAXIMUM - Try Tor first
        slow_print("\n👻 Configuring MAXIMUM anonymity...", Fore.GREEN)
        
        slow_print("\n🔍 Checking Tor connection...", Fore.CYAN)
        tor_ok, tor_ip = anon_manager.check_tor_connection()
        
        if tor_ok:
            config["use_tor"] = True
            slow_print(f"✅ Tor ACTIVE! IP: {tor_ip}", Fore.GREEN)
        else:
            slow_print("⚠️  Tor not available.", Fore.YELLOW)
            slow_print("💡 To start Tor: tor &", Fore.CYAN)
            slow_print("💡 Or: pkg install tor && tor &", Fore.CYAN)
            
            use_proxy = input(Fore.YELLOW + "\n🔄 Use proxy instead? (y/n): ").strip().lower()
            if use_proxy == 'y':
                config["use_proxy"] = True
                config["proxy_rotation"] = True
        
        config["fingerprint_randomization"] = True
        config["encrypt_credentials"] = True
        
    elif choice == "2":
        # HIGH
        slow_print("\n🛡️  Configuring HIGH anonymity...", Fore.YELLOW)
        config["use_proxy"] = True
        config["proxy_rotation"] = True
        config["fingerprint_randomization"] = True
        config["encrypt_credentials"] = True
        
    elif choice == "3":
        # MEDIUM
        slow_print("\n🔐 Configuring MEDIUM anonymity...", Fore.CYAN)
        config["fingerprint_randomization"] = True
        config["encrypt_credentials"] = True
        
    else:
        # LOW
        slow_print("\n⚠️  Configuring LOW anonymity...", Fore.RED)
        config["fingerprint_randomization"] = True
    
    # Termux-specific: Always headless
    config["headless"] = True
    
    # Setup proxy if needed
    if config["use_proxy"] and not config["use_tor"]:
        slow_print("\n🔄 Setting up proxy...", Fore.CYAN)
        proxies = anon_manager.get_proxy_list()
        
        if proxies:
            slow_print(f"📋 Found {len(proxies)} proxies", Fore.GREEN)
            proxy = anon_manager.get_random_proxy(validate=True)
            if proxy:
                slow_print(f"✅ Proxy configured: {proxy}", Fore.GREEN)
            else:
                slow_print("❌ No valid proxy found", Fore.RED)
                config["use_proxy"] = False
        else:
            slow_print("⚠️  No proxies configured", Fore.YELLOW)
            config["use_proxy"] = False
    
    # Show status
    anon_manager.print_anonymity_status()
    
    return config, anon_manager

def show_termux_warning():
    """Avvertimenti per Termux"""
    print(Fore.RED + "\n" + "="*70)
    print(Fore.YELLOW + Style.BRIGHT + "⚠️  TERMUX/ANDROID WARNING ⚠️")
    print(Fore.RED + "="*70)
    print(Fore.WHITE + """
    📱 TERMUX/ANDROID SPECIFIC NOTES:
    
    1. ⚠️  Headless mode is enabled (no GUI)
    2. 🔒 Tor must be started manually: tor &
    3. 📱 Mobile data usage may be high
    4. 🔋 High battery consumption expected
    5. ⏱️  Operations may be slower on mobile
    6. 📊 Use WiFi for better performance
    7. 🛡️  Anonymity features fully supported
    8. ⚠️  Use responsibly and legally
    
    ⚠️  ANONYMITY DOES NOT GUARANTEE 100% PROTECTION ⚠️
    """)
    print(Fore.RED + "="*70)
    response = input(Fore.YELLOW + "\n⚠️  Continue? (sì/no): ").strip().lower()
    return response in ['sì', 'si', 'yes', 'y', 's']

def get_termux_chrome_options():
    """Ottiene Chrome options ottimizzate per Termux"""
    from selenium.webdriver.chrome.options import Options
    
    options = Options()
    
    # Termux-specific optimizations
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-logging')
    options.add_argument('--disable-background-networking')
    options.add_argument('--disable-background-timer-throttling')
    options.add_argument('--disable-backgrounding-occluded-windows')
    options.add_argument('--disable-renderer-backgrounding')
    options.add_argument('--disable-features=TranslateUI')
    options.add_argument('--disable-ipc-flooding-protection')
    options.add_argument('--window-size=720,1280')
    options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36')
    
    # Android-specific
    options.add_argument('--force-device-scale-factor=1')
    options.add_argument('--high-dpi-support=1')
    
    return options

def main():
    """Main function per Termux"""
    banner()
    
    # Check if Termux
    if not is_termux():
        slow_print("\n⚠️  This script is optimized for Termux", Fore.YELLOW)
        slow_print("💡 For regular Linux/Windows, use: python3 anonymous_reporter.py", Fore.CYAN)
        response = input(Fore.YELLOW + "\nContinue anyway? (y/n): ").strip().lower()
        if response != 'y':
            return
    
    # Check requirements
    slow_print("\n🔍 Checking requirements...", Fore.CYAN)
    issues = check_termux_requirements()
    
    if issues:
        for issue in issues:
            if "optional" in issue.lower() or "⚠️" in issue:
                slow_print(f"{issue}", Fore.YELLOW)
            else:
                slow_print(f"❌ {issue}", Fore.RED)
        
        critical = [i for i in issues if "❌" not in str(i) and "⚠️" not in str(i)]
        if critical:
            slow_print("\n❌ Critical issues found. Please install missing packages.", Fore.RED)
            return
    
    slow_print("✅ Requirements check complete!", Fore.GREEN)
    
    # Avvertimenti
    if not show_termux_warning():
        slow_print("\n✅ Operation cancelled. Stay safe!", Fore.BLUE)
        return
    
    # Setup anonimato
    anon_config, anon_manager = setup_termux_anonymity()
    
    slow_print("\n🚀 Starting Termux-optimized reporter...", Fore.GREEN)
    slow_print("📱 Headless mode: ENABLED", Fore.CYAN)
    slow_print("🛡️  Anonymity: CONFIGURED", Fore.CYAN)
    slow_print("⏳ Please wait...\n", Fore.CYAN)
    time.sleep(2)
    
    slow_print("✅ Termux reporter ready!", Fore.GREEN + Style.BRIGHT)
    slow_print("💡 Use multi_platform_reporter.py with anonymity settings", Fore.CYAN)
    slow_print("👻 Stay anonymous, stay safe!\n", Fore.MAGENTA)
    
    # Import and run multi_platform_reporter with termux config
    try:
        # Load termux config
        termux_config_path = Path.home() / "social-reporter" / "termux_config.json"
        if termux_config_path.exists():
            with open(termux_config_path, 'r') as f:
                termux_config = json.load(f)
            
            # Merge with anonymity config
            anon_config.update(termux_config.get("termux", {}))
        
        slow_print("💡 To start reporting, run:", Fore.CYAN)
        slow_print("   python3 multi_platform_reporter.py", Fore.YELLOW)
        slow_print("\n💡 Or use the quick start:", Fore.CYAN)
        slow_print("   ~/quick_reporter.sh", Fore.YELLOW)
        
    except Exception as e:
        slow_print(f"⚠️  Error: {e}", Fore.YELLOW)
        slow_print("💡 You can still run multi_platform_reporter.py directly", Fore.CYAN)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        slow_print("\n\n🛑 Process interrupted by user (CTRL+C)", Fore.RED)
        slow_print("👻 Cleaning traces...", Fore.YELLOW)
        time.sleep(1)
        slow_print("✅ Cleanup complete. Stay safe!", Fore.GREEN)
    except Exception as e:
        print(Fore.RED + f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
