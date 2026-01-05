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

class FacebookReporter(SocialReporter):
    """Reporter avanzato per Facebook"""
    
    def __init__(self, config_path="config.json"):
        super().__init__(config_path)
        self.platform_config = self.config.get("facebook", {})
        self.base_url = "https://www.facebook.com"
    
    def is_valid_username(self, username):
        """Verifica se l'username Facebook esiste"""
        url = f"{self.base_url}/{username}"
        try:
            response = requests.get(url, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def login(self, username, password):
        """Effettua il login su Facebook"""
        try:
            self.logger.info(f"Tentativo di login Facebook per {username}")
            self.driver.get(f"{self.base_url}/login")
            self.human_delay(3, 5)
            
            # Prova a caricare sessione salvata
            if self.load_session("facebook", username):
                self.driver.get(f"{self.base_url}/")
                self.human_delay(2, 3)
                if "login" not in self.driver.current_url.lower():
                    self.logger.info("Login tramite sessione salvata riuscito")
                    return True
            
            # Input email/username
            email_selectors = [
                (By.ID, "email"),
                (By.NAME, "email"),
                (By.XPATH, "//input[@type='text']"),
                (By.XPATH, "//input[@name='email']")
            ]
            
            email_input = self.find_element_safe(email_selectors, timeout=10)
            if not email_input:
                self.logger.error("Campo email non trovato")
                return False
            
            self.human_type(email_input, username)
            self.human_delay(0.5, 1)
            
            # Input password
            password_selectors = [
                (By.ID, "pass"),
                (By.NAME, "pass"),
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
                "//button[@name='login']",
                "//button[@type='submit']",
                "//button[contains(text(), 'Log in')]",
                "//button[contains(text(), 'Accedi')]"
            ]
            
            for selector in login_selectors:
                if self.safe_click(selector, timeout=3):
                    break
            
            self.human_delay(5, 7)
            
            # Verifica login
            if "login" in self.driver.current_url.lower():
                self.logger.error("Login fallito")
                self.take_screenshot("facebook_login_failed")
                return False
            
            # Gestisci popup "Save Login Info"
            try:
                not_now = self.driver.find_elements(By.XPATH, "//span[contains(text(), 'Not Now')] | //span[contains(text(), 'Non ora')]")
                if not_now:
                    not_now[0].click()
                    self.human_delay(1, 2)
            except:
                pass
            
            # Salva sessione
            self.save_session("facebook", username)
            
            self.logger.info("Login Facebook riuscito")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante login Facebook: {e}")
            self.take_screenshot("facebook_login_error")
            return False
    
    def send_report(self, target_username, reason_text):
        """Invia un report reale su Facebook"""
        try:
            self.logger.info(f"Invio report Facebook per {target_username} - Motivo: {reason_text}")
            
            # Naviga al profilo
            profile_url = f"{self.base_url}/{target_username}"
            self.driver.get(profile_url)
            self.human_delay(3, 5)
            
            # Scroll
            self.driver.execute_script("window.scrollTo(0, 300);")
            self.human_delay(1, 2)
            
            # Click menu (tre puntini)
            menu_selectors = [
                "//div[@aria-label='More']",
                "//div[@aria-label='Altro']",
                "//i[contains(@class, 'x1lliihq')]/../..",
                "//div[contains(@aria-label, 'Action')]",
                "//span[contains(text(), '...')]/ancestor::div[@role='button']"
            ]
            
            menu_clicked = False
            for selector in menu_selectors:
                if self.safe_click(selector, timeout=3):
                    menu_clicked = True
                    break
            
            if not menu_clicked:
                self.logger.warning("Menu Facebook non trovato")
                self.take_screenshot("facebook_menu_not_found")
                return False
            
            # Click "Find support or report"
            report_selectors = [
                "//span[contains(text(), 'Find support or report')]",
                "//span[contains(text(), 'Trova assistenza o segnala')]",
                "//span[contains(text(), 'Report')]",
                "//span[contains(text(), 'Segnala')]",
                "//div[@role='menuitem']//span[contains(text(), 'support')]"
            ]
            
            report_clicked = False
            for selector in report_selectors:
                if self.safe_click(selector, timeout=3):
                    report_clicked = True
                    break
            
            if not report_clicked:
                self.logger.warning("Opzione Report non trovata")
                self.take_screenshot("facebook_report_not_found")
                return False
            
            self.human_delay(2, 3)
            
            # Click "Report profile"
            profile_report_selectors = [
                "//span[contains(text(), 'Report profile')]",
                "//span[contains(text(), 'Segnala profilo')]",
                "//div[@role='menuitem']//span[contains(text(), 'profile')]"
            ]
            
            for selector in profile_report_selectors:
                if self.safe_click(selector, timeout=3):
                    self.human_delay(1, 2)
                    break
            
            # Seleziona motivo (primo disponibile)
            reason_selectors = [
                "//div[@role='radio']",
                "//input[@type='radio']/..",
                "//div[contains(@class, 'x1i10hfl')][@role='button']"
            ]
            
            for selector in reason_selectors:
                try:
                    options = self.driver.find_elements(By.XPATH, selector)
                    if options:
                        self.driver.execute_script("arguments[0].click();", options[0])
                        self.human_delay(1, 2)
                        break
                except:
                    continue
            
            # Click Submit/Next
            submit_selectors = [
                "//span[contains(text(), 'Submit')]/..",
                "//span[contains(text(), 'Next')]/..",
                "//span[contains(text(), 'Invia')]/..",
                "//span[contains(text(), 'Avanti')]/..",
                "//div[@aria-label='Submit']",
                "//div[@aria-label='Next']"
            ]
            
            # Potrebbe richiedere più click
            for _ in range(3):
                clicked = False
                for selector in submit_selectors:
                    if self.safe_click(selector, timeout=2):
                        clicked = True
                        self.human_delay(1, 2)
                        break
                if not clicked:
                    break
            
            self.logger.info("Report Facebook inviato con successo")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante invio report Facebook: {e}")
            self.take_screenshot("facebook_report_error")
            return False
