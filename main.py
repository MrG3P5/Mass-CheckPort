#!/usr/bin/env python3
import socket
import sys
import os
import requests
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Color
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE
blue = Fore.LIGHTBLUE_EX
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX

init(autoreset=True)

try:
    open("result.txt", "a")
except:
    pass

def banner():
    os.system("cls||clear")
    __banner__ = f"""{red}
  ⣴⣶⣤⡤⠦⣤⣀⣤⠆      ⣈⣭⣭⣿⣶⣿⣦⣼⣆⠄
   ⠉⠻⢿⣿⠿⣿⣿⣶⣦⠤⠄⡠⢾⣿⣿⡿⠋⠉⠉⠻⣿⣿⡛⣦⠄
           ⠈⢿⣿⣟⠦⠄⣾⣿⣿⣷⠄⠄⠄⠄⠻⠿⢿⣿⣧⣄
            ⣸⣿⣿⢧ ⢻⠻⣿⣿⣷⣄⣀⠄⠢⣀⡀⠈⠙⠿
           ⢠⣿⣿⣿⠈  ⠡⠌⣻⣿⣿⣿⣿⣿⣿⣿⣛⣳⣤⣀⣀
   ⢠⣧⣶⣥⡤⢄⠄⣸⣿⣿   ⢀⣴⣿⣿⡿⠛⣿⣿⣧⠈⢿⠿⠟⠛⠻⠿⠄
 ⣰⣿⣿⠛⠻⣿⣿⡦⢹⣿⣷   ⢊⣿⣿⡏⠄⠄⢸⣿⣿⡇⠄⢀⣠⣄⣾⠄     {cyan}[ {white}MASS AUTO CHECK PORT 80 & 443 {cyan}]
{red}⣠⣿⠿⠛  ⣿⣿⣷⠘⢿⣿⣦⡀ ⢸⢿⣿⣿⣄⠄⣸⣿⣿⡇⣪⣿⡿⠿⣿⣷⡄      {cyan}[ {white}Created By X-MrG3P5 {cyan}]
{red}⠙⠃    ⣼⣿⡟⠌ ⠈⠻⣿⣿⣦⣌⡇⠻⣿⣿⣷⣿⣿⣿⠐⣿⣿⡇⠄⠛⠻⢷⣄
      ⢻⣿⣿⣄⠄  ⠈⠻⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟⠄⠫⢿⣿⡆    
       ⠻⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣀⣤⣾⡿⠃"""
    print(__banner__ + "\n")

def CheckPort443(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        check = sock.connect_ex((ip, 443))

        if check == 0:
            test_req = requests.get(f"https://{ip}:443", verify=False, timeout=5)

            if test_req.status_code == 200:
                if ip in open("result.txt", "r").read():
                    pass
                else:
                    sys.stdout.write(f"\n{white}---> {blue}{ip} {white}PORT {green}443 {white}OPEN!")
                    open("result.txt", "a").write(f"https://{ip}:443\n")
            else:
                sys.stdout.write(f"\n{white}---> {blue}{ip} {white}PORT {red}443 {white}CLOSED!")
        else:
            sys.stdout.write(f"\n{white}---> {blue}{ip} {white}PORT {red}443 {white}CLOSED!")
    except:
        sys.stdout.write(f"\n{white}---> {blue}{ip} {white}PORT {red}443 {white}CLOSED!")

def CheckPort80(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        check = sock.connect_ex((ip, 80))

        if check == 0:
            test_req = requests.get(f"http://{ip}:80", verify=False, timeout=5)

            if test_req.status_code == 200:
                if ip in open("result.txt", "r").read():
                    pass
                else:
                    sys.stdout.write(f"\n{white}---> {blue}{ip} {white}PORT {green}80 {white}OPEN!")
                    open("result.txt", "a").write(f"http://{ip}:80\n")
            else:
                sys.stdout.write(f"\n{white}---> {blue}{ip} {white}PORT {red}80 {white}CLOSED!")
        else:
            sys.stdout.write(f"\n{white}---> {blue}{ip} {white}PORT {red}80 {white}CLOSED!")
    except:
        sys.stdout.write(f"\n{white}---> {blue}{ip} {white}PORT {red}80 {white}CLOSED!")

def PortChecker(ip):
    try:
        ip = ip.strip("\r\n")

        CheckPort80(ip)
        CheckPort443(ip)
    except:
        pass

if __name__=="__main__":
    banner()
    input_list = open(input(f"{red}[{white}?{red}] {white}Give Me List : ")).readlines()
    Thread = input(f"{red}[{white}?{red}] {white}Thread : ")
    pool = ThreadPool(int(Thread))
    pool.map(PortChecker, input_list)
    pool.close()
    pool.join()
    sys.stdout.write(f"\n{white}---> DONE!")
