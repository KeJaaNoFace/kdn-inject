#!/usr/bin/env python3
"""
KDN INJECT Setup Script
Run this first: python3 setup.py
"""

import os
import sys
import subprocess
import platform
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}
╔══════════════════════════════════════════════════════╗
║                                                      ║
║          KDN INJECT v2.0 - SETUP WIZARD             ║
║          Created by: KeJaaDarkNet                   ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
{Style.RESET_ALL}
    """
    print(banner)

def check_os():
    """Check operating system"""
    system = platform.system().lower()
    print(f"{Fore.YELLOW}[*] Detected OS: {system}{Style.RESET_ALL}")
    return system

def install_dependencies(os_name):
    """Install system dependencies"""
    print(f"{Fore.YELLOW}[*] Installing system dependencies...{Style.RESET_ALL}")
    
    try:
        if os_name == "linux":
            # Check distro
            if os.path.exists("/etc/debian_version"):
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "python3", "python3-pip", "git"], check=True)
                print(f"{Fore.GREEN}[✓] Debian/Ubuntu packages installed{Style.RESET_ALL}")
            elif os.path.exists("/etc/redhat-release"):
                subprocess.run(["sudo", "yum", "install", "-y", "python3", "python3-pip", "git"], check=True)
                print(f"{Fore.GREEN}[✓] RHEL/CentOS packages installed{Style.RESET_ALL}")
            elif os.path.exists("/etc/arch-release"):
                subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "python", "python-pip", "git"], check=True)
                print(f"{Fore.GREEN}[✓] Arch Linux packages installed{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error installing packages: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Please install manually: python3, pip3, git{Style.RESET_ALL}")

def install_python_packages():
    """Install Python packages"""
    print(f"{Fore.YELLOW}[*] Installing Python packages...{Style.RESET_ALL}")
    
    packages = ["requests", "colorama", "beautifulsoup4", "paramiko"]
    
    try:
        for package in packages:
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            print(f"{Fore.GREEN}[✓] Installed: {package}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Try: pip3 install {' '.join(packages)}{Style.RESET_ALL}")

def clone_sqlmap():
    """Clone SQLMap repository"""
    print(f"{Fore.YELLOW}[*] Installing SQLMap...{Style.RESET_ALL}")
    
    sqlmap_dir = "bin/sqlmap"
    if not os.path.exists(sqlmap_dir):
        try:
            subprocess.run(["git", "clone", "--depth", "1", "https://github.com/sqlmapproject/sqlmap.git", sqlmap_dir], check=True)
            print(f"{Fore.GREEN}[✓] SQLMap cloned successfully{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error cloning SQLMap: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Manual download: github.com/sqlmapproject/sqlmap{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[✓] SQLMap already exists{Style.RESET_ALL}")

def create_directory_structure():
    """Create directory structure"""
    print(f"{Fore.YELLOW}[*] Creating directory structure...{Style.RESET_ALL}")
    
    directories = [
        "core",
        "templates",
        "config",
        "logs/scans",
        "logs/dumps",
        "logs/attacks",
        "output",
        "bin"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"{Fore.GREEN}[✓] Created: {directory}{Style.RESET_ALL}")
    
    # Create template README
    with open("templates/README.txt", "w") as f:
        f.write("Place your HTML deface files here.\n")
        f.write("Files should have .html extension.\n")
        f.write("The tool will list them for selection.\n")

def create_config():
    """Create configuration file"""
    print(f"{Fore.YELLOW}[*] Creating configuration...{Style.RESET_ALL}")
    
    config = {
        "sqlmap_path": "bin/sqlmap/sqlmap.py",
        "timeout": 30,
        "user_agent": "KDN-INJECT/2.0",
        "github_repo": "https://github.com/KeJaaNoFace/kdn-inject"
    }
    
    import json
    with open("config/settings.json", "w") as f:
        json.dump(config, f, indent=4)
    
    print(f"{Fore.GREEN}[✓] Config file created{Style.RESET_ALL}")

def make_executable():
    """Make main script executable"""
    if os.path.exists("kdn.py"):
        os.chmod("kdn.py", 0o755)
        print(f"{Fore.GREEN}[✓] Made kdn.py executable{Style.RESET_ALL}")

def main():
    """Main setup function"""
    print_banner()
    
    print(f"{Fore.CYAN}[*] Starting KDN INJECT setup...{Style.RESET_ALL}")
    
    # Check OS
    os_name = check_os()
    
    # Install dependencies
    install_dependencies(os_name)
    
    # Install Python packages
    install_python_packages()
    
    # Create directories
    create_directory_structure()
    
    # Clone SQLMap
    clone_sqlmap()
    
    # Create config
    create_config()
    
    # Make executable
    make_executable()
    
    # Final message
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] SETUP COMPLETED SUCCESSFULLY!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}[*] NEXT STEPS:{Style.RESET_ALL}")
    print(f"1. Add your HTML files to 'templates/' folder")
    print(f"2. Run the tool: {Fore.CYAN}python3 kdn.py{Style.RESET_ALL}")
    print(f"3. Or: {Fore.CYAN}./kdn.py{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}[*] GITHUB DEPLOYMENT:{Style.RESET_ALL}")
    print(f"Upload this folder to GitHub")
    print(f"Users can install with:")
    print(f"  git clone https://github.com/KeJaaNoFace/kdn-inject")
    print(f"  cd kdn-inject")
    print(f"  python3 setup.py")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Setup interrupted{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}[!] Setup failed: {e}{Style.RESET_ALL}")
        sys.exit(1)
