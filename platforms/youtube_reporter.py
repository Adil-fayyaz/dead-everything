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

class YouTubeReporter(SocialReporter):
    """Reporter avanzato per YouTube"""
    
    def __init__(self, config_path="config.json"):
        super().__init__(config_path)
        self.platform_config = self.config.get("youtube", {})
        self.base_url = "https://www.youtube.com"
    
    def is_valid_username(self, username):
        """Verifica se il canale YouTube esiste"""
        # YouTube può usare @username o /c/channelname
        urls = [
            f"{self.base_url}/@{username}",
            f"{self.base_url}/c/{username}",
            f"{self.base_url}/user/{username}"
        ]
        for url in urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    return True
            except:
                continue
        return False
    
    def login(self, username, password):
        """Effettua il login su YouTube (tramite Google)"""
        try:
            self.logger.info(f"Tentativo di login YouTube/Google per {username}")
            self.driver.get("https://accounts.google.com/signin")
            self.human_delay(3, 5)
            
            # Prova a caricare sessione salvata
            if self.load_session("youtube", username):
                self.driver.get(f"{self.base_url}/")
                self.human_delay(2, 3)
                # Verifica se loggato cercando l'avatar
                try:
                    avatar = self.driver.find_elements(By.ID, "avatar-btn")
                    if avatar:
                        self.logger.info("Login tramite sessione salvata riuscito")
                        return True
                except:
                    pass
            
            # Input email
            email_selectors = [
                (By.ID, "identifierId"),
                (By.NAME, "identifier"),
                (By.XPATH, "//input[@type='email']")
            ]
            
            email_input = self.find_element_safe(email_selectors, timeout=10)
            if not email_input:
                self.logger.error("Campo email non trovato")
                return False
            
            self.human_type(email_input, username)
            self.human_delay(0.5, 1)
            
            # Click Next
            next_selectors = [
                "//span[contains(text(), 'Next')]/..",
                "//button[contains(@id, 'identifierNext')]",
                "//span[contains(text(), 'Avanti')]/.."
            ]
            
            for selector in next_selectors:
                if self.safe_click(selector, timeout=3):
                    break
            
            self.human_delay(3, 5)
            
            # Input password
            password_selectors = [
                (By.NAME, "password"),
                (By.XPATH, "//input[@type='password']"),
                (By.XPATH, "//input[@name='Passwd']")
            ]
            
            password_input = self.find_element_safe(password_selectors, timeout=10)
            if not password_input:
                self.logger.error("Campo password non trovato")
                return False
            
            self.human_type(password_input, password)
            self.human_delay(0.5, 1)
            
            # Click Next/Sign in
            signin_selectors = [
                "//span[contains(text(), 'Next')]/..",
                "//button[contains(@id, 'passwordNext')]",
                "//span[contains(text(), 'Avanti')]/.."
            ]
            
            for selector in signin_selectors:
                if self.safe_click(selector, timeout=3):
                    break
            
            self.human_delay(5, 7)
            
            # Naviga a YouTube
            self.driver.get(f"{self.base_url}/")
            self.human_delay(2, 3)
            
            # Verifica login
            try:
                avatar = self.driver.find_elements(By.ID, "avatar-btn")
                if not avatar:
                    self.logger.error("Login fallito")
                    self.take_screenshot("youtube_login_failed")
                    return False
            except:
                self.logger.error("Login fallito")
                return False
            
            # Salva sessione
            self.save_session("youtube", username)
            
            self.logger.info("Login YouTube riuscito")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante login YouTube: {e}")
            self.take_screenshot("youtube_login_error")
            return False
    
    def send_report(self, target_username, reason_text):
        """Invia un report reale su YouTube"""
        try:
            self.logger.info(f"Invio report YouTube per @{target_username} - Motivo: {reason_text}")
            
            # Naviga al canale
            channel_urls = [
                f"{self.base_url}/@{target_username}",
                f"{self.base_url}/c/{target_username}",
                f"{self.base_url}/user/{target_username}"
            ]
            
            channel_loaded = False
            for url in channel_urls:
                self.driver.get(url)
                self.human_delay(3, 5)
                if "error" not in self.driver.current_url.lower():
                    channel_loaded = True
                    break
            
            if not channel_loaded:
                self.logger.warning("Canale YouTube non trovato")
                return False
            
            # Scroll
            self.driver.execute_script("window.scrollTo(0, 300);")
            self.human_delay(1, 2)
            
            # Click menu (tre puntini o flag icon)
            menu_selectors = [
                "//button[@aria-label='More']",
                "//button[contains(@aria-label, 'More')]",
                "//yt-icon-button[@id='button']//button",
                "//button[contains(@class, 'yt-spec-button-shape-next')]"
            ]
            
            menu_clicked = False
            for selector in menu_selectors:
                try:
                    buttons = self.driver.find_elements(By.XPATH, selector)
                    for btn in buttons:
                        if btn.is_displayed():
                            self.driver.execute_script("arguments[0].click();", btn)
                            self.human_delay(1, 2)
                            menu_clicked = True
                            break
                    if menu_clicked:
                        break
                except:
                    continue
            
            if not menu_clicked:
                # Prova con flag icon diretto
                try:
                    flag_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Report']")
                    self.driver.execute_script("arguments[0].click();", flag_button)
                    menu_clicked = True
                    self.human_delay(1, 2)
                except:
                    pass
            
            if not menu_clicked:
                self.logger.warning("Menu YouTube non trovato")
                self.take_screenshot("youtube_menu_not_found")
                return False
            
            # Click Report
            report_selectors = [
                "//tp-yt-paper-item[contains(text(), 'Report')]",
                "//yt-formatted-string[contains(text(), 'Report')]",
                "//tp-yt-paper-item[contains(text(), 'Segnala')]",
                "//span[contains(text(), 'Report user')]"
            ]
            
            report_clicked = False
            for selector in report_selectors:
                if self.safe_click(selector, timeout=3):
                    report_clicked = True
                    break
            
            if not report_clicked:
                self.logger.warning("Opzione Report non trovata")
                self.take_screenshot("youtube_report_not_found")
                return False
            
            self.human_delay(2, 3)
            
            # Seleziona motivo (primo disponibile o specifico)
            reason_selectors = [
                "//tp-yt-paper-radio-button",
                "//yt-formatted-string[@class='style-scope ytd-report-form-modal-renderer']/..",
                "//div[@id='label']"
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
                "//button[@aria-label='Submit']",
                "//yt-button-renderer[@id='submit-button']//button",
                "//button[contains(text(), 'Submit')]",
                "//button[contains(text(), 'Invia')]"
            ]
            
            for selector in submit_selectors:
                if self.safe_click(selector, timeout=3):
                    self.human_delay(2, 3)
                    break
            
            self.logger.info("Report YouTube inviato con successo")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante invio report YouTube: {e}")
            self.take_screenshot("youtube_report_error")
            return False
