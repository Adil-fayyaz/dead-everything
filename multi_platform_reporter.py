import time
import os
import sys
import json
import random
from colorama import Fore, Style, init
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
    """Mostra banner multi-platform"""
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.MAGENTA + Style.BRIGHT + r"""
    
    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗      ██████╗ ██╗      █████╗ ████████╗███████╗ ██████╗ ██████╗ ███╗   ███╗
    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║      ██╔══██╗██║     ██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗████╗ ████║
    ██╔████╔██║██║   ██║██║     ██║   ██║█████╗██████╔╝██║     ███████║   ██║   █████╗  ██║   ██║██████╔╝██╔████╔██║
    ██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════╝██╔═══╝ ██║     ██╔══██║   ██║   ██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║
    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║      ██║     ███████╗██║  ██║   ██║   ██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║
    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
    
    ╔════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║  🔥 MULTI-PLATFORM SOCIAL MEDIA REPORTER - 7 Platforms Supported! 🔥                             ║
    ║  📸 Instagram | 🎵 TikTok | 🐦 Twitter/X | 👥 Facebook | ▶️ YouTube | 🤖 Reddit | 💼 LinkedIn  ║
    ║  ⚡ Advanced Automation | Session Management | Anti-Detection | Multi-Account Support ⚡         ║
    ╚════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

def select_platforms():
    """Seleziona le piattaforme social (multipla selezione)"""
    slow_print("\n🌐 Select Platform(s) - You can select multiple:", Fore.CYAN)
    platforms = {
        "1": ("📸 Instagram", "instagram"),
        "2": ("🎵 TikTok", "tiktok"),
        "3": ("🐦 Twitter/X", "twitter"),
        "4": ("👥 Facebook", "facebook"),
        "5": ("▶️  YouTube", "youtube"),
        "6": ("🤖 Reddit", "reddit"),
        "7": ("💼 LinkedIn", "linkedin"),
        "8": ("🌟 ALL PLATFORMS", "all")
    }
    
    for key, (name, _) in platforms.items():
        slow_print(f"[{key}] {name}", Fore.YELLOW)
    
    slow_print("\n💡 Enter numbers separated by commas (e.g., 1,3,5) or 8 for ALL", Fore.CYAN)
    choice = input(Fore.GREEN + "📥 Your selection: ").strip()
    
    selected = []
    try:
        choices = [c.strip() for c in choice.split(',')]
        if '8' in choices:
            # Seleziona tutte le piattaforme
            selected = [code for _, code in platforms.values() if code != "all"]
        else:
            for c in choices:
                if c in platforms and platforms[c][1] != "all":
                    selected.append(platforms[c][1])
    except:
        pass
    
    if not selected:
        selected = ["instagram"]  # Default
    
    return selected

def select_country():
    """Seleziona paese"""
    slow_print("\n🌍 Select Country:", Fore.YELLOW)
    countries = [
        "🇮🇳 India", "🇺🇸 USA", "🇬🇧 UK", "🇧🇩 Bangladesh",
        "🇵🇰 Pakistan", "🇮🇹 Italy", "🇩🇪 Germany", "🇫🇷 France",
        "🇪🇸 Spain", "🇧🇷 Brazil", "🇨🇦 Canada", "🇦🇺 Australia", "🌐 Other"
    ]
    for i, country in enumerate(countries, start=1):
        slow_print(f"[{i}] {country}", Fore.CYAN)
    choice = input(Fore.GREEN + "📥 Enter choice number: ").strip()
    try:
        return countries[int(choice) - 1]
    except:
        return "🌐 Other"

def select_reason(platform="instagram"):
    """Seleziona motivo report per piattaforma specifica"""
    slow_print(f"\n🚫 Select Reason for Reporting on {platform.upper()}:", Fore.RED)
    
    reasons = {
        "instagram": [
            "Fake Account", "Adult Content", "Hate Speech",
            "Harassment or Bullying", "Violence or Abuse", "Spam or Scam"
        ],
        "tiktok": [
            "Fake Account", "Inappropriate Content", "Harassment or Bullying",
            "Violence or Dangerous Acts", "Spam or Scam", "Hateful Behavior"
        ],
        "twitter": [
            "Spam", "Abusive or Harmful", "Fake Account",
            "Impersonation", "Misleading Information", "Hateful Content"
        ],
        "facebook": [
            "Fake Account", "Harassment", "Hate Speech",
            "Violence", "Spam", "Inappropriate Content"
        ],
        "youtube": [
            "Spam or Misleading", "Hateful Content", "Harassment",
            "Violent Content", "Child Safety", "Infringes My Rights"
        ],
        "reddit": [
            "Spam", "Harassment", "Threatening Violence",
            "Hate", "Impersonation", "Prohibited Content"
        ],
        "linkedin": [
            "Fake Profile", "Harassment", "Inappropriate Content",
            "Spam", "Scam or Fraud", "Hate Speech"
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
    """Mostra avvertenze legali critiche"""
    print(Fore.RED + "\n" + "="*90)
    print(Fore.YELLOW + Style.BRIGHT + "⚠️  CRITICAL LEGAL WARNING - AVVERTENZA LEGALE CRITICA ⚠️")
    print(Fore.RED + "="*90)
    print(Fore.WHITE + """
    1. ⚠️  Questo tool invia REPORT REALI su 7 PIATTAFORME SOCIAL
    2. 🚫 L'uso viola i Termini di Servizio di TUTTE le piattaforme
    3. 🔒 I tuoi account possono essere PERMANENTEMENTE BANNATI
    4. ⚖️  L'abuso può avere CONSEGUENZE LEGALI GRAVI
    5. 💀 Usa SOLO a tuo rischio - l'autore NON è responsabile
    6. 📚 Questo tool è SOLO per SCOPI EDUCATIVI e di RICERCA
    7. 🛡️  NON USARE per attività ILLEGALI, DANNOSE o MOLESTIE
    8. ⚠️  Potresti essere PERSEGUITO LEGALMENTE per abuso
    
    ⚠️  ACCETTANDO, TI ASSUMI PIENA RESPONSABILITÀ ⚠️
    """)
    print(Fore.RED + "="*90)
    response = input(Fore.YELLOW + "\n⚠️  Accetti i rischi e vuoi continuare? (sì/no): ").strip().lower()
    return response in ['sì', 'si', 'yes', 'y', 's']

def get_reporter(platform, config):
    """Factory per creare il reporter appropriato"""
    reporters = {
        "instagram": InstagramReporter,
        "tiktok": TikTokReporter,
        "twitter": TwitterReporter,
        "facebook": FacebookReporter,
        "youtube": YouTubeReporter,
        "reddit": RedditReporter,
        "linkedin": LinkedInReporter
    }
    return reporters.get(platform, InstagramReporter)()

def run_platform_report(platform, reporter, username, password, target, reason, config):
    """Esegue report su una piattaforma specifica"""
    platform_name = platform.upper()
    slow_print(f"\n{'='*90}", Fore.BLUE)
    slow_print(f"🚀 PROCESSING {platform_name}", Fore.CYAN + Style.BRIGHT)
    slow_print(f"{'='*90}", Fore.BLUE)
    
    # Inizializza driver
    reporter.driver = reporter.init_driver(
        headless=config.get(platform, {}).get("headless", False)
    )
    if not reporter.driver:
        slow_print(f"❌ Errore nell'inizializzazione del browser per {platform_name}", Fore.RED)
        return False, 0, 0
    
    try:
        # Login
        slow_print(f"\n🔐 Logging in to {platform_name}...", Fore.CYAN)
        if not reporter.login(username, password):
            reporter.driver.quit()
            slow_print(f"❌ Login fallito su {platform_name}", Fore.RED)
            return False, 0, 0
        
        slow_print(f"✅ Login successful on {platform_name}!", Fore.GREEN)
        
        # Configura report
        num_reports = config.get(platform, {}).get("max_reports_per_session", 5)
        delay = config.get(platform, {}).get("default_delay", 30)
        
        slow_print(f"\n⚙️  Configuration for {platform_name}:", Fore.BLUE)
        slow_print(f"   📊 Reports: {num_reports}", Fore.WHITE)
        slow_print(f"   ⏱️  Delay: {delay} seconds", Fore.WHITE)
        slow_print(f"   🎯 Target: {target}", Fore.WHITE)
        slow_print(f"   🚫 Reason: {reason}", Fore.WHITE)
        
        success = 0
        failed = 0
        
        for i in range(num_reports):
            if i > 0:
                wait = delay + random.uniform(-5, 5)
                slow_print(f"\n⏳ Waiting {wait:.1f}s before next report...", Fore.CYAN)
                time.sleep(wait)
            
            slow_print(f"\n📤 Sending report #{i+1}/{num_reports} on {platform_name}...", Fore.YELLOW)
            if reporter.send_report(target, reason):
                success += 1
                slow_print(f"✅ Report #{i+1} sent successfully on {platform_name}!", Fore.GREEN)
            else:
                failed += 1
                slow_print(f"❌ Report #{i+1} failed on {platform_name}", Fore.RED)
            
            time.sleep(random.uniform(2, 5))
        
        reporter.driver.quit()
        return True, success, failed
        
    except Exception as e:
        slow_print(f"\n❌ Critical error on {platform_name}: {e}", Fore.RED)
        try:
            reporter.driver.quit()
        except:
            pass
        return False, 0, 0

def main():
    """Funzione principale multi-platform"""
    banner()
    
    # Avvertimenti
    if not show_warning():
        slow_print("\n✅ Operation cancelled. Thank you for being responsible.", Fore.BLUE)
        return
    
    # Selezione piattaforme
    platforms_to_run = select_platforms()
    
    slow_print(f"\n✅ Selected platforms: {', '.join([p.upper() for p in platforms_to_run])}", Fore.GREEN)
    
    # Credenziali
    slow_print("\n🔐 Enter your credentials:", Fore.CYAN)
    slow_print("⚠️  Use the SAME credentials for all platforms (or press Enter to skip per platform)", Fore.YELLOW)
    
    username = input(Fore.GREEN + "📧 Username/Email: ").strip()
    password = input(Fore.GREEN + "🔒 Password: ").strip()
    
    if not username or not password:
        slow_print("\n⚠️  No credentials provided. You'll be asked per platform.", Fore.YELLOW)
    
    # Target
    slow_print("\n🎯 Enter target username to report:", Fore.CYAN)
    target = input(Fore.GREEN + "@").strip().lstrip('@')
    
    if not target:
        slow_print("\n❌ Target username is required!", Fore.RED)
        return
    
    # Country
    country = select_country()
    
    # Carica config
    try:
        with open("config.json", 'r') as f:
            config = json.load(f)
    except:
        config = {}
    
    # Statistiche globali
    total_success = 0
    total_failed = 0
    platform_results = {}
    
    # Esegui report per ogni piattaforma
    for platform in platforms_to_run:
        slow_print(f"\n\n{'#'*90}", Fore.MAGENTA)
        slow_print(f"# STARTING {platform.upper()} REPORTING SESSION", Fore.MAGENTA + Style.BRIGHT)
        slow_print(f"{'#'*90}\n", Fore.MAGENTA)
        
        # Chiedi credenziali specifiche se non fornite
        platform_username = username
        platform_password = password
        
        if not platform_username or not platform_password:
            slow_print(f"\n🔐 Enter credentials for {platform.upper()}:", Fore.CYAN)
            platform_username = input(Fore.GREEN + f"📧 {platform.capitalize()} Username/Email: ").strip()
            platform_password = input(Fore.GREEN + f"🔒 {platform.capitalize()} Password: ").strip()
            
            if not platform_username or not platform_password:
                slow_print(f"\n❌ Skipping {platform.upper()} - no credentials provided", Fore.RED)
                continue
        
        # Seleziona motivo per questa piattaforma
        reason = select_reason(platform)
        
        # Crea reporter
        reporter = get_reporter(platform, config)
        
        # Verifica username valido
        slow_print(f"\n🔍 Validating target on {platform.upper()}...", Fore.CYAN)
        if not reporter.is_valid_username(target):
            slow_print(f"\n❌ Invalid username on {platform.upper()}: {target}", Fore.RED)
            slow_print(f"⚠️  Skipping {platform.upper()}", Fore.YELLOW)
            platform_results[platform] = {"success": 0, "failed": 0, "status": "Invalid username"}
            continue
        
        slow_print(f"✅ Username valid on {platform.upper()}!", Fore.GREEN)
        
        # Esegui report
        ok, success, failed = run_platform_report(
            platform, reporter, platform_username, platform_password, target, reason, config
        )
        
        total_success += success
        total_failed += failed
        platform_results[platform] = {
            "success": success,
            "failed": failed,
            "status": "Completed" if ok else "Error"
        }
        
        # Pausa tra piattaforme
        if platform != platforms_to_run[-1]:
            slow_print(f"\n⏸️  Pausing 10 seconds before next platform...", Fore.CYAN)
            time.sleep(10)
    
    # Statistiche finali dettagliate
    print(Fore.BLUE + "\n\n" + "="*90)
    print(Fore.CYAN + Style.BRIGHT + "📊 FINAL STATISTICS - MULTI-PLATFORM REPORT")
    print(Fore.BLUE + "="*90)
    
    # Per piattaforma
    for platform, results in platform_results.items():
        emoji = {"instagram": "📸", "tiktok": "🎵", "twitter": "🐦", "facebook": "👥",
                 "youtube": "▶️", "reddit": "🤖", "linkedin": "💼"}.get(platform, "🌐")
        print(Fore.YELLOW + f"\n{emoji} {platform.upper()}:")
        print(Fore.GREEN + f"   ✅ Success: {results['success']}")
        print(Fore.RED + f"   ❌ Failed: {results['failed']}")
        print(Fore.CYAN + f"   📋 Status: {results['status']}")
    
    # Totale
    print(Fore.BLUE + "\n" + "-"*90)
    print(Fore.GREEN + Style.BRIGHT + f"✅ TOTAL REPORTS SENT SUCCESSFULLY: {total_success}")
    print(Fore.RED + Style.BRIGHT + f"❌ TOTAL REPORTS FAILED: {total_failed}")
    print(Fore.BLUE + Style.BRIGHT + f"📊 TOTAL ATTEMPTS: {total_success + total_failed}")
    print(Fore.CYAN + f"🌐 PLATFORMS PROCESSED: {len(platform_results)}")
    print(Fore.BLUE + "="*90)
    
    slow_print("\n✅ Multi-platform reporting process completed!", Fore.GREEN)
    slow_print("📝 Check logs/ directory for detailed logs", Fore.CYAN)
    slow_print("📸 Check screenshots_errors/ for any error screenshots", Fore.CYAN)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        slow_print("\n\n🛑 Process interrupted by user (CTRL+C)", Fore.RED)
    except Exception as e:
        print(Fore.RED + f"\n❌ Fatal error: {e}")
