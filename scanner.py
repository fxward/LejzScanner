import requests, subprocess, socket
import datetime
from colorama import Fore

w = Fore.WHITE
cy = Fore.CYAN
r = Fore.RED
blck = Fore.BLACK
now = datetime.datetime.now()

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

def public_ip():
    r = requests.get("https://icanhazip.com")
    if r.status_code == 200:
        return r.text.strip()
    else:
        return f"{w}[{cy}LejzScanner{w}] {blck}- {r}No Internet or Web is offline"

def get_ssid():
    try:
        result = subprocess.run(['iwgetid', '--raw'], capture_output=True, text=True, check=True)
        ssid = result.stdout.strip()
        return ssid
    except subprocess.CalledProcessError as e:
        print(f"{w}[{cy}LejzScanner{w}] {blck}- {r} Error While Getting SSID Name: {e}")
        return None

def get_privateip():
    try:
        hostname = socket.gethostname()
        private_ip = socket.gethostbyname(hostname)
        return private_ip
    except Exception as e:
        print(f"{w}[{cy}LejzScanner{w}] {blck}- {r} Error While Getting Priv IP: {e}")
        return None

ssid = get_ssid()
myip = public_ip()
privateip = get_privateip()


def lejzscanner():
    with open("wifi_history.txt", "a") as f:
        f.write(f"""
========{ssid}========
Public: {myip}
Private: {privateip}
Date: {hour}:{minute} - {day}.{month}.{year}
\n""")
        
if __name__ == "__main__":
    lejzscanner()