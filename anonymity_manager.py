import os
import sys
import json
import random
import hashlib
import base64
import socket
import requests
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
import logging

class AnonymityManager:
    """Gestisce tutte le funzionalità di anonimato e privacy"""
    
    def __init__(self, config_path="config.json"):
        self.config = self.load_config(config_path)
        self.anonymity_config = self.config.get("anonymity", {})
        self.logger = self.setup_logging()
        self.encryption_key = None
        self.current_proxy = None
        self.tor_enabled = False
        
    def load_config(self, config_path):
        """Carica configurazione"""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def setup_logging(self):
        """Setup logging anonimo"""
        logger = logging.getLogger("AnonymityManager")
        logger.setLevel(logging.INFO)
        return logger
    
    def generate_encryption_key(self, password):
        """Genera chiave di cifratura da password"""
        salt = b'social_reporter_salt_v1'  # In produzione, usa salt random
        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        self.encryption_key = key
        return Fernet(key)
    
    def encrypt_credentials(self, username, password, master_password):
        """Cifra le credenziali"""
        fernet = self.generate_encryption_key(master_password)
        credentials = json.dumps({"username": username, "password": password})
        encrypted = fernet.encrypt(credentials.encode())
        return base64.urlsafe_b64encode(encrypted).decode()
    
    def decrypt_credentials(self, encrypted_data, master_password):
        """Decifra le credenziali"""
        try:
            fernet = self.generate_encryption_key(master_password)
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_data.encode())
            decrypted = fernet.decrypt(encrypted_bytes)
            return json.loads(decrypted.decode())
        except:
            return None
    
    def save_encrypted_credentials(self, platform, username, password, master_password):
        """Salva credenziali cifrate"""
        creds_dir = Path("encrypted_credentials")
        creds_dir.mkdir(exist_ok=True)
        
        encrypted = self.encrypt_credentials(username, password, master_password)
        creds_file = creds_dir / f"{platform}_creds.enc"
        
        with open(creds_file, 'w') as f:
            f.write(encrypted)
        
        self.logger.info(f"Credenziali cifrate salvate per {platform}")
    
    def load_encrypted_credentials(self, platform, master_password):
        """Carica credenziali cifrate"""
        creds_file = Path("encrypted_credentials") / f"{platform}_creds.enc"
        
        if not creds_file.exists():
            return None
        
        with open(creds_file, 'r') as f:
            encrypted = f.read()
        
        return self.decrypt_credentials(encrypted, master_password)
    
    def get_tor_proxy(self):
        """Ottiene configurazione proxy Tor"""
        return {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
    
    def check_tor_connection(self):
        """Verifica se Tor è attivo"""
        try:
            proxies = self.get_tor_proxy()
            response = requests.get(
                'https://check.torproject.org/api/ip',
                proxies=proxies,
                timeout=10
            )
            data = response.json()
            if data.get('IsTor'):
                self.tor_enabled = True
                self.logger.info(f"✅ Tor connesso! IP: {data.get('IP')}")
                return True, data.get('IP')
            return False, None
        except Exception as e:
            self.logger.error(f"❌ Tor non disponibile: {e}")
            return False, None
    
    def get_proxy_list(self):
        """Carica lista proxy dal config o file"""
        proxy_list = self.anonymity_config.get("proxy_list", [])
        
        # Prova a caricare da file
        proxy_file = Path("proxies.txt")
        if proxy_file.exists():
            with open(proxy_file, 'r') as f:
                file_proxies = [line.strip() for line in f if line.strip()]
                proxy_list.extend(file_proxies)
        
        return list(set(proxy_list))  # Rimuovi duplicati
    
    def validate_proxy(self, proxy):
        """Valida un proxy"""
        try:
            proxies = {
                'http': proxy,
                'https': proxy
            }
            response = requests.get(
                'https://httpbin.org/ip',
                proxies=proxies,
                timeout=10
            )
            if response.status_code == 200:
                ip = response.json().get('origin')
                self.logger.info(f"✅ Proxy valido: {proxy} (IP: {ip})")
                return True, ip
            return False, None
        except Exception as e:
            self.logger.warning(f"❌ Proxy non valido: {proxy}")
            return False, None
    
    def get_random_proxy(self, validate=True):
        """Ottiene un proxy random dalla lista"""
        proxies = self.get_proxy_list()
        
        if not proxies:
            self.logger.warning("Nessun proxy disponibile")
            return None
        
        random.shuffle(proxies)
        
        for proxy in proxies:
            if validate:
                valid, ip = self.validate_proxy(proxy)
                if valid:
                    self.current_proxy = proxy
                    return proxy
            else:
                self.current_proxy = proxy
                return proxy
        
        return None
    
    def rotate_proxy(self):
        """Ruota il proxy corrente"""
        new_proxy = self.get_random_proxy(validate=True)
        if new_proxy:
            self.logger.info(f"🔄 Proxy ruotato: {new_proxy}")
            return new_proxy
        return None
    
    def get_random_user_agent(self):
        """Genera user agent random realistico"""
        user_agents = [
            # Chrome Windows
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            # Chrome Mac
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            # Chrome Linux
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            # Firefox
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
            # Safari
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
            # Edge
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        ]
        return random.choice(user_agents)
    
    def get_random_screen_resolution(self):
        """Genera risoluzione schermo random"""
        resolutions = [
            (1920, 1080), (1366, 768), (1440, 900), (1536, 864),
            (1280, 720), (1600, 900), (2560, 1440), (1920, 1200)
        ]
        return random.choice(resolutions)
    
    def get_random_timezone(self):
        """Genera timezone random"""
        timezones = [
            "America/New_York", "America/Los_Angeles", "America/Chicago",
            "Europe/London", "Europe/Paris", "Europe/Berlin",
            "Asia/Tokyo", "Asia/Shanghai", "Asia/Dubai",
            "Australia/Sydney", "America/Toronto"
        ]
        return random.choice(timezones)
    
    def get_random_language(self):
        """Genera lingua random"""
        languages = [
            "en-US,en;q=0.9",
            "en-GB,en;q=0.9",
            "it-IT,it;q=0.9,en;q=0.8",
            "es-ES,es;q=0.9,en;q=0.8",
            "fr-FR,fr;q=0.9,en;q=0.8",
            "de-DE,de;q=0.9,en;q=0.8"
        ]
        return random.choice(languages)
    
    def generate_fingerprint(self):
        """Genera fingerprint browser completo"""
        width, height = self.get_random_screen_resolution()
        
        fingerprint = {
            "user_agent": self.get_random_user_agent(),
            "screen_resolution": f"{width}x{height}",
            "color_depth": random.choice([24, 32]),
            "timezone": self.get_random_timezone(),
            "language": self.get_random_language(),
            "platform": random.choice(["Win32", "MacIntel", "Linux x86_64"]),
            "hardware_concurrency": random.choice([2, 4, 6, 8, 12, 16]),
            "device_memory": random.choice([4, 8, 16, 32]),
            "do_not_track": random.choice(["1", None]),
            "canvas_fingerprint": self.generate_canvas_fingerprint(),
            "webgl_vendor": random.choice(["Google Inc.", "Intel Inc.", "NVIDIA Corporation"]),
            "webgl_renderer": random.choice([
                "ANGLE (Intel, Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0)",
                "ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 Direct3D11 vs_5_0 ps_5_0)",
                "ANGLE (AMD, AMD Radeon RX 580 Direct3D11 vs_5_0 ps_5_0)"
            ])
        }
        
        return fingerprint
    
    def generate_canvas_fingerprint(self):
        """Genera canvas fingerprint random"""
        return hashlib.md5(str(random.random()).encode()).hexdigest()
    
    def get_chrome_options_anonymous(self, use_tor=False, use_proxy=None):
        """Ottiene Chrome options per massimo anonimato"""
        from selenium.webdriver.chrome.options import Options
        
        options = Options()
        fingerprint = self.generate_fingerprint()
        
        # User Agent
        options.add_argument(f'user-agent={fingerprint["user_agent"]}')
        
        # Window size
        width, height = fingerprint["screen_resolution"].split('x')
        options.add_argument(f'--window-size={width},{height}')
        
        # Anti-detection
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Privacy
        options.add_argument('--disable-web-security')
        options.add_argument('--disable-features=IsolateOrigins,site-per-process')
        options.add_argument('--disable-site-isolation-trials')
        
        # Fingerprint protection
        options.add_argument(f'--lang={fingerprint["language"].split(",")[0]}')
        options.add_argument('--disable-webgl')  # Opzionale
        options.add_argument('--disable-canvas-fingerprinting')
        
        # DNS
        options.add_argument('--host-resolver-rules="MAP * ~NOTFOUND , EXCLUDE localhost"')
        
        # WebRTC leak prevention
        options.add_experimental_option("prefs", {
            "webrtc.ip_handling_policy": "disable_non_proxied_udp",
            "webrtc.multiple_routes_enabled": False,
            "webrtc.nonproxied_udp_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.media_stream": 2,
            "profile.managed_default_content_settings.images": 1
        })
        
        # Tor support
        if use_tor:
            options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
        
        # Proxy support
        elif use_proxy:
            options.add_argument(f'--proxy-server={use_proxy}')
        
        return options, fingerprint
    
    def check_ip_leak(self):
        """Controlla leak IP"""
        try:
            # Check IP normale
            response = requests.get('https://api.ipify.org?format=json', timeout=10)
            real_ip = response.json().get('ip')
            
            # Check IP con proxy/tor se attivo
            if self.current_proxy or self.tor_enabled:
                proxies = self.get_tor_proxy() if self.tor_enabled else {
                    'http': self.current_proxy,
                    'https': self.current_proxy
                }
                response = requests.get(
                    'https://api.ipify.org?format=json',
                    proxies=proxies,
                    timeout=10
                )
                proxy_ip = response.json().get('ip')
                
                if real_ip == proxy_ip:
                    self.logger.warning(f"⚠️ IP LEAK DETECTED! Real IP: {real_ip}")
                    return False, real_ip
                else:
                    self.logger.info(f"✅ No IP leak. Proxy IP: {proxy_ip}")
                    return True, proxy_ip
            
            return True, real_ip
        except Exception as e:
            self.logger.error(f"Errore check IP: {e}")
            return False, None
    
    def check_dns_leak(self):
        """Controlla DNS leak"""
        try:
            # Usa servizio DNS leak test
            response = requests.get('https://www.dnsleaktest.com/api/v1/test', timeout=10)
            if response.status_code == 200:
                self.logger.info("✅ DNS leak test completato")
                return True
            return False
        except:
            return False
    
    def get_anonymity_score(self):
        """Calcola score anonimato (0-100)"""
        score = 0
        
        # Tor attivo: +40
        if self.tor_enabled:
            score += 40
        
        # Proxy attivo: +30
        elif self.current_proxy:
            score += 30
        
        # Fingerprint randomization: +20
        score += 20
        
        # Encrypted credentials: +10
        if Path("encrypted_credentials").exists():
            score += 10
        
        # No IP leak: +10
        no_leak, _ = self.check_ip_leak()
        if no_leak:
            score += 10
        
        return min(score, 100)
    
    def print_anonymity_status(self):
        """Stampa stato anonimato"""
        from colorama import Fore, Style
        
        print(Fore.CYAN + "\n" + "="*70)
        print(Fore.YELLOW + Style.BRIGHT + "🛡️  ANONYMITY STATUS")
        print(Fore.CYAN + "="*70)
        
        # Tor
        if self.tor_enabled:
            print(Fore.GREEN + "✅ Tor: ATTIVO")
        else:
            print(Fore.RED + "❌ Tor: NON ATTIVO")
        
        # Proxy
        if self.current_proxy:
            print(Fore.GREEN + f"✅ Proxy: {self.current_proxy}")
        else:
            print(Fore.YELLOW + "⚠️  Proxy: NON CONFIGURATO")
        
        # IP check
        no_leak, ip = self.check_ip_leak()
        if no_leak:
            print(Fore.GREEN + f"✅ IP Attuale: {ip}")
        else:
            print(Fore.RED + f"⚠️  IP LEAK: {ip}")
        
        # Score
        score = self.get_anonymity_score()
        if score >= 80:
            color = Fore.GREEN
        elif score >= 50:
            color = Fore.YELLOW
        else:
            color = Fore.RED
        
        print(color + f"\n🎯 Anonymity Score: {score}/100")
        print(Fore.CYAN + "="*70 + "\n")
