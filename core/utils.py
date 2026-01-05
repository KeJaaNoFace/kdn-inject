import os
import json
import hashlib
from colorama import Fore, Style

def save_log(data, filename):
    """Save data to log file"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w') as f:
        if isinstance(data, dict):
            json.dump(data, f, indent=2)
        else:
            f.write(str(data))
    
    return filename

def get_file_hash(filename):
    """Get MD5 hash of file"""
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    return None

def check_internet():
    """Check internet connection"""
    try:
        import requests
        requests.get("https://google.com", timeout=5)
        return True
    except:
        return False

def print_status(message, status="info"):
    """Print colored status message"""
    colors = {
        "info": Fore.CYAN,
        "success": Fore.GREEN,
        "warning": Fore.YELLOW,
        "error": Fore.RED
    }
    
    color = colors.get(status, Fore.WHITE)
    print(f"{color}[{status.upper()}] {message}{Style.RESET_ALL}")
