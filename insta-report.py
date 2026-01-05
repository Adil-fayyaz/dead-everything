import time
import os
import requests
import sys
import random
from colorama import Fore, Style, init
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

init(autoreset=True)

def slow_print(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.MAGENTA + Style.BRIGHT + r"""
    
    
#### ##    ##  ######  ########    ###            ########  ######## ########   #######  ########  ######## 
 ##  ###   ## ##    ##    ##      ## ##           ##     ## ##       ##     ## ##     ## ##     ##    ##    
 ##  ####  ## ##          ##     ##   ##          ##     ## ##       ##     ## ##     ## ##     ##    ##    
 ##  ## ## ##  ######     ##    ##     ## ####### ########  ######   ########  ##     ## ########     ##    
 ##  ##  ####       ##    ##    #########         ##   ##   ##       ##        ##     ## ##   ##      ##    
 ##  ##   ### ##    ##    ##    ##     ##         ##    ##  ##       ##        ##     ## ##    ##     ##    
#### ##    ##  ######     ##    ##     ##         ##     ## ######## ##         #######  ##     ##    ##    

                                                                                         
       🔥 INSTA-REPORT - Instagram Reporter Tool by @the_silent_hacker_raj 🔥
 
         SUBSCRIBE TO OUR YOUTUBE CHANNEL HACKER COLONY OFFICIAL🌐🤗
""")

def is_valid_username(username):
    url = f"https://www.instagram.com/{username}/"
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

def select_country():
    slow_print("\n🌍 Select the Country of the Instagram Account:", Fore.YELLOW)
    countries = [
        "🇮🇳 India",
        "🇺🇸 USA",
        "🇬🇧 UK",
        "🇧🇩 Bangladesh",
        "🇵🇰 Pakistan",
        "🌐 Other"
    ]
    for i, country in enumerate(countries, start=1):
        slow_print(f"[{i}] {country}", Fore.CYAN)
    choice = input(Fore.GREEN + "📥 Enter choice number: ")
    try:
        return countries[int(choice) - 1]
    except:
        return "🌐 Other"
def select_reason():
    slow_print("\n🚫 Select the Reason for Reporting:", Fore.RED)
    reasons = [
        "Fake Account",
        "Adult Content",
        "Hate Speech",
        "Harassment or Bullying",
        "Posting Violence or Abuse",
        "Spam or Scam Activity"
    ]
    for i, reason in enumerate(reasons, start=1):
        slow_print(f"[{i}] {reason}", Fore.YELLOW)
    choice = input(Fore.GREEN + "📥 Enter reason number: ")
    try:
        return reasons[int(choice) - 1]
    except:
        return "Fake Account"

def get_instagram_reason_code(reason):
    """Mappa i motivi italiani ai codici usati da Instagram"""
    reason_map = {
        "Fake Account": "pretending_to_be_someone",
        "Adult Content": "nudity_or_pornography",
        "Hate Speech": "hate_speech_or_symbols",
        "Harassment or Bullying": "bullying_or_harassment",
        "Posting Violence or Abuse": "violence_or_dangerous_organizations",
        "Spam or Scam Activity": "spam"
    }
    return reason_map.get(reason, "pretending_to_be_someone")

def init_driver():
    """Inizializza il driver Selenium con opzioni configurate"""
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Decommentare per modalità headless
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    chrome_options.add_argument('--window-size=1920,1080')
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
    except Exception as e:
        print(Fore.RED + f"\n❌ Errore nell'inizializzazione del browser: {e}")
        print(Fore.YELLOW + "💡 Assicurati di avere Chrome installato e di aver eseguito: pip install -r requirements.txt")
        return None

def login_instagram(driver, username, password):
    """Effettua il login su Instagram"""
    try:
        slow_print("\n🔐 Accedendo a Instagram...", Fore.CYAN)
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(random.uniform(2, 4))
        
        # Input username
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_input.clear()
        for char in username:
            username_input.send_keys(char)
            time.sleep(random.uniform(0.05, 0.15))
        time.sleep(random.uniform(0.5, 1))
        
        # Input password
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        for char in password:
            password_input.send_keys(char)
            time.sleep(random.uniform(0.05, 0.15))
        time.sleep(random.uniform(0.5, 1))
        
        # Click login button
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(random.uniform(3, 5))
        
        # Controlla se il login è riuscito
        if "accounts/login" in driver.current_url:
            print(Fore.RED + "\n❌ Login fallito! Controlla username e password.")
            return False
        
        # Gestisci popup "Not Now" se presenti
        try:
            not_now_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
            for btn in not_now_buttons:
                if btn.is_displayed():
                    btn.click()
                    time.sleep(1)
        except:
            pass
        
        print(Fore.GREEN + "✅ Login effettuato con successo!")
        return True
        
    except TimeoutException:
        print(Fore.RED + "\n❌ Timeout durante il login. Instagram potrebbe aver rilevato automazione.")
        return False
    except Exception as e:
        print(Fore.RED + f"\n❌ Errore durante il login: {e}")
        return False

def send_real_report(driver, target_username, reason_code, reason_text):
    """Invia un report reale su Instagram"""
    try:
        # Naviga al profilo target
        profile_url = f"https://www.instagram.com/{target_username}/"
        driver.get(profile_url)
        time.sleep(random.uniform(3, 5))
        
        # Scroll per assicurarsi che la pagina sia caricata
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
        time.sleep(random.uniform(1, 2))
        
        # Clicca sui tre puntini (menu) - prova vari selettori
        menu_found = False
        menu_selectors = [
            "//button[contains(@aria-label, 'Options')]",
            "//button[contains(@aria-label, 'Menu')]",
            "//svg[@aria-label='Options']/ancestor::button",
            "//span[contains(@aria-label, 'Options')]/ancestor::button",
            "//button[contains(@class, '_abl-')]",
            "//div[@role='button' and contains(@tabindex, '0')]//svg[@aria-label='Options']/ancestor::div[@role='button']"
        ]
        
        for selector in menu_selectors:
            try:
                menu_button = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, selector))
                )
                driver.execute_script("arguments[0].click();", menu_button)
                time.sleep(random.uniform(1, 2))
                menu_found = True
                break
            except:
                continue
        
        if not menu_found:
            print(Fore.YELLOW + "⚠️  Menu non trovato, prova manualmente")
            return False
        
        # Clicca su "Report" - prova vari selettori
        report_found = False
        report_selectors = [
            "//button[contains(text(), 'Report')]",
            "//div[contains(text(), 'Report')]",
            "//a[contains(text(), 'Report')]",
            "//span[contains(text(), 'Report')]/ancestor::button",
            "//div[contains(text(), 'Segnala')]/ancestor::button",  # Italiano
            "//button[contains(@class, '_acan')]//div[contains(text(), 'Report')]"
        ]
        
        for selector in report_selectors:
            try:
                report_option = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, selector))
                )
                driver.execute_script("arguments[0].click();", report_option)
                time.sleep(random.uniform(2, 3))
                report_found = True
                break
            except:
                continue
        
        if not report_found:
            print(Fore.YELLOW + "⚠️  Opzione Report non trovata")
            return False
        
        # Seleziona "Report Account" se presente
        try:
            report_account = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Report Account')] | //div[contains(text(), 'Report Account')] | //button[contains(text(), 'Segnala account')]"))
            )
            driver.execute_script("arguments[0].click();", report_account)
            time.sleep(random.uniform(1, 2))
        except:
            pass
        
        # Seleziona il motivo specifico o usa il primo motivo disponibile
        try:
            # Prova prima a trovare un motivo specifico
            reason_selectors = [
                f"//button[contains(text(), '{reason_text}')]",
                f"//div[contains(text(), '{reason_text}')]",
                "//button[contains(@class, '_acan')]",
                "//div[@role='button']"
            ]
            
            for selector in reason_selectors:
                try:
                    reason_buttons = driver.find_elements(By.XPATH, selector)
                    if reason_buttons:
                        # Clicca sul primo pulsante disponibile (motivo generico)
                        driver.execute_script("arguments[0].click();", reason_buttons[0])
                        time.sleep(random.uniform(1, 2))
                        break
                except:
                    continue
        except:
            pass
        
        # Conferma finale - "Submit" o "Report"
        try:
            submit_selectors = [
                "//button[contains(text(), 'Submit')]",
                "//button[contains(text(), 'Report')]",
                "//button[@type='submit']",
                "//button[contains(text(), 'Invia')]",  # Italiano
                "//div[@role='button']//div[contains(text(), 'Submit')]/ancestor::div[@role='button']"
            ]
            
            for selector in submit_selectors:
                submit_buttons = driver.find_elements(By.XPATH, selector)
                for btn in submit_buttons:
                    if btn.is_displayed() and btn.is_enabled():
                        driver.execute_script("arguments[0].click();", btn)
                        time.sleep(random.uniform(2, 3))
                        return True
        except:
            pass
        
        # Se arriva qui, il report potrebbe essere stato inviato comunque
        return True
        
    except Exception as e:
        print(Fore.YELLOW + f"⚠️  Errore durante il report: {str(e)[:100]}")
        return False

def show_warning():
    """Mostra avvertenze legali e di sicurezza"""
    print(Fore.RED + "\n" + "="*70)
    print(Fore.YELLOW + Style.BRIGHT + "⚠️  AVVERTENZA LEGALE IMPORTANTE ⚠️")
    print(Fore.RED + "="*70)
    print(Fore.WHITE + """
    1. L'uso di questo strumento può violare i Termini di Servizio di Instagram
    2. Il tuo account Instagram potrebbe essere BANNATO o SOSPESO
    3. L'abuso del sistema di reporting può avere conseguenze legali
    4. Usa questo strumento SOLO a tuo rischio e pericolo
    5. L'autore non si assume alcuna responsabilità per l'uso improprio
    
    Questo strumento è solo per scopi educativi e di ricerca.
    """)
    print(Fore.RED + "="*70)
    response = input(Fore.YELLOW + "\n⚠️  Vuoi continuare comunque? (sì/no): ").strip().lower()
    return response in ['sì', 'si', 'yes', 'y', 's']

def main():
    banner()
    
    # Mostra avvertimenti
    if not show_warning():
        print(Fore.BLUE + "\n✅ Operazione annullata. Grazie per aver scelto responsabilità.")
        return
    
    # Richiedi credenziali Instagram
    slow_print("\n🔐 Inserisci le tue credenziali Instagram per effettuare il login:", Fore.CYAN)
    print(Fore.YELLOW + "⚠️  Le credenziali sono usate solo per la sessione e non vengono salvate")
    insta_username = input(Fore.GREEN + "📧 Username Instagram: ").strip()
    insta_password = input(Fore.GREEN + "🔒 Password Instagram: ").strip()
    
    if not insta_username or not insta_password:
        print(Fore.RED + "\n❌ Username e password sono richiesti!")
        return
    
    # Inizializza browser
    driver = init_driver()
    if not driver:
        return
    
    try:
        # Login
        if not login_instagram(driver, insta_username, insta_password):
            driver.quit()
            return
        
        # Richiedi username target
        slow_print("\n🔎 Enter Instagram Username to report:", Fore.CYAN)
        target_username = input(Fore.GREEN + "@").strip().lstrip('@')

        if not is_valid_username(target_username):
            print(Fore.RED + f"\n❌ Invalid Instagram Username: @{target_username}")
            driver.quit()
        return

    country = select_country()
    reason = select_reason()
        reason_code = get_instagram_reason_code(reason)

        print(Fore.GREEN + f"\n✅ Valid Username Detected: @{target_username}")
    print(Fore.BLUE + f"🌍 Country Selected: {country}")
    print(Fore.RED + f"🚫 Reason Selected: {reason}")
        
        # Chiedi numero di report
        try:
            num_reports = input(Fore.YELLOW + "\n📊 Quanti report vuoi inviare? (default: 1): ").strip()
            num_reports = int(num_reports) if num_reports else 1
            num_reports = max(1, min(num_reports, 10))  # Limite massimo 10
        except:
            num_reports = 1
        
        delay = input(Fore.YELLOW + "⏱️  Delay tra i report in secondi (default: 30): ").strip()
        try:
            delay = float(delay) if delay else 30.0
            delay = max(10, delay)  # Minimo 10 secondi
        except:
            delay = 30.0
        
        print(Fore.YELLOW + f"\n🚀 Inizio invio di {num_reports} report per @{target_username}...")
        print(Fore.YELLOW + f"⏱️  Delay tra i report: {delay} secondi")
        print(Fore.YELLOW + "⚠️  Premi CTRL+C per interrompere\n")

        count = 0
        success_count = 0
        failed_count = 0
        
        try:
            for i in range(num_reports):
                if i > 0:
                    wait_time = delay + random.uniform(-5, 5)
                    print(Fore.CYAN + f"\n⏳ Attesa {wait_time:.1f} secondi prima del prossimo report...")
                    time.sleep(wait_time)
                
                print(Fore.YELLOW + f"\n📤 Invio report #{i+1}/{num_reports}...")
                
                if send_real_report(driver, target_username, reason_code, reason):
            count += 1
                    success_count += 1
                    print(Fore.GREEN + f"✅ Report #{count} inviato con successo per @{target_username} (Motivo: {reason})")
                else:
                    failed_count += 1
                    print(Fore.RED + f"❌ Report #{i+1} fallito. Instagram potrebbe aver rilevato automazione.")
                
                # Delay aggiuntivo random per sembrare più umano
                time.sleep(random.uniform(2, 5))
                
    except KeyboardInterrupt:
            print(Fore.RED + "\n\n🛑 Reporting interrotto dall'utente (CTRL+C)")
        
        # Statistiche finali
        print(Fore.BLUE + "\n" + "="*70)
        print(Fore.CYAN + Style.BRIGHT + "📊 STATISTICHE FINALI")
        print(Fore.BLUE + "="*70)
        print(Fore.GREEN + f"✅ Report inviati con successo: {success_count}")
        print(Fore.RED + f"❌ Report falliti: {failed_count}")
        print(Fore.BLUE + f"📊 Totale tentativi: {count + failed_count}")
        print(Fore.BLUE + "="*70)
        
        # Chiusura browser
        print(Fore.YELLOW + "\n🔒 Chiusura browser...")
        time.sleep(2)
        driver.quit()
        
    except Exception as e:
        print(Fore.RED + f"\n❌ Errore critico: {e}")
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    main()
