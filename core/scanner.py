import subprocess
import time
import os
from colorama import Fore, Style

class SQLScanner:
    def __init__(self, sqlmap_path):
        self.sqlmap_path = sqlmap_path
    
    def scan(self, target):
        print(f"{Fore.CYAN}[*] Scanning: {target}{Style.RESET_ALL}")
        
        if not os.path.exists(self.sqlmap_path):
            print(f"{Fore.RED}[!] SQLMap not found at: {self.sqlmap_path}{Style.RESET_ALL}")
            return
        
        cmd = [
            "python3", self.sqlmap_path,
            "-u", target,
            "--batch",
            "--random-agent",
            "--level=3",
            "--risk=2",
            "--output-dir=logs/scans"
        ]
        
        try:
            print(f"{Fore.YELLOW}[+] Executing SQLMap...{Style.RESET_ALL}")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            # Save detailed log
            log_file = f"logs/scans/scan_{int(time.time())}.log"
            with open(log_file, 'w') as f:
                f.write(f"Target: {target}\n")
                f.write(f"Time: {time.ctime()}\n")
                f.write(f"Command: {' '.join(cmd)}\n")
                f.write("="*50 + "\n")
                f.write(result.stdout)
            
            print(f"{Fore.GREEN}[✓] Scan completed{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Log saved: {log_file}{Style.RESET_ALL}")
            
            if "sqlmap identified" in result.stdout.lower():
                print(f"{Fore.GREEN}[✓] VULNERABILITY DETECTED!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[✗] No SQL injection found{Style.RESET_ALL}")
                
        except subprocess.TimeoutExpired:
            print(f"{Fore.RED}[!] Scan timeout (5 minutes){Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
