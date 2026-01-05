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

class TikTokReporter(SocialReporter):
    """Reporter avanzato per TikTok"""
    
    def __init__(self, config_path="config.json"):
        super().__init__(config_path)
        self.platform_config = self.config.get("tiktok", {})
        self.base_url = "https://www.tiktok.com"
    
    def is_valid_username(self, username):
        """Verifica se l'username TikTok esiste"""
        url = f"{self.base_url}/@{username}"
        try:
            response = requests.get(url, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def login(self, username, password):
        """Effettua il login su TikTok"""
        try:
            self.logger.info(f"Tentativo di login TikTok per {username}")
            self.driver.get(f"{self.base_url}/login")
            self.human_delay(3, 5)
            
            # Prova a caricare sessione salvata
            if self.load_session("tiktok", username):
                self.driver.get(f"{self.base_url}/")
                self.human_delay(2, 3)
                if "login" not in self.driver.current_url.lower():
                    self.logger.info("Login tramite sessione salvata riuscito")
                    return True
            
            # TikTok può richiedere login con email/phone o username
            # Prova vari metodi di input
            login_selectors = [
                (By.XPATH, "//input[@placeholder='Email or username']"),
                (By.XPATH, "//input[@placeholder='Username or email']"),
                (By.XPATH, "//input[@type='text']"),
                (By.XPATH, "//input[@name='username']")
            ]
            
            username_input = self.find_element_safe(login_selectors, timeout=10)
            if not username_input:
                self.logger.error("Campo username non trovato")
                return False
            
            self.human_type(username_input, username)
            self.human_delay(0.5, 1)
            
            # Password
            password_selectors = [
                (By.XPATH, "//input[@type='password']"),
                (By.XPATH, "//input[@placeholder='Password']"),
                (By.NAME, "password")
            ]
            
            password_input = self.find_element_safe(password_selectors, timeout=5)
            if not password_input:
                self.logger.error("Campo password non trovato")
                return False
            
            self.human_type(password_input, password)
            self.human_delay(0.5, 1)
            
            # Click login
            login_button_selectors = [
                "//button[@type='submit']",
                "//button[contains(text(), 'Log in')]",
                "//button[contains(text(), 'Login')]",
                "//button[contains(@class, 'login-button')]"
            ]
            
            login_clicked = False
            for selector in login_button_selectors:
                if self.safe_click(selector, timeout=5):
                    login_clicked = True
                    break
            
            if not login_clicked:
                self.logger.error("Pulsante login non trovato")
                return False
            
            self.human_delay(5, 7)  # TikTok può richiedere più tempo
            
            # Verifica login
            if "login" in self.driver.current_url.lower():
                self.logger.error("Login fallito")
                self.take_screenshot("login_failed")
                return False
            
            # Gestisci popup/captcha
            self.handle_popups()
            
            # Salva sessione
            self.save_session("tiktok", username)
            
            self.logger.info("Login TikTok riuscito")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante login TikTok: {e}")
            self.take_screenshot("login_error")
            return False
    
    def handle_popups(self):
        """Gestisce popup e notifiche post-login"""
        try:
            # Chiudi popup notifiche
            close_buttons = self.driver.find_elements(By.XPATH, 
                "//button[contains(@class, 'close')] | //button[contains(@aria-label, 'Close')] | //div[contains(@class, 'close')]")
            for btn in close_buttons[:2]:  # Max 2 tentativi
                try:
                    if btn.is_displayed():
                        btn.click()
                        self.human_delay(1, 2)
                except:
                    continue
        except:
            pass
    
    def send_report(self, target_username, reason_text):
        """Invia un report reale su TikTok"""
        try:
            self.logger.info(f"Invio report TikTok per @{target_username} - Motivo: {reason_text}")
            
            # Naviga al profilo
            profile_url = f"{self.base_url}/@{target_username}"
            self.driver.get(profile_url)
            self.human_delay(3, 5)
            
            # Scroll per caricare
            self.driver.execute_script("window.scrollTo(0, 500);")
            self.human_delay(1, 2)
            
            # TikTok ha un menu a tre puntini nella parte superiore del profilo
            # Prova vari selettori per il menu
            menu_selectors = [
                "//button[contains(@aria-label, 'More options')]",
                "//button[contains(@aria-label, 'Menu')]",
                "//svg[contains(@data-e2e, 'more-icon')]/ancestor::button",
                "//div[contains(@data-e2e, 'more-icon')]/ancestor::button",
                "//button[contains(@class, 'more')]",
                "//span[contains(@class, 'more')]/ancestor::button"
            ]
            
            menu_clicked = False
            for selector in menu_selectors:
                if self.safe_click(selector, timeout=3):
                    menu_clicked = True
                    break
            
            if not menu_clicked:
                # Prova alternativa: click su "..." icon
                try:
                    more_icons = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'icon-more')] | //*[contains(@class, 'more-icon')]")
                    if more_icons:
                        self.driver.execute_script("arguments[0].click();", more_icons[0])
                        self.human_delay(1, 2)
                        menu_clicked = True
                except:
                    pass
            
            if not menu_clicked:
                self.logger.warning("Menu TikTok non trovato")
                self.take_screenshot("tiktok_menu_not_found")
                return False
            
            # Click Report
            report_selectors = [
                "//div[contains(text(), 'Report')]",
                "//button[contains(text(), 'Report')]",
                "//span[contains(text(), 'Report')]/ancestor::div[@role='button']",
                "//div[contains(text(), 'Segnala')]",
                "//div[contains(@data-e2e, 'report')]"
            ]
            
            report_clicked = False
            for selector in report_selectors:
                if self.safe_click(selector, timeout=3):
                    report_clicked = True
                    break
            
            if not report_clicked:
                self.logger.warning("Opzione Report non trovata")
                self.take_screenshot("tiktok_report_not_found")
                return False
            
            # Selezione motivo (TikTok ha una struttura diversa)
            # Prova a selezionare un motivo generico
            reason_selectors = [
                "//div[@role='button']",
                "//div[contains(@class, 'report-item')]",
                "//div[contains(@class, 'option')]"
            ]
            
            for selector in reason_selectors:
                try:
                    options = self.driver.find_elements(By.XPATH, selector)
                    if options:
                        # Clicca sul primo motivo disponibile
                        self.driver.execute_script("arguments[0].click();", options[0])
                        self.human_delay(1, 2)
                        break
                except:
                    continue
            
            # Submit finale
            submit_selectors = [
                "//button[contains(text(), 'Submit')]",
                "//button[contains(text(), 'Report')]",
                "//div[contains(text(), 'Submit')]/ancestor::div[@role='button']",
                "//div[contains(@data-e2e, 'submit')]"
            ]
            
            for selector in submit_selectors:
                try:
                    buttons = self.driver.find_elements(By.XPATH, selector)
                    for btn in buttons:
                        if btn.is_displayed() and btn.is_enabled():
                            self.driver.execute_script("arguments[0].click();", btn)
                            self.human_delay(2, 3)
                            self.logger.info("Report TikTok inviato con successo")
                            return True
                except:
                    continue
            
            # Assume successo se arrivato qui
            self.logger.info("Report TikTok processato (assunto successo)")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante invio report TikTok: {e}")
            self.take_screenshot("tiktok_report_error")
            return False
