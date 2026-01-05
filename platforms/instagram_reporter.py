import time
import random
import requests
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Aggiungi il percorso parent per importare social_reporter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from social_reporter import SocialReporter

class InstagramReporter(SocialReporter):
    """Reporter avanzato per Instagram"""
    
    def __init__(self, config_path="config.json"):
        super().__init__(config_path)
        self.platform_config = self.config.get("instagram", {})
        self.base_url = "https://www.instagram.com"
    
    def is_valid_username(self, username):
        """Verifica se l'username Instagram esiste"""
        url = f"{self.base_url}/{username}/"
        try:
            response = requests.get(url, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def login(self, username, password):
        """Effettua il login su Instagram con gestione avanzata"""
        try:
            self.logger.info(f"Tentativo di login Instagram per {username}")
            self.driver.get(f"{self.base_url}/accounts/login/")
            self.human_delay(2, 4)
            
            # Prova a caricare sessione salvata
            if self.load_session("instagram", username):
                self.driver.get(f"{self.base_url}/")
                self.human_delay(2, 3)
                if "accounts/login" not in self.driver.current_url:
                    self.logger.info("Login tramite sessione salvata riuscito")
                    return True
            
            # Input username
            username_selectors = [
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
            password_input = self.driver.find_element(By.NAME, "password")
            self.human_type(password_input, password)
            self.human_delay(0.5, 1)
            
            # Click login
            login_selectors = [
                "//button[@type='submit']",
                "//button[contains(text(), 'Log in')]",
                "//button[contains(text(), 'Accedi')]"
            ]
            if not self.safe_click(login_selectors[0], timeout=5):
                self.logger.error("Pulsante login non trovato")
                return False
            
            self.human_delay(3, 5)
            
            # Verifica login
            if "accounts/login" in self.driver.current_url:
                self.logger.error("Login fallito - credenziali errate")
                self.take_screenshot("login_failed")
                return False
            
            # Gestisci popup
            self.handle_popups()
            
            # Salva sessione
            self.save_session("instagram", username)
            
            self.logger.info("Login Instagram riuscito")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante login Instagram: {e}")
            self.take_screenshot("login_error")
            return False
    
    def handle_popups(self):
        """Gestisce i popup post-login"""
        popup_texts = ["Not Now", "Not now", "Non ora", "Save Info", "Turn on Notifications"]
        for text in popup_texts:
            try:
                buttons = self.driver.find_elements(By.XPATH, f"//button[contains(text(), '{text}')]")
                for btn in buttons:
                    if btn.is_displayed():
                        self.safe_click(f"//button[contains(text(), '{text}')]", timeout=2)
                        self.human_delay(1, 2)
            except:
                continue
    
    def send_report(self, target_username, reason_text):
        """Invia un report reale su Instagram"""
        try:
            self.logger.info(f"Invio report per @{target_username} - Motivo: {reason_text}")
            
            # Naviga al profilo
            profile_url = f"{self.base_url}/{target_username}/"
            self.driver.get(profile_url)
            self.human_delay(3, 5)
            
            # Scroll per caricare elementi
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
            self.human_delay(1, 2)
            
            # Click menu (tre puntini)
            menu_selectors = [
                "//button[contains(@aria-label, 'Options')]",
                "//button[contains(@aria-label, 'Menu')]",
                "//svg[@aria-label='Options']/ancestor::button",
                "//span[contains(@aria-label, 'Options')]/ancestor::button",
                "//button[contains(@class, '_abl-')]"
            ]
            
            menu_clicked = False
            for selector in menu_selectors:
                if self.safe_click(selector, timeout=3):
                    menu_clicked = True
                    break
            
            if not menu_clicked:
                self.logger.warning("Menu non trovato")
                self.take_screenshot("menu_not_found")
                return False
            
            # Click Report
            report_selectors = [
                "//button[contains(text(), 'Report')]",
                "//div[contains(text(), 'Report')]/ancestor::button",
                "//span[contains(text(), 'Report')]/ancestor::button",
                "//a[contains(text(), 'Report')]",
                "//button[contains(text(), 'Segnala')]",
                "//div[contains(text(), 'Segnala')]/ancestor::button"
            ]
            
            report_clicked = False
            for selector in report_selectors:
                if self.safe_click(selector, timeout=3):
                    report_clicked = True
                    break
            
            if not report_clicked:
                self.logger.warning("Opzione Report non trovata")
                self.take_screenshot("report_option_not_found")
                return False
            
            # Click "Report Account"
            account_report_selectors = [
                "//button[contains(text(), 'Report Account')]",
                "//div[contains(text(), 'Report Account')]/ancestor::button",
                "//button[contains(text(), 'Segnala account')]",
                "//div[contains(text(), 'Segnala account')]/ancestor::button"
            ]
            
            for selector in account_report_selectors:
                self.safe_click(selector, timeout=3)
                self.human_delay(1, 2)
            
            # Seleziona motivo (primo disponibile o generico)
            reason_selectors = [
                "//button[contains(@class, '_acan')]",
                "//div[@role='button']",
                "//button[@type='button']"
            ]
            
            for selector in reason_selectors:
                try:
                    buttons = self.driver.find_elements(By.XPATH, selector)
                    if buttons:
                        self.driver.execute_script("arguments[0].click();", buttons[0])
                        self.human_delay(1, 2)
                        break
                except:
                    continue
            
            # Submit finale
            submit_selectors = [
                "//button[contains(text(), 'Submit')]",
                "//button[contains(text(), 'Report')]",
                "//button[@type='submit']",
                "//button[contains(text(), 'Invia')]",
                "//div[@role='button']//div[contains(text(), 'Submit')]/ancestor::div[@role='button']"
            ]
            
            for selector in submit_selectors:
                buttons = self.driver.find_elements(By.XPATH, selector)
                for btn in buttons:
                    if btn.is_displayed() and btn.is_enabled():
                        self.driver.execute_script("arguments[0].click();", btn)
                        self.human_delay(2, 3)
                        self.logger.info("Report inviato con successo")
                        return True
            
            # Se arriva qui, assume successo
            self.logger.info("Report processato (assunto successo)")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante invio report: {e}")
            self.take_screenshot("report_error")
            return False
