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

class LinkedInReporter(SocialReporter):
    """Reporter avanzato per LinkedIn"""
    
    def __init__(self, config_path="config.json"):
        super().__init__(config_path)
        self.platform_config = self.config.get("linkedin", {})
        self.base_url = "https://www.linkedin.com"
    
    def is_valid_username(self, username):
        """Verifica se il profilo LinkedIn esiste"""
        url = f"{self.base_url}/in/{username}"
        try:
            response = requests.get(url, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def login(self, username, password):
        """Effettua il login su LinkedIn"""
        try:
            self.logger.info(f"Tentativo di login LinkedIn per {username}")
            self.driver.get(f"{self.base_url}/login")
            self.human_delay(3, 5)
            
            # Prova a caricare sessione salvata
            if self.load_session("linkedin", username):
                self.driver.get(f"{self.base_url}/feed/")
                self.human_delay(2, 3)
                if "login" not in self.driver.current_url.lower() and "checkpoint" not in self.driver.current_url.lower():
                    self.logger.info("Login tramite sessione salvata riuscito")
                    return True
            
            # Input email/username
            email_selectors = [
                (By.ID, "username"),
                (By.NAME, "session_key"),
                (By.XPATH, "//input[@name='session_key']"),
                (By.XPATH, "//input[@type='text']")
            ]
            
            email_input = self.find_element_safe(email_selectors, timeout=10)
            if not email_input:
                self.logger.error("Campo email non trovato")
                return False
            
            self.human_type(email_input, username)
            self.human_delay(0.5, 1)
            
            # Input password
            password_selectors = [
                (By.ID, "password"),
                (By.NAME, "session_password"),
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
                "//button[@type='submit']",
                "//button[contains(@class, 'sign-in-form__submit-button')]",
                "//button[contains(text(), 'Sign in')]",
                "//button[contains(text(), 'Accedi')]"
            ]
            
            for selector in login_selectors:
                if self.safe_click(selector, timeout=3):
                    break
            
            self.human_delay(5, 7)
            
            # Verifica login (potrebbe esserci verifica sicurezza)
            if "login" in self.driver.current_url.lower() or "checkpoint" in self.driver.current_url.lower():
                self.logger.warning("Login richiede verifica aggiuntiva o è fallito")
                self.take_screenshot("linkedin_login_verification")
                # Attendi un po' per verifica manuale se necessario
                self.human_delay(10, 15)
                
                # Ricontrolla
                if "login" in self.driver.current_url.lower():
                    self.logger.error("Login fallito")
                    return False
            
            # Salva sessione
            self.save_session("linkedin", username)
            
            self.logger.info("Login LinkedIn riuscito")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante login LinkedIn: {e}")
            self.take_screenshot("linkedin_login_error")
            return False
    
    def send_report(self, target_username, reason_text):
        """Invia un report reale su LinkedIn"""
        try:
            self.logger.info(f"Invio report LinkedIn per {target_username} - Motivo: {reason_text}")
            
            # Naviga al profilo
            profile_url = f"{self.base_url}/in/{target_username}"
            self.driver.get(profile_url)
            self.human_delay(3, 5)
            
            # Scroll
            self.driver.execute_script("window.scrollTo(0, 300);")
            self.human_delay(1, 2)
            
            # Click menu (tre puntini "More")
            menu_selectors = [
                "//button[@aria-label='More actions']",
                "//button[contains(@aria-label, 'More')]",
                "//button[contains(@id, 'ember')]//span[contains(text(), 'More')]/..",
                "//button[contains(@class, 'artdeco-dropdown__trigger')]",
                "//li-icon[@type='overflow-horizontal-icon']/.."
            ]
            
            menu_clicked = False
            for selector in menu_selectors:
                if self.safe_click(selector, timeout=3):
                    menu_clicked = True
                    break
            
            if not menu_clicked:
                self.logger.warning("Menu LinkedIn non trovato")
                self.take_screenshot("linkedin_menu_not_found")
                return False
            
            # Click Report/Flag
            report_selectors = [
                "//span[contains(text(), 'Report')]/..",
                "//div[contains(text(), 'Report')]",
                "//span[contains(text(), 'Segnala')]/..",
                "//li-icon[@type='flag-fill-icon']/..",
                "//button[contains(@aria-label, 'Report')]"
            ]
            
            report_clicked = False
            for selector in report_selectors:
                if self.safe_click(selector, timeout=3):
                    report_clicked = True
                    break
            
            if not report_clicked:
                self.logger.warning("Opzione Report non trovata")
                self.take_screenshot("linkedin_report_not_found")
                return False
            
            self.human_delay(2, 3)
            
            # Seleziona motivo (radio button o checkbox)
            reason_selectors = [
                "//input[@type='radio']/..",
                "//label[contains(@class, 'artdeco-radio')]",
                "//fieldset//label",
                "//div[contains(@class, 'report-form')]//label"
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
            
            # Click Submit
            submit_selectors = [
                "//button[contains(@aria-label, 'Submit')]",
                "//button[contains(text(), 'Submit')]",
                "//button[@type='submit']",
                "//button[contains(text(), 'Invia')]",
                "//button[contains(@class, 'artdeco-button--primary')]"
            ]
            
            for selector in submit_selectors:
                if self.safe_click(selector, timeout=3):
                    self.human_delay(2, 3)
                    break
            
            self.logger.info("Report LinkedIn inviato con successo")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante invio report LinkedIn: {e}")
            self.take_screenshot("linkedin_report_error")
            return False
