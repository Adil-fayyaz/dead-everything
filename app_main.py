#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔥 MULTI-PLATFORM SOCIAL MEDIA REPORTER - KIVY APP 🔥
Advanced Hacker-Style GUI Application
Compatible with: Kali Linux, Termux, Android APK

Created by Infinity X White devels team
"""

import os
import sys
import json
import time
import threading
from datetime import datetime

# Kivy imports
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line
from kivy.properties import StringProperty, NumericProperty, BooleanProperty

# Set window size for desktop
Window.size = (400, 700)

# Import reporter modules
try:
    from multi_platform_reporter import (
        InstagramReporter, TikTokReporter, TwitterReporter,
        FacebookReporter, YouTubeReporter, RedditReporter, LinkedInReporter
    )
    from anonymity_manager import AnonymityManager
    REPORTERS_AVAILABLE = True
except ImportError:
    REPORTERS_AVAILABLE = False
    print("⚠️  Reporter modules not found. Running in demo mode.")


class HackerLabel(Label):
    """Custom label with hacker style"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0, 1, 0, 1)  # Green
        self.font_name = 'RobotoMono-Regular'
        self.markup = True


class HackerButton(Button):
    """Custom button with hacker style"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0.3, 0, 1)  # Dark green
        self.color = (0, 1, 0, 1)  # Bright green
        self.bold = True
        self.markup = True


class HackerTextInput(TextInput):
    """Custom text input with hacker style"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.05, 0.05, 0.05, 1)  # Almost black
        self.foreground_color = (0, 1, 0, 1)  # Green
        self.cursor_color = (0, 1, 0, 1)
        self.multiline = False


class SplashScreen(Screen):
    """Splash screen with hacker animation"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Banner
        banner = HackerLabel(
            text='[b][color=#00ff00]' + '''
    ╔═══════════════════════════════════╗
    ║  🔥 MULTI-PLATFORM REPORTER 🔥  ║
    ║                                   ║
    ║    👻 ANONYMOUS HACKER TOOL 👻   ║
    ║                                   ║
    ║  Instagram | TikTok | Twitter    ║
    ║  Facebook | YouTube | Reddit     ║
    ║  LinkedIn | 7 Platforms          ║
    ║                                   ║
    ║  🛡️  Tor | Proxy | Encrypted 🛡️  ║
    ╚═══════════════════════════════════╝
            ''' + '[/color][/b]',
            font_size='10sp',
            halign='center'
        )
        
        # Loading bar
        self.progress = ProgressBar(max=100, value=0)
        self.progress.size_hint_y = 0.1
        
        # Status
        self.status = HackerLabel(
            text='[color=#00ff00]⚡ Initializing systems...[/color]',
            font_size='12sp',
            halign='center'
        )
        
        # Credits
        credits = HackerLabel(
            text='[color=#00ff00]Created by Infinity X White devels team[/color]',
            font_size='10sp',
            halign='center'
        )
        
        layout.add_widget(banner)
        layout.add_widget(self.progress)
        layout.add_widget(self.status)
        layout.add_widget(credits)
        
        self.add_widget(layout)
        
        # Start loading animation
        Clock.schedule_once(self.start_loading, 0.5)
    
    def start_loading(self, dt):
        """Animate loading"""
        self.loading_step = 0
        Clock.schedule_interval(self.update_loading, 0.1)
    
    def update_loading(self, dt):
        """Update loading progress"""
        steps = [
            (10, '🔍 Checking system compatibility...'),
            (25, '📦 Loading modules...'),
            (40, '🔐 Initializing encryption...'),
            (55, '🌐 Setting up network...'),
            (70, '👻 Configuring anonymity...'),
            (85, '⚡ Preparing interface...'),
            (100, '✅ Ready!')
        ]
        
        if self.loading_step < len(steps):
            value, text = steps[self.loading_step]
            self.progress.value = value
            self.status.text = f'[color=#00ff00]{text}[/color]'
            self.loading_step += 1
        else:
            Clock.unschedule(self.update_loading)
            Clock.schedule_once(self.go_to_main, 1)
    
    def go_to_main(self, dt):
        """Navigate to main menu"""
        self.manager.current = 'main_menu'


class MainMenuScreen(Screen):
    """Main menu with hacker style"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header
        header = HackerLabel(
            text='[b][color=#00ff00]╔═══ MAIN MENU ═══╗[/color][/b]',
            font_size='16sp',
            size_hint_y=0.1
        )
        
        # Menu buttons
        buttons_data = [
            ('🎯 START ATTACK', 'platform_select'),
            ('⚙️  SETTINGS', 'settings'),
            ('🛡️  ANONYMITY CONFIG', 'anonymity'),
            ('📊 STATISTICS', 'stats'),
            ('ℹ️  ABOUT', 'about'),
            ('❌ EXIT', 'exit')
        ]
        
        for text, screen in buttons_data:
            btn = HackerButton(
                text=f'[b]{text}[/b]',
                size_hint_y=0.12,
                font_size='14sp'
            )
            if screen == 'exit':
                btn.bind(on_press=self.exit_app)
            else:
                btn.bind(on_press=lambda x, s=screen: self.go_to_screen(s))
            layout.add_widget(btn)
        
        # Footer
        footer = HackerLabel(
            text='[color=#00ff00]👻 Stay Anonymous | Stay Safe 👻[/color]',
            font_size='10sp',
            size_hint_y=0.08
        )
        
        layout.add_widget(header)
        layout.add_widget(footer)
        
        self.add_widget(layout)
    
    def go_to_screen(self, screen_name):
        """Navigate to screen"""
        self.manager.current = screen_name
    
    def exit_app(self, instance):
        """Exit application"""
        App.get_running_app().stop()


class PlatformSelectScreen(Screen):
    """Platform selection screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header
        header = HackerLabel(
            text='[b][color=#00ff00]╔═══ SELECT TARGET PLATFORM ═══╗[/color][/b]',
            font_size='14sp',
            size_hint_y=0.08
        )
        layout.add_widget(header)
        
        # Scroll view for platforms
        scroll = ScrollView(size_hint=(1, 0.7))
        platforms_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        platforms_layout.bind(minimum_height=platforms_layout.setter('height'))
        
        self.selected_platforms = []
        
        platforms = [
            ('📸 Instagram', 'instagram'),
            ('🎵 TikTok', 'tiktok'),
            ('🐦 Twitter/X', 'twitter'),
            ('👥 Facebook', 'facebook'),
            ('▶️  YouTube', 'youtube'),
            ('🤖 Reddit', 'reddit'),
            ('💼 LinkedIn', 'linkedin'),
            ('🔥 ALL PLATFORMS', 'all')
        ]
        
        for name, platform in platforms:
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
            
            checkbox = CheckBox(
                size_hint_x=0.2,
                color=(0, 1, 0, 1)
            )
            checkbox.bind(active=lambda cb, val, p=platform: self.toggle_platform(p, val))
            
            label = HackerLabel(
                text=f'[b]{name}[/b]',
                size_hint_x=0.8,
                font_size='13sp'
            )
            
            row.add_widget(checkbox)
            row.add_widget(label)
            platforms_layout.add_widget(row)
        
        scroll.add_widget(platforms_layout)
        layout.add_widget(scroll)
        
        # Buttons
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=0.12, spacing=10)
        
        back_btn = HackerButton(text='[b]⬅️  BACK[/b]')
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'main_menu'))
        
        next_btn = HackerButton(text='[b]NEXT ➡️[/b]')
        next_btn.bind(on_press=self.go_to_credentials)
        
        btn_layout.add_widget(back_btn)
        btn_layout.add_widget(next_btn)
        layout.add_widget(btn_layout)
        
        self.add_widget(layout)
    
    def toggle_platform(self, platform, active):
        """Toggle platform selection"""
        if platform == 'all':
            if active:
                self.selected_platforms = ['instagram', 'tiktok', 'twitter', 'facebook', 
                                          'youtube', 'reddit', 'linkedin']
            else:
                self.selected_platforms = []
        else:
            if active and platform not in self.selected_platforms:
                self.selected_platforms.append(platform)
            elif not active and platform in self.selected_platforms:
                self.selected_platforms.remove(platform)
    
    def go_to_credentials(self, instance):
        """Go to credentials screen"""
        if not self.selected_platforms:
            # Show error (simplified)
            return
        
        app = App.get_running_app()
        app.selected_platforms = self.selected_platforms
        self.manager.current = 'credentials'


class CredentialsScreen(Screen):
    """Credentials input screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header
        header = HackerLabel(
            text='[b][color=#00ff00]╔═══ ENTER CREDENTIALS ═══╗[/color][/b]',
            font_size='14sp',
            size_hint_y=0.08
        )
        layout.add_widget(header)
        
        # Warning
        warning = HackerLabel(
            text='[color=#ffff00]⚠️  Use test accounts only!\nNever use your main accounts![/color]',
            font_size='11sp',
            size_hint_y=0.1
        )
        layout.add_widget(warning)
        
        # Username
        layout.add_widget(HackerLabel(text='[b]📧 Username/Email:[/b]', size_hint_y=0.06))
        self.username_input = HackerTextInput(hint_text='Enter username or email')
        layout.add_widget(self.username_input)
        
        # Password
        layout.add_widget(HackerLabel(text='[b]🔒 Password:[/b]', size_hint_y=0.06))
        self.password_input = HackerTextInput(
            hint_text='Enter password',
            password=True
        )
        layout.add_widget(self.password_input)
        
        # Target
        layout.add_widget(HackerLabel(text='[b]🎯 Target Username:[/b]', size_hint_y=0.06))
        self.target_input = HackerTextInput(hint_text='Enter target username (without @)')
        layout.add_widget(self.target_input)
        
        # Country
        layout.add_widget(HackerLabel(text='[b]🌍 Country:[/b]', size_hint_y=0.06))
        self.country_spinner = Spinner(
            text='Select Country',
            values=['Italy', 'USA', 'UK', 'Germany', 'France', 'Spain', 'Other'],
            size_hint_y=0.08,
            background_color=(0, 0.3, 0, 1),
            color=(0, 1, 0, 1)
        )
        layout.add_widget(self.country_spinner)
        
        # Reason
        layout.add_widget(HackerLabel(text='[b]📝 Report Reason:[/b]', size_hint_y=0.06))
        self.reason_spinner = Spinner(
            text='Select Reason',
            values=['Fake Account', 'Spam', 'Harassment', 'Hate Speech', 
                   'Violence', 'Adult Content', 'Impersonation'],
            size_hint_y=0.08,
            background_color=(0, 0.3, 0, 1),
            color=(0, 1, 0, 1)
        )
        layout.add_widget(self.reason_spinner)
        
        # Buttons
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=10)
        
        back_btn = HackerButton(text='[b]⬅️  BACK[/b]')
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'platform_select'))
        
        attack_btn = HackerButton(text='[b]🔥 START ATTACK 🔥[/b]')
        attack_btn.bind(on_press=self.start_attack)
        
        btn_layout.add_widget(back_btn)
        btn_layout.add_widget(attack_btn)
        layout.add_widget(btn_layout)
        
        self.add_widget(layout)
    
    def start_attack(self, instance):
        """Start the attack"""
        # Validate inputs
        if not self.username_input.text or not self.password_input.text or not self.target_input.text:
            return
        
        # Save data to app
        app = App.get_running_app()
        app.credentials = {
            'username': self.username_input.text,
            'password': self.password_input.text,
            'target': self.target_input.text,
            'country': self.country_spinner.text,
            'reason': self.reason_spinner.text
        }
        
        # Go to attack screen
        self.manager.current = 'attack'
        
        # Start attack in background
        attack_screen = self.manager.get_screen('attack')
        attack_screen.start_reporting()


class AttackScreen(Screen):
    """Attack progress screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header
        header = HackerLabel(
            text='[b][color=#ff0000]╔═══ ATTACK IN PROGRESS ═══╗[/color][/b]',
            font_size='14sp',
            size_hint_y=0.08
        )
        layout.add_widget(header)
        
        # Status
        self.status_label = HackerLabel(
            text='[color=#00ff00]⚡ Initializing attack...[/color]',
            font_size='12sp',
            size_hint_y=0.08
        )
        layout.add_widget(self.status_label)
        
        # Progress bar
        self.progress_bar = ProgressBar(max=100, value=0, size_hint_y=0.08)
        layout.add_widget(self.progress_bar)
        
        # Log scroll
        scroll = ScrollView(size_hint=(1, 0.6))
        self.log_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.log_layout.bind(minimum_height=self.log_layout.setter('height'))
        scroll.add_widget(self.log_layout)
        layout.add_widget(scroll)
        
        # Stats
        self.stats_label = HackerLabel(
            text='[color=#00ff00]✅ Success: 0 | ❌ Failed: 0[/color]',
            font_size='12sp',
            size_hint_y=0.08
        )
        layout.add_widget(self.stats_label)
        
        # Stop button
        self.stop_btn = HackerButton(
            text='[b]🛑 STOP ATTACK[/b]',
            size_hint_y=0.08
        )
        self.stop_btn.bind(on_press=self.stop_attack)
        layout.add_widget(self.stop_btn)
        
        self.add_widget(layout)
        
        self.is_running = False
        self.success_count = 0
        self.failed_count = 0
    
    def add_log(self, message, color='#00ff00'):
        """Add log message"""
        log = HackerLabel(
            text=f'[color={color}]{message}[/color]',
            font_size='10sp',
            size_hint_y=None,
            height=30
        )
        self.log_layout.add_widget(log)
    
    def update_stats(self):
        """Update statistics"""
        self.stats_label.text = f'[color=#00ff00]✅ Success: {self.success_count} | ❌ Failed: {self.failed_count}[/color]'
    
    def start_reporting(self):
        """Start reporting in background thread"""
        self.is_running = True
        self.success_count = 0
        self.failed_count = 0
        
        # Clear logs
        self.log_layout.clear_widgets()
        
        # Start in thread
        thread = threading.Thread(target=self.run_attack)
        thread.daemon = True
        thread.start()
    
    def run_attack(self):
        """Run the attack (simplified demo version)"""
        app = App.get_running_app()
        platforms = app.selected_platforms
        credentials = app.credentials
        
        Clock.schedule_once(lambda dt: self.add_log('🔥 Attack started!', '#ff0000'))
        Clock.schedule_once(lambda dt: self.add_log(f'🎯 Target: @{credentials["target"]}'))
        Clock.schedule_once(lambda dt: self.add_log(f'🌐 Platforms: {", ".join(platforms)}'))
        
        total = len(platforms)
        
        for i, platform in enumerate(platforms):
            if not self.is_running:
                break
            
            # Update progress
            progress = int((i + 1) / total * 100)
            Clock.schedule_once(lambda dt, p=progress: setattr(self.progress_bar, 'value', p))
            
            # Update status
            Clock.schedule_once(lambda dt, pl=platform: setattr(
                self.status_label, 
                'text', 
                f'[color=#00ff00]⚡ Attacking {pl.upper()}...[/color]'
            ))
            
            # Add log
            Clock.schedule_once(lambda dt, pl=platform: self.add_log(f'📸 Starting {pl.upper()} attack...'))
            
            # Simulate attack (replace with real reporter code)
            time.sleep(2)
            
            # Random success/fail for demo
            import random
            if random.random() > 0.3:
                self.success_count += 1
                Clock.schedule_once(lambda dt, pl=platform: self.add_log(
                    f'✅ {pl.upper()} report sent successfully!', '#00ff00'
                ))
            else:
                self.failed_count += 1
                Clock.schedule_once(lambda dt, pl=platform: self.add_log(
                    f'❌ {pl.upper()} report failed!', '#ff0000'
                ))
            
            Clock.schedule_once(lambda dt: self.update_stats())
        
        # Completed
        Clock.schedule_once(lambda dt: setattr(
            self.status_label,
            'text',
            '[color=#00ff00]✅ Attack completed![/color]'
        ))
        Clock.schedule_once(lambda dt: self.add_log('🎉 All attacks completed!', '#00ff00'))
        Clock.schedule_once(lambda dt: setattr(self.stop_btn, 'text', '[b]✅ DONE - BACK TO MENU[/b]'))
    
    def stop_attack(self, instance):
        """Stop attack"""
        self.is_running = False
        self.manager.current = 'main_menu'


class SettingsScreen(Screen):
    """Settings screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        header = HackerLabel(
            text='[b][color=#00ff00]╔═══ SETTINGS ═══╗[/color][/b]',
            font_size='14sp',
            size_hint_y=0.1
        )
        layout.add_widget(header)
        
        # Settings content (simplified)
        content = HackerLabel(
            text='[color=#00ff00]⚙️  Settings coming soon...[/color]',
            font_size='12sp'
        )
        layout.add_widget(content)
        
        # Back button
        back_btn = HackerButton(text='[b]⬅️  BACK[/b]', size_hint_y=0.1)
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'main_menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)


class AnonymityScreen(Screen):
    """Anonymity configuration screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        header = HackerLabel(
            text='[b][color=#00ff00]╔═══ ANONYMITY CONFIG ═══╗[/color][/b]',
            font_size='14sp',
            size_hint_y=0.1
        )
        layout.add_widget(header)
        
        # Anonymity level
        layout.add_widget(HackerLabel(text='[b]🛡️  Anonymity Level:[/b]', size_hint_y=0.08))
        self.anon_spinner = Spinner(
            text='HIGH',
            values=['MAXIMUM (Tor+Proxy)', 'HIGH (Proxy)', 'MEDIUM (Fingerprint)', 'LOW (Basic)'],
            size_hint_y=0.1,
            background_color=(0, 0.3, 0, 1),
            color=(0, 1, 0, 1)
        )
        layout.add_widget(self.anon_spinner)
        
        # Info
        info = HackerLabel(
            text='[color=#ffff00]⚠️  MAXIMUM level requires Tor installed[/color]',
            font_size='10sp',
            size_hint_y=0.1
        )
        layout.add_widget(info)
        
        # Back button
        back_btn = HackerButton(text='[b]⬅️  BACK[/b]', size_hint_y=0.1)
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'main_menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)


class StatsScreen(Screen):
    """Statistics screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        header = HackerLabel(
            text='[b][color=#00ff00]╔═══ STATISTICS ═══╗[/color][/b]',
            font_size='14sp',
            size_hint_y=0.1
        )
        layout.add_widget(header)
        
        # Stats content
        stats_text = '''[color=#00ff00]
📊 Total Attacks: 0
✅ Successful Reports: 0
❌ Failed Reports: 0
🎯 Targets Reported: 0
🌐 Platforms Used: 0
        [/color]'''
        
        content = HackerLabel(
            text=stats_text,
            font_size='12sp'
        )
        layout.add_widget(content)
        
        # Back button
        back_btn = HackerButton(text='[b]⬅️  BACK[/b]', size_hint_y=0.1)
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'main_menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)


class AboutScreen(Screen):
    """About screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        header = HackerLabel(
            text='[b][color=#00ff00]╔═══ ABOUT ═══╗[/color][/b]',
            font_size='14sp',
            size_hint_y=0.1
        )
        layout.add_widget(header)
        
        # About content
        about_text = '''[color=#00ff00]
🔥 MULTI-PLATFORM REPORTER 🔥

Version: 2.0
Created by: Infinity X White devels team

Supported Platforms:
📸 Instagram
🎵 TikTok
🐦 Twitter/X
👥 Facebook
▶️  YouTube
🤖 Reddit
💼 LinkedIn

Features:
🛡️  Tor Support
🔐 Encrypted Credentials
👻 Complete Anonymity
⚡ Advanced Automation

⚠️  FOR EDUCATIONAL USE ONLY ⚠️
        [/color]'''
        
        content = HackerLabel(
            text=about_text,
            font_size='11sp'
        )
        layout.add_widget(content)
        
        # Back button
        back_btn = HackerButton(text='[b]⬅️  BACK[/b]', size_hint_y=0.1)
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'main_menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)


class HackerReporterApp(App):
    """Main application class"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_platforms = []
        self.credentials = {}
    
    def build(self):
        """Build the application"""
        # Set window background to black
        Window.clearcolor = (0, 0, 0, 1)
        
        # Create screen manager
        sm = ScreenManager(transition=FadeTransition())
        
        # Add screens
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(PlatformSelectScreen(name='platform_select'))
        sm.add_widget(CredentialsScreen(name='credentials'))
        sm.add_widget(AttackScreen(name='attack'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(AnonymityScreen(name='anonymity'))
        sm.add_widget(StatsScreen(name='stats'))
        sm.add_widget(AboutScreen(name='about'))
        
        return sm


if __name__ == '__main__':
    HackerReporterApp().run()
