from colorama import Fore, Back, Style
from dechiffrement import fromage_de_bite, couille,couillevide
from random import random
import sys, time, threading, requests, os ,base64
os.system("cls")
def printlent(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0001)
    sys.stdout.write("\n")
banner = """
 ▄████▄   ▄▄▄       ██▓     ██▓ ██▓███    ██████  ▒█████  
▒██▀ ▀█  ▒████▄    ▓██▒    ▓██▒▓██░  ██▒▒██    ▒ ▒██▒  ██▒
▒▓█    ▄ ▒██  ▀█▄  ▒██░    ▒██▒▓██░ ██▓▒░ ▓██▄   ▒██░  ██▒
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    ░██░▒██▄█▓▒ ▒  ▒   ██▒▒██   ██░
▒ ▓███▀ ░ ▓█   ▓██▒░██████▒░██░▒██▒ ░  ░▒██████▒▒░ ████▓▒░
░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░░▓  ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ 
  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░░▒ ░     ░ ░▒  ░ ░  ░ ▒ ▒░ 
░          ░   ▒     ░ ░    ▒ ░░░       ░  ░  ░  ░ ░ ░ ▒  
░ ░            ░  ░    ░  ░ ░                 ░      ░ ░  
░  
calipso crypt decrypt by Opale
"""
printlent(Fore.CYAN+banner)

while True: 
    rep = ""
    while rep not in ["crypt", "decrypt"]:
        rep = str(input("crypt or decrypt :"))
    if rep == "crypt":
        coder = str(input("enter msg to crypt:"))
        print(couille(coder, int(25*random())))
    else :
        uncoder = str(input("enter msg to decrypt:"))
        print(couillevide(uncoder))
    input()



