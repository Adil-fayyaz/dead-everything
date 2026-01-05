import time
import random
import requests
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from social_reporter import SocialReporter

class RedditReporter(SocialReporter):
    """Reporter avanzato per Reddit"""
    
    def __init__(self, config_path="config.json"):
        super().__init__(config_path)
        self.platform_config = self.config.get("reddit", {})
        self.base_url = "https://www.reddit.com"
    
    def is_valid_username(self, username):
        """Verifica se l'username Reddit esiste"""
        url = f"{self.base_url}/user/{username}"
        try:
            response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            return response.status_code == 200
        except:
            return False
    
    def login(self, username, password):
        """Effettua il login su Reddit"""
        try:
            self.logger.info(f"Tentativo di login Reddit per {username}")
            self.driver.get(f"{self.base_url}/login")
            self.human_delay(3, 5)
            
            # Prova a caricare sessione salvata
            if self.load_session("reddit", username):
                self.driver.get(f"{self.base_url}/")
                self.human_delay(2, 3)
                if "login" not in self.driver.current_url.lower():
                    self.logger.info("Login tramite sessione salvata riuscito")
                    return True
            
            # Input username
            username_selectors = [
                (By.ID, "loginUsername"),
                (By.NAME, "username"),
                (By.XPATH, "//input[@name='username']"),
                (By.XPATH, "//input[@type='text']")
            ]
            
            username_input = self.find_element_safe(username_selectors, timeout=10)
            if not username_input:
                self.logger.error("Campo username non trovato")
                return False
            
            self.human_type(username_input, username)
            self.human_delay(0.5, 1)
            
            # Input password
            password_selectors = [
                (By.ID, "loginPassword"),
                (By.NAME, "password"),
                (By.XPATH, "//input[@type='password']")
            ]
            
            password_input = self.find_element_safe(password_selectors, timeout=5)
            if not password_input:
                self.logger.error("Campo password non trovato")
                return False
            
            self.human_type(password_input, password)
            self.human_delay(0.5, 1)
            
            # Click login
            login_selectors = [
                "//button[contains(text(), 'Log in')]",
                "//button[contains(text(), 'Log In')]",
                "//button[@type='submit']",
                "//button[contains(@class, 'AnimatedForm__submitButton')]"
            ]
            
            for selector in login_selectors:
                if self.safe_click(selector, timeout=3):
                    break
            
            self.human_delay(5, 7)
            
            # Verifica login
            if "login" in self.driver.current_url.lower():
                self.logger.error("Login fallito")
                self.take_screenshot("reddit_login_failed")
                return False
            
            # Salva sessione
            self.save_session("reddit", username)
            
            self.logger.info("Login Reddit riuscito")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante login Reddit: {e}")
            self.take_screenshot("reddit_login_error")
            return False
    
    def send_report(self, target_username, reason_text):
        """Invia un report reale su Reddit"""
        try:
            self.logger.info(f"Invio report Reddit per u/{target_username} - Motivo: {reason_text}")
            
            # Naviga al profilo
            profile_url = f"{self.base_url}/user/{target_username}"
            self.driver.get(profile_url)
            self.human_delay(3, 5)
            
            # Scroll
            self.driver.execute_script("window.scrollTo(0, 300);")
            self.human_delay(1, 2)
            
            # Click menu (tre puntini)
            menu_selectors = [
                "//button[@aria-label='More options']",
                "//button[contains(@aria-label, 'more options')]",
                "//button[contains(@id, 'USER_DROPDOWN')]",
                "//i[contains(@class, 'icon-menu')]/..",
                "//button[contains(@class, '_3ch9jJ0painNf41PmU4F9i')]"
            ]
            
            menu_clicked = False
            for selector in menu_selectors:
                if self.safe_click(selector, timeout=3):
                    menu_clicked = True
                    break
            
            if not menu_clicked:
                self.logger.warning("Menu Reddit non trovato")
                self.take_screenshot("reddit_menu_not_found")
                return False
            
            # Click Report
            report_selectors = [
                "//span[contains(text(), 'Report')]",
                "//button[contains(text(), 'Report')]",
                "//div[contains(text(), 'Report')]",
                "//span[contains(text(), 'Segnala')]"
            ]
            
            report_clicked = False
            for selector in report_selectors:
                if self.safe_click(selector, timeout=3):
                    report_clicked = True
                    break
            
            if not report_clicked:
                self.logger.warning("Opzione Report non trovata")
                self.take_screenshot("reddit_report_not_found")
                return False
            
            self.human_delay(2, 3)
            
            # Seleziona categoria (es: Spam, Harassment, etc.)
            category_selectors = [
                "//button[contains(text(), 'Spam')]",
                "//button[contains(text(), 'Harassment')]",
                "//label[contains(text(), 'Spam')]",
                "//label[contains(text(), 'Harassment')]",
                "//input[@type='radio']/.."
            ]
            
            for selector in category_selectors:
                if self.safe_click(selector, timeout=3):
                    self.human_delay(1, 2)
                    break
            
            # Click Submit
            submit_selectors = [
                "//button[contains(text(), 'Submit')]",
                "//button[contains(text(), 'Report')]",
                "//button[@type='submit']",
                "//button[contains(text(), 'Invia')]"
            ]
            
            # Potrebbe richiedere più click
            for _ in range(2):
                clicked = False
                for selector in submit_selectors:
                    if self.safe_click(selector, timeout=2):
                        clicked = True
                        self.human_delay(1, 2)
                        break
                if not clicked:
                    break
            
            self.logger.info("Report Reddit inviato con successo")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante invio report Reddit: {e}")
            self.take_screenshot("reddit_report_error")
            return False
