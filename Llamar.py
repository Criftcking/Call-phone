import time
import subprocess
import colorama
from colorama import Fore
from colorama import Style

print("")
print("")
print(Fore.RED + "By:Criftcking")
print(Fore.YELLOW + "▒█░░░ █░░ █▀▀█ █▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀")
print(Fore.YELLOW + "▒█░░░ █░░ █▄▄█ █░▀░█ █▄▄█ █░░█ █▄▄█ ▀▀█")
print(Fore.YELLOW + "▒█▄▄█ ▀▀▀ ▀░░▀ ▀░░░▀ ▀░░▀ ▀▀▀░ ▀░░▀ ▀▀▀")

print(Fore.BLUE + "")                                               
numero = input("[+]Numero:")                                              
print("\u001b[32;1m[+]Llamando...")
time.sleep(2)
subprocess.call("termux-telephony-call {}".format(numero),shell=True )
