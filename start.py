#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script di avvio semplice per il tool di reporting
Verifica le dipendenze e avvia l'interfaccia corretta
"""

import sys
import os

def check_dependencies():
    """Verifica che tutte le dipendenze siano installate"""
    missing = []
    
    required = [
        'colorama',
        'requests',
        'selenium',
        'webdriver_manager',
        'cryptography',
        'json',
        'time',
        'random'
    ]
    
    optional = [
        'PySocks',
        'stem'
    ]
    
    print("\n🔍 Checking dependencies...")
    
    for module in required:
        try:
            __import__(module)
            print(f"  ✅ {module}")
        except ImportError:
            print(f"  ❌ {module} - MISSING!")
            missing.append(module)
    
    for module in optional:
        try:
            __import__(module)
            print(f"  ✅ {module} (optional)")
        except ImportError:
            print(f"  ⚠️  {module} (optional) - not installed")
    
    return missing

def show_menu():
    """Mostra il menu principale"""
    print("\n" + "="*60)
    print("  🔥 INSTA-REPORT - Social Media Reporting Tool")
    print("="*60)
    print("\n  Select which script to run:")
    print("\n  1. 🎯 insta-report.py")
    print("     → Original Instagram reporter (basic)")
    print("\n  2. 🌐 multi_platform_reporter.py")
    print("     → Multi-platform reporter (Instagram, TikTok, Twitter, etc.)")
    print("\n  3. 👻 anonymous_reporter.py")
    print("     → Multi-platform with anonymity features")
    print("\n  4. 🚀 advanced_reporter.py")
    print("     → Instagram + TikTok reporter")
    print("\n  5. 📱 termux_reporter.py")
    print("     → Termux-optimized version")
    print("\n  0. ❌ Exit")
    print("\n" + "="*60)

def main():
    """Funzione principale"""
    os.system('clear' if os.name != 'nt' else 'cls')
    
    print("\n" + "="*60)
    print("  🔥 INSTA-REPORT - Startup Script")
    print("="*60)
    
    # Verifica dipendenze
    missing = check_dependencies()
    
    if missing:
        print(f"\n❌ Missing required dependencies: {', '.join(missing)}")
        print("\n📦 Install them with:")
        print(f"   pip3 install {' '.join(missing)}")
        print("\nOr install all dependencies:")
        print("   pip3 install colorama requests selenium webdriver-manager cryptography PySocks stem")
        sys.exit(1)
    
    print("\n✅ All dependencies OK!")
    
    # Menu principale
    while True:
        show_menu()
        
        try:
            choice = input("\n👉 Select option (0-5): ").strip()
            
            if choice == '0':
                print("\n👋 Goodbye!")
                sys.exit(0)
            
            elif choice == '1':
                print("\n🚀 Starting insta-report.py...")
                os.system('python3 insta-report.py')
                break
            
            elif choice == '2':
                print("\n🚀 Starting multi_platform_reporter.py...")
                os.system('python3 multi_platform_reporter.py')
                break
            
            elif choice == '3':
                print("\n🚀 Starting anonymous_reporter.py...")
                os.system('python3 anonymous_reporter.py')
                break
            
            elif choice == '4':
                print("\n🚀 Starting advanced_reporter.py...")
                os.system('python3 advanced_reporter.py')
                break
            
            elif choice == '5':
                print("\n🚀 Starting termux_reporter.py...")
                os.system('python3 termux_reporter.py')
                break
            
            else:
                print("\n❌ Invalid option! Please select 0-5.")
                input("\nPress Enter to continue...")
                os.system('clear' if os.name != 'nt' else 'cls')
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {e}")
            input("\nPress Enter to continue...")
            os.system('clear' if os.name != 'nt' else 'cls')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
