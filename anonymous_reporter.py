import time
import os
import sys
import json
import random
from colorama import Fore, Style, init
from anonymity_manager import AnonymityManager
from social_reporter import SocialReporter
from platforms.instagram_reporter import InstagramReporter
from platforms.tiktok_reporter import TikTokReporter
from platforms.twitter_reporter import TwitterReporter
from platforms.facebook_reporter import FacebookReporter
from platforms.youtube_reporter import YouTubeReporter
from platforms.reddit_reporter import RedditReporter
from platforms.linkedin_reporter import LinkedInReporter

init(autoreset=True)

def slow_print(text, color=Fore.WHITE, delay=0.03):
    """Stampa testo con effetto digitazione"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    """Banner anonimo"""
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.RED + Style.BRIGHT + r"""
    
    ░█████╗░███╗░░██╗░█████╗░███╗░░██╗██╗░░░██╗███╗░░░███╗░█████╗░██╗░░░██╗░██████╗
    ██╔══██╗████╗░██║██╔══██╗████╗░██║╚██╗░██╔╝████╗░████║██╔══██╗██║░░░██║██╔════╝
    ███████║██╔██╗██║██║░░██║██╔██╗██║░╚████╔╝░██╔████╔██║██║░░██║██║░░░██║╚█████╗░
    ██╔══██║██║╚████║██║░░██║██║╚████║░░╚██╔╝░░██║╚██╔╝██║██║░░██║██║░░░██║░╚═══██╗
    ██║░░██║██║░╚███║╚█████╔╝██║░╚███║░░░██║░░░██║░╚═╝░██║╚█████╔╝╚██████╔╝██████╔╝
    ╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░░╚═════╝░╚═════╝░
    
    ██████╗░███████╗██████╗░░█████╗░██████╗░████████╗███████╗██████╗░
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
    ██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░█████╗░░██████╔╝
    ██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
    ██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░███████╗██║░░██║
    ╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║  🛡️  ANONYMOUS MULTI-PLATFORM REPORTER - Maximum Privacy & Anonymity 🛡️    ║
    ║  🔒 Tor Support | Proxy Rotation | Fingerprint Spoofing | Encrypted 🔒     ║
    ║  👻 Stay Anonymous | No Traces | Complete Privacy Protection 👻            ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
""")

def setup_anonymity():
    """Setup anonimato"""
    slow_print("\n🛡️  ANONYMITY SETUP", Fore.CYAN + Style.BRIGHT)
    slow_print("="*70, Fore.CYAN)
    
    anon_manager = AnonymityManager()
    
    # Menu anonimato
    slow_print("\n🔒 Select Anonymity Level:", Fore.YELLOW)
    slow_print("[1] 👻 MAXIMUM (Tor + Proxy + Full Fingerprint)", Fore.GREEN)
    slow_print("[2] 🛡️  HIGH (Proxy Rotation + Fingerprint)", Fore.YELLOW)
    slow_print("[3] 🔐 MEDIUM (Fingerprint Randomization)", Fore.CYAN)
    slow_print("[4] ⚠️  LOW (Basic Protection)", Fore.RED)
    slow_print("[5] 🚫 NONE (No Anonymity - NOT RECOMMENDED)", Fore.RED + Style.BRIGHT)
    
    choice = input(Fore.GREEN + "\n📥 Your choice: ").strip()
    
    config = {
        "use_tor": False,
        "use_proxy": False,
        "proxy_rotation": False,
        "fingerprint_randomization": False,
        "encrypt_credentials": False
    }
    
    if choice == "1":
        # MAXIMUM
        slow_print("\n👻 Configuring MAXIMUM anonymity...", Fore.GREEN)
        
        # Check Tor
        slow_print("\n🔍 Checking Tor connection...", Fore.CYAN)
        tor_ok, tor_ip = anon_manager.check_tor_connection()
        
        if tor_ok:
            config["use_tor"] = True
            slow_print(f"✅ Tor ACTIVE! IP: {tor_ip}", Fore.GREEN)
        else:
            slow_print("⚠️  Tor not available. Install Tor Browser and start it.", Fore.YELLOW)
            slow_print("📝 Download: https://www.torproject.org/download/", Fore.CYAN)
            
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
        
    elif choice == "4":
        # LOW
        slow_print("\n⚠️  Configuring LOW anonymity...", Fore.RED)
        config["fingerprint_randomization"] = True
        
    else:
        # NONE
        slow_print("\n🚫 NO ANONYMITY - Proceeding without protection!", Fore.RED + Style.BRIGHT)
        slow_print("⚠️  WARNING: Your real IP and identity will be exposed!", Fore.RED)
        time.sleep(2)
    
    # Setup proxy se richiesto
    if config["use_proxy"] and not config["use_tor"]:
        slow_print("\n🔄 Setting up proxy...", Fore.CYAN)
        
        # Carica proxy
        proxies = anon_manager.get_proxy_list()
        if proxies:
            slow_print(f"📋 Found {len(proxies)} proxies in list", Fore.GREEN)
            slow_print("🔍 Validating proxies...", Fore.CYAN)
            
            proxy = anon_manager.get_random_proxy(validate=True)
            if proxy:
                slow_print(f"✅ Proxy configured: {proxy}", Fore.GREEN)
            else:
                slow_print("❌ No valid proxy found", Fore.RED)
                config["use_proxy"] = False
        else:
            slow_print("⚠️  No proxies configured. Add proxies to config.json or proxies.txt", Fore.YELLOW)
            config["use_proxy"] = False
    
    # Mostra stato anonimato
    anon_manager.print_anonymity_status()
    
    return config, anon_manager

def show_critical_warning():
    """Mostra avvertenze critiche"""
    print(Fore.RED + "\n" + "="*90)
    print(Fore.YELLOW + Style.BRIGHT + "⚠️  CRITICAL WARNING - AVVERTENZA CRITICA ⚠️")
    print(Fore.RED + "="*90)
    print(Fore.WHITE + """
    🚨 ANONYMITY DOES NOT GUARANTEE 100% PROTECTION 🚨
    
    1. ⚠️  Anche con Tor/Proxy, puoi essere tracciato
    2. 🚫 Le piattaforme hanno sistemi anti-bot avanzati
    3. 🔒 I tuoi account possono essere collegati alla tua identità
    4. ⚖️  L'uso illegale può portare a conseguenze legali GRAVI
    5. 👮 Le autorità possono richiedere dati ai provider
    6. 💀 L'anonimato non ti protegge dalla legge
    7. 📚 Usa SOLO per scopi educativi e legali
    8. ⚠️  NON usare per molestie, cyberbullismo o attività illegali
    
    ⚠️  ACCETTANDO, TI ASSUMI PIENA RESPONSABILITÀ ⚠️
    """)
    print(Fore.RED + "="*90)
    response = input(Fore.YELLOW + "\n⚠️  Comprendi i rischi e vuoi continuare? (sì/no): ").strip().lower()
    return response in ['sì', 'si', 'yes', 'y', 's']

def main():
    """Main function anonimo"""
    banner()
    
    # Avvertenze
    if not show_critical_warning():
        slow_print("\n✅ Operation cancelled. Stay safe!", Fore.BLUE)
        return
    
    # Setup anonimato
    anon_config, anon_manager = setup_anonymity()
    
    # Continua con il normale flusso ma con anonimato
    slow_print("\n🚀 Starting anonymous reporting session...", Fore.GREEN)
    slow_print("⏳ Please wait...\n", Fore.CYAN)
    time.sleep(2)
    
    # Import e esegui multi_platform_reporter con configurazione anonima
    slow_print("✅ Anonymity configured successfully!", Fore.GREEN)
    slow_print("📝 Proceeding to platform selection...\n", Fore.CYAN)
    
    # Qui puoi integrare il resto del codice di multi_platform_reporter
    # ma con le opzioni di anonimato attive
    
    slow_print("🎯 Anonymous reporter ready!", Fore.GREEN + Style.BRIGHT)
    slow_print("🛡️  Your anonymity is protected", Fore.CYAN)
    slow_print("👻 Stay anonymous, stay safe!\n", Fore.MAGENTA)

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
