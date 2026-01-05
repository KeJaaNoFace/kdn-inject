import requests
import threading
import time
from colorama import Fore, Style

class AdminFinder:
    def __init__(self):
        self.common_paths = [
            "/admin", "/wp-admin", "/administrator", "/login",
            "/admin.php", "/admin/login", "/admincp", "/moderator",
            "/user/login", "/backend", "/console", "/panel",
            "/cpanel", "/webadmin", "/phpmyadmin", "/mysql",
            "/dbadmin", "/sqladmin", "/webdav", "/server-status",
            "/manager", "/system", "/config", "/setup"
        ]
        self.found = []
    
    def scan(self, base_url):
        print(f"{Fore.CYAN}[*] Scanning admin panels: {base_url}{Style.RESET_ALL}")
        
        self.found = []
        threads = []
        
        def check_path(path):
            url = base_url.rstrip('/') + path
            try:
                r = requests.get(url, timeout=5, allow_redirects=False)
                if r.status_code in [200, 301, 302, 403, 401]:
                    self.found.append({
                        'url': url,
                        'status': r.status_code,
                        'title': self.extract_title(r.text) if r.status_code == 200 else 'N/A'
                    })
            except:
                pass
        
        # Create threads
        for path in self.common_paths:
            t = threading.Thread(target=check_path, args=(path,))
            threads.append(t)
            t.start()
        
        # Wait for completion
        for t in threads:
            t.join()
        
        # Display results
        self.display_results()
    
    def extract_title(self, html):
        """Extract page title from HTML"""
        try:
            start = html.find('<title>') + 7
            end = html.find('</title>', start)
            return html[start:end].strip()[:50]
        except:
            return "No title"
    
    def display_results(self):
        """Display found admin panels"""
        if self.found:
            print(f"\n{Fore.GREEN}[✓] Found {len(self.found)} admin panels:{Style.RESET_ALL}")
            for item in self.found:
                status_color = Fore.GREEN if item['status'] == 200 else Fore.YELLOW
                print(f"  {status_color}{item['status']}{Style.RESET_ALL} {item['url']}")
                if item['title'] != 'N/A':
                    print(f"     Title: {item['title']}")
        else:
            print(f"{Fore.RED}[✗] No admin panels found{Style.RESET_ALL}")
        
        # Save results
        if self.found:
            import json
            import time
            log_file = f"logs/attacks/admin_found_{int(time.time())}.json"
            with open(log_file, 'w') as f:
                json.dump(self.found, f, indent=2)
            print(f"{Fore.YELLOW}[*] Results saved: {log_file}{Style.RESET_ALL}")
