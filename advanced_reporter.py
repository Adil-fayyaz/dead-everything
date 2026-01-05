import time
import os
import sys
import json
import random
from colorama import Fore, Style, init
from social_reporter import SocialReporter
from platforms.instagram_reporter import InstagramReporter
from platforms.tiktok_reporter import TikTokReporter

init(autoreset=True)

def slow_print(text, color=Fore.WHITE, delay=0.03):
    """Stampa testo con effetto digitazione"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    """Mostra banner avanzato"""
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.MAGENTA + Style.BRIGHT + r"""
    
    ██╗███╗   ██╗███████╗████████╗ █████╗      ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗    ██╔═══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
    ██║██╔██╗ ██║███████╗   ██║   ███████║    ██║   ██║█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║    ██║   ██║██╔══╝  ██╔══██╗██║   ██║██╔══██╗   ██║   
    ██║██║ ╚████║███████║   ██║   ██║  ██║    ╚██████╔╝███████╗██║  ██║╚██████╔╝██║  ██║   ██║   
    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
    
    ╔═══════════════════════════════════════════════════════════════════════════════════════╗
    ║  🔥 ADVANCED SOCIAL MEDIA REPORTER - Instagram & TikTok 🔥                          ║
    ║  ⚡ Multi-Platform | Session Management | Anti-Detection | Logging ⚡                ║
    ╚═══════════════════════════════════════════════════════════════════════════════════════╝
""")

def select_platform():
    """Seleziona la piattaforma social"""
    slow_print("\n🌐 Select Platform:", Fore.CYAN)
    platforms = [
        "📸 Instagram",
        "🎵 TikTok",
        "🔄 Both (Multi-Platform)"
    ]
    for i, platform in enumerate(platforms, start=1):
        slow_print(f"[{i}] {platform}", Fore.YELLOW)
    choice = input(Fore.GREEN + "📥 Enter choice number: ").strip()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(platforms):
            return platforms[idx]
    except:
        pass
    return platforms[0]

def select_country():
    """Seleziona paese"""
    slow_print("\n🌍 Select Country:", Fore.YELLOW)
    countries = [
        "🇮🇳 India", "🇺🇸 USA", "🇬🇧 UK", "🇧🇩 Bangladesh",
        "🇵🇰 Pakistan", "🇮🇹 Italy", "🇩🇪 Germany", "🇫🇷 France", "🌐 Other"
    ]
    for i, country in enumerate(countries, start=1):
        slow_print(f"[{i}] {country}", Fore.CYAN)
    choice = input(Fore.GREEN + "📥 Enter choice number: ").strip()
    try:
        return countries[int(choice) - 1]
    except:
        return "🌐 Other"

def select_reason(platform="instagram"):
    """Seleziona motivo report"""
    slow_print(f"\n🚫 Select Reason for Reporting on {platform.upper()}:", Fore.RED)
    
    reasons = {
        "instagram": [
            "Fake Account",
            "Adult Content",
            "Hate Speech",
            "Harassment or Bullying",
            "Posting Violence or Abuse",
            "Spam or Scam Activity"
        ],
        "tiktok": [
            "Fake Account",
            "Inappropriate Content",
            "Harassment or Bullying",
            "Violence or Dangerous Acts",
            "Spam or Scam",
            "Hateful Behavior"
        ]
    }
    
    reason_list = reasons.get(platform, reasons["instagram"])
    for i, reason in enumerate(reason_list, start=1):
        slow_print(f"[{i}] {reason}", Fore.YELLOW)
    choice = input(Fore.GREEN + "📥 Enter reason number: ").strip()
    try:
        return reason_list[int(choice) - 1]
    except:
        return reason_list[0]

def show_warning():
    """Mostra avvertenze legali"""
    print(Fore.RED + "\n" + "="*80)
    print(Fore.YELLOW + Style.BRIGHT + "⚠️  CRITICAL LEGAL WARNING - AVVERTENZA LEGALE CRITICA ⚠️")
    print(Fore.RED + "="*80)
    print(Fore.WHITE + """
    1. ⚠️  Questo tool invia REPORT REALI su Instagram e TikTok
    2. 🚫 L'uso viola i Termini di Servizio di entrambe le piattaforme
    3. 🔒 Il tuo account può essere PERMANENTEMENTE BANNATO
    4. ⚖️  L'abuso può avere conseguenze LEGALI
    5. 💀 Usa SOLO a tuo rischio - l'autore non è responsabile
    6. 📚 Questo tool è solo per SCOPI EDUCATIVI e di RICERCA
    
    ⚠️  NON USARE PER ATTIVITÀ ILLEGALI O DANNOSE ⚠️
    """)
    print(Fore.RED + "="*80)
    response = input(Fore.YELLOW + "\n⚠️  Vuoi continuare comunque? (sì/no): ").strip().lower()
    return response in ['sì', 'si', 'yes', 'y', 's']

def run_instagram_report(reporter, username, password, target, reason, country, config):
    """Esegue report su Instagram"""
    slow_print("\n📸 Starting Instagram Report Process...", Fore.CYAN)
    
    # Inizializza driver
    reporter.driver = reporter.init_driver(
        headless=config.get("instagram", {}).get("headless", False)
    )
    if not reporter.driver:
        print(Fore.RED + "❌ Errore nell'inizializzazione del browser")
        return False, 0, 0
    
    try:
        # Login
        if not reporter.login(username, password):
            reporter.driver.quit()
            return False, 0, 0
        
        # Configura report
        num_reports = config.get("instagram", {}).get("max_reports_per_session", 5)
        delay = config.get("instagram", {}).get("default_delay", 30)
        
        slow_print(f"\n⚙️  Configuration:", Fore.BLUE)
        slow_print(f"   📊 Reports: {num_reports}", Fore.WHITE)
        slow_print(f"   ⏱️  Delay: {delay} seconds", Fore.WHITE)
        slow_print(f"   🎯 Target: @{target}", Fore.WHITE)
        slow_print(f"   🚫 Reason: {reason}", Fore.WHITE)
        
        success = 0
        failed = 0
        
        for i in range(num_reports):
            if i > 0:
                wait = delay + random.uniform(-5, 5)
                slow_print(f"\n⏳ Waiting {wait:.1f}s before next report...", Fore.CYAN)
                time.sleep(wait)
            
            slow_print(f"\n📤 Sending report #{i+1}/{num_reports}...", Fore.YELLOW)
            if reporter.send_report(target, reason):
                success += 1
                slow_print(f"✅ Report #{i+1} sent successfully!", Fore.GREEN)
            else:
                failed += 1
                slow_print(f"❌ Report #{i+1} failed", Fore.RED)
            
            time.sleep(random.uniform(2, 5))
        
        reporter.driver.quit()
        return True, success, failed
        
    except Exception as e:
        print(Fore.RED + f"\n❌ Critical error: {e}")
        try:
            reporter.driver.quit()
        except:
            pass
        return False, 0, 0

def run_tiktok_report(reporter, username, password, target, reason, country, config):
    """Esegue report su TikTok"""
    slow_print("\n🎵 Starting TikTok Report Process...", Fore.CYAN)
    
    # Inizializza driver
    reporter.driver = reporter.init_driver(
        headless=config.get("tiktok", {}).get("headless", False)
    )
    if not reporter.driver:
        print(Fore.RED + "❌ Errore nell'inizializzazione del browser")
        return False, 0, 0
    
    try:
        # Login
        if not reporter.login(username, password):
            reporter.driver.quit()
            return False, 0, 0
        
        # Configura report
        num_reports = config.get("tiktok", {}).get("max_reports_per_session", 5)
        delay = config.get("tiktok", {}).get("default_delay", 45)
        
        slow_print(f"\n⚙️  Configuration:", Fore.BLUE)
        slow_print(f"   📊 Reports: {num_reports}", Fore.WHITE)
        slow_print(f"   ⏱️  Delay: {delay} seconds", Fore.WHITE)
        slow_print(f"   🎯 Target: @{target}", Fore.WHITE)
        slow_print(f"   🚫 Reason: {reason}", Fore.WHITE)
        
        success = 0
        failed = 0
        
        for i in range(num_reports):
            if i > 0:
                wait = delay + random.uniform(-5, 5)
                slow_print(f"\n⏳ Waiting {wait:.1f}s before next report...", Fore.CYAN)
                time.sleep(wait)
            
            slow_print(f"\n📤 Sending report #{i+1}/{num_reports}...", Fore.YELLOW)
            if reporter.send_report(target, reason):
                success += 1
                slow_print(f"✅ Report #{i+1} sent successfully!", Fore.GREEN)
            else:
                failed += 1
                slow_print(f"❌ Report #{i+1} failed", Fore.RED)
            
            time.sleep(random.uniform(2, 5))
        
        reporter.driver.quit()
        return True, success, failed
        
    except Exception as e:
        print(Fore.RED + f"\n❌ Critical error: {e}")
        try:
            reporter.driver.quit()
        except:
            pass
        return False, 0, 0

def main():
    """Funzione principale"""
    banner()
    
    # Avvertimenti
    if not show_warning():
        slow_print("\n✅ Operation cancelled. Thank you for being responsible.", Fore.BLUE)
        return
    
    # Selezione piattaforma
    platform_choice = select_platform()
    platforms_to_run = []
    
    if "Instagram" in platform_choice:
        platforms_to_run.append("instagram")
    if "TikTok" in platform_choice:
        platforms_to_run.append("tiktok")
    
    if not platforms_to_run:
        platforms_to_run = ["instagram"]
    
    # Credenziali
    slow_print("\n🔐 Enter your credentials:", Fore.CYAN)
    slow_print("⚠️  Credentials are used only for the session and NOT saved", Fore.YELLOW)
    
    username = input(Fore.GREEN + "📧 Username: ").strip()
    password = input(Fore.GREEN + "🔒 Password: ").strip()
    
    if not username or not password:
        print(Fore.RED + "\n❌ Username and password are required!")
        return
    
    # Target
    slow_print("\n🎯 Enter target username to report:", Fore.CYAN)
    target = input(Fore.GREEN + "@").strip().lstrip('@')
    
    if not target:
        print(Fore.RED + "\n❌ Target username is required!")
        return
    
    # Country e reason
    country = select_country()
    
    # Risultati
    total_success = 0
    total_failed = 0
    
    # Carica config
    try:
        with open("config.json", 'r') as f:
            config = json.load(f)
    except:
        config = {}
    
    # Esegui report per ogni piattaforma
    for platform in platforms_to_run:
        slow_print(f"\n{'='*80}", Fore.BLUE)
        slow_print(f"🚀 PROCESSING {platform.upper()}", Fore.CYAN)
        slow_print(f"{'='*80}", Fore.BLUE)
        
        reason = select_reason(platform)
        
        if platform == "instagram":
            reporter = InstagramReporter()
            if not reporter.is_valid_username(target):
                slow_print(f"\n❌ Invalid Instagram username: @{target}", Fore.RED)
                continue
            
            ok, success, failed = run_instagram_report(
                reporter, username, password, target, reason, country, config
            )
            total_success += success
            total_failed += failed
            
        elif platform == "tiktok":
            reporter = TikTokReporter()
            if not reporter.is_valid_username(target):
                slow_print(f"\n❌ Invalid TikTok username: @{target}", Fore.RED)
                continue
            
            ok, success, failed = run_tiktok_report(
                reporter, username, password, target, reason, country, config
            )
            total_success += success
            total_failed += failed
        
        time.sleep(3)  # Pausa tra piattaforme
    
    # Statistiche finali
    print(Fore.BLUE + "\n" + "="*80)
    print(Fore.CYAN + Style.BRIGHT + "📊 FINAL STATISTICS")
    print(Fore.BLUE + "="*80)
    print(Fore.GREEN + f"✅ Total reports sent successfully: {total_success}")
    print(Fore.RED + f"❌ Total reports failed: {total_failed}")
    print(Fore.BLUE + f"📊 Total attempts: {total_success + total_failed}")
    print(Fore.BLUE + "="*80)
    
    slow_print("\n✅ Process completed!", Fore.GREEN)
    slow_print("📝 Check logs/ directory for detailed logs", Fore.CYAN)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        slow_print("\n\n🛑 Process interrupted by user (CTRL+C)", Fore.RED)
    except Exception as e:
        print(Fore.RED + f"\n❌ Fatal error: {e}")
