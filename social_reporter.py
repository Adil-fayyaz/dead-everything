import time
import os
import json
import random
import logging
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

class SocialReporter:
    """Classe base per il reporting su social media"""
    
    def __init__(self, config_path="config.json"):
        self.config = self.load_config(config_path)
        self.driver = None
        self.session_dir = Path(self.config.get("advanced", {}).get("session_dir", "sessions"))
        self.session_dir.mkdir(exist_ok=True)
        self.setup_logging()
    
    def load_config(self, config_path):
        """Carica la configurazione dal file JSON"""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def setup_logging(self):
        """Configura il sistema di logging"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f"reporter_{datetime.now().strftime('%Y%m%d')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def init_driver(self, headless=None, use_proxy=False, proxy=None):
        """Inizializza il driver Selenium con opzioni avanzate"""
        chrome_options = Options()
        
        if headless is None:
            headless = self.config.get("advanced", {}).get("headless", False)
        
        if headless:
            chrome_options.add_argument('--headless=new')
        
        # Anti-detection measures
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # User agent random
        user_agents = self.config.get("advanced", {}).get("user_agents", [])
        if user_agents:
            user_agent = random.choice(user_agents)
        else:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        chrome_options.add_argument(f'--user-agent={user_agent}')
        
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--lang=en-US,en')
        
        # Proxy support
        if use_proxy and proxy:
            chrome_options.add_argument(f'--proxy-server={proxy}')
        
        # Prefs
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.managed_default_content_settings.images": 1
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
            self.logger.info("Driver inizializzato con successo")
            return driver
        except Exception as e:
            self.logger.error(f"Errore nell'inizializzazione del driver: {e}")
            return None
    
    def save_session(self, platform, username):
        """Salva i cookies della sessione"""
        if not self.config.get("advanced", {}).get("save_session", True):
            return
        
        try:
            cookies = self.driver.get_cookies()
            session_file = self.session_dir / f"{platform}_{username}_session.json"
            with open(session_file, 'w') as f:
                json.dump(cookies, f)
            self.logger.info(f"Sessione salvata per {platform} - {username}")
        except Exception as e:
            self.logger.error(f"Errore nel salvare la sessione: {e}")
    
    def load_session(self, platform, username):
        """Carica i cookies della sessione salvata"""
        try:
            session_file = self.session_dir / f"{platform}_{username}_session.json"
            if session_file.exists():
                with open(session_file, 'r') as f:
                    cookies = json.load(f)
                    for cookie in cookies:
                        try:
                            self.driver.add_cookie(cookie)
                        except:
                            pass
                self.logger.info(f"Sessione caricata per {platform} - {username}")
                return True
        except Exception as e:
            self.logger.error(f"Errore nel caricare la sessione: {e}")
        return False
    
    def take_screenshot(self, name="error"):
        """Cattura screenshot in caso di errore"""
        if not self.config.get("advanced", {}).get("screenshots_on_error", True):
            return
        
        try:
            screenshots_dir = Path(self.config.get("advanced", {}).get("screenshots_dir", "screenshots_errors"))
            screenshots_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = screenshots_dir / f"{name}_{timestamp}.png"
            self.driver.save_screenshot(str(screenshot_path))
            self.logger.info(f"Screenshot salvato: {screenshot_path}")
        except Exception as e:
            self.logger.error(f"Errore nel salvare screenshot: {e}")
    
    def human_delay(self, min_seconds=1, max_seconds=3):
        """Delay randomizzato per sembrare più umano"""
        delay = random.uniform(min_seconds, max_seconds)
        time.sleep(delay)
    
    def human_type(self, element, text, delay_range=(0.05, 0.2)):
        """Scrive testo come un umano con delay random"""
        element.clear()
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(*delay_range))
    
    def safe_click(self, selector, by=By.XPATH, timeout=10, use_js=True):
        """Click sicuro con fallback a JavaScript"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            if use_js:
                self.driver.execute_script("arguments[0].click();", element)
            else:
                element.click()
            self.human_delay(0.5, 1.5)
            return True
        except Exception as e:
            self.logger.warning(f"Click fallito per {selector}: {e}")
            return False
    
    def find_element_safe(self, selectors, timeout=5):
        """Trova elemento provando più selettori"""
        for selector in selectors:
            try:
                if isinstance(selector, tuple):
                    by, value = selector
                else:
                    by, value = By.XPATH, selector
                
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, value))
                )
                return element
            except:
                continue
        return None
