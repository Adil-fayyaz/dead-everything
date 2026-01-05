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

# Aggiungi il percorso parent per importare social_reporter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from social_reporter import SocialReporter

class TwitterReporter(SocialReporter):
    """Reporter avanzato per Twitter/X"""
    
    def __init__(self, config_path="config.json"):
        super().__init__(config_path)
        self.platform_config = self.config.get("twitter", {})
        self.base_url = "https://twitter.com"
    
    def is_valid_username(self, username):
        """Verifica se l'username Twitter esiste"""
        url = f"{self.base_url}/{username}"
        try:
            response = requests.get(url, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def login(self, username, password):
        """Effettua il login su Twitter/X"""
        try:
            self.logger.info(f"Tentativo di login Twitter per {username}")
            self.driver.get(f"{self.base_url}/i/flow/login")
            self.human_delay(3, 5)
            
            # Prova a caricare sessione salvata
            if self.load_session("twitter", username):
                self.driver.get(f"{self.base_url}/home")
                self.human_delay(2, 3)
                if "login" not in self.driver.current_url.lower():
                    self.logger.info("Login tramite sessione salvata riuscito")
                    return True
            
            # Input username/email
            username_selectors = [
                (By.NAME, "text"),
                (By.XPATH, "//input[@autocomplete='username']"),
                (By.XPATH, "//input[@name='text']"),
                (By.XPATH, "//input[@type='text']")
            ]
            
            username_input = self.find_element_safe(username_selectors, timeout=10)
            if not username_input:
                self.logger.error("Campo username non trovato")
                return False
            
            self.human_type(username_input, username)
            self.human_delay(0.5, 1)
            
            # Click Next
            next_selectors = [
                "//span[contains(text(), 'Next')]/..",
                "//div[@role='button']//span[contains(text(), 'Next')]",
                "//button[contains(text(), 'Next')]"
            ]
            
            for selector in next_selectors:
                if self.safe_click(selector, timeout=3):
                    break
            
            self.human_delay(2, 3)
            
            # Potrebbe chiedere username aggiuntivo (verifica)
            try:
                additional_username = self.driver.find_elements(By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")
                if additional_username:
                    self.human_type(additional_username[0], username)
                    self.safe_click("//span[contains(text(), 'Next')]/..", timeout=3)
                    self.human_delay(2, 3)
            except:
                pass
            
            # Input password
            password_selectors = [
                (By.NAME, "password"),
                (By.XPATH, "//input[@type='password']"),
                (By.XPATH, "//input[@name='password']")
            ]
            
            password_input = self.find_element_safe(password_selectors, timeout=10)
            if not password_input:
                self.logger.error("Campo password non trovato")
                return False
            
            self.human_type(password_input, password)
            self.human_delay(0.5, 1)
            
            # Click Login
            login_selectors = [
                "//span[contains(text(), 'Log in')]/..",
                "//div[@role='button']//span[contains(text(), 'Log in')]",
                "//button[contains(@data-testid, 'LoginForm_Login_Button')]"
            ]
            
            for selector in login_selectors:
                if self.safe_click(selector, timeout=3):
                    break
            
            self.human_delay(5, 7)
            
            # Verifica login
            if "login" in self.driver.current_url.lower() or "flow" in self.driver.current_url.lower():
                self.logger.error("Login fallito")
                self.take_screenshot("twitter_login_failed")
                return False
            
            # Salva sessione
            self.save_session("twitter", username)
            
            self.logger.info("Login Twitter riuscito")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante login Twitter: {e}")
            self.take_screenshot("twitter_login_error")
            return False
    
    def send_report(self, target_username, reason_text):
        """Invia un report reale su Twitter/X"""
        try:
            self.logger.info(f"Invio report Twitter per @{target_username} - Motivo: {reason_text}")
            
            # Naviga al profilo
            profile_url = f"{self.base_url}/{target_username}"
            self.driver.get(profile_url)
            self.human_delay(3, 5)
            
            # Scroll per caricare
            self.driver.execute_script("window.scrollTo(0, 300);")
            self.human_delay(1, 2)
            
            # Click menu (tre puntini)
            menu_selectors = [
                "//button[@aria-label='More']",
                "//div[@aria-label='More']",
                "//button[@data-testid='userActions']",
                "//div[@data-testid='userActions']",
                "//button[contains(@aria-label, 'More')]"
            ]
            
            menu_clicked = False
            for selector in menu_selectors:
                if self.safe_click(selector, timeout=3):
                    menu_clicked = True
                    break
            
            if not menu_clicked:
                self.logger.warning("Menu Twitter non trovato")
                self.take_screenshot("twitter_menu_not_found")
                return False
            
            # Click Report
            report_selectors = [
                "//span[contains(text(), 'Report')]/..",
                "//div[@role='menuitem']//span[contains(text(), 'Report')]",
                "//div[contains(text(), 'Report @')]",
                "//span[contains(text(), 'Segnala')]/.."
            ]
            
            report_clicked = False
            for selector in report_selectors:
                if self.safe_click(selector, timeout=3):
                    report_clicked = True
                    break
            
            if not report_clicked:
                self.logger.warning("Opzione Report non trovata")
                self.take_screenshot("twitter_report_not_found")
                return False
            
            self.human_delay(2, 3)
            
            # Seleziona tipo di problema
            problem_selectors = [
                "//span[contains(text(), 'Suspicious or spam')]/..",
                "//span[contains(text(), 'Abusive or harmful')]/..",
                "//div[@role='button']//span[contains(text(), 'spam')]",
                "//div[@role='button']//span[contains(text(), 'harmful')]"
            ]
            
            for selector in problem_selectors:
                if self.safe_click(selector, timeout=3):
                    self.human_delay(1, 2)
                    break
            
            # Click Next/Submit
            submit_selectors = [
                "//span[contains(text(), 'Next')]/..",
                "//span[contains(text(), 'Submit')]/..",
                "//div[@role='button']//span[contains(text(), 'Next')]",
                "//div[@role='button']//span[contains(text(), 'Submit')]"
            ]
            
            # Potrebbe richiedere più click Next
            for _ in range(3):
                clicked = False
                for selector in submit_selectors:
                    if self.safe_click(selector, timeout=2):
                        clicked = True
                        self.human_delay(1, 2)
                        break
                if not clicked:
                    break
            
            self.logger.info("Report Twitter inviato con successo")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante invio report Twitter: {e}")
            self.take_screenshot("twitter_report_error")
            return False
