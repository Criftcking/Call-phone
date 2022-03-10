import time
import subprocess
import colorama
from colorama import Fore
from colorama import Style
from os import system, execl

system("clear")
print("Ejecuta primero el instalador con el comando 'bash instalar.sh' ")
time.sleep(4)
print("")
print(Fore.GREEN + "Es Importante que ejecutes dos veces para que te funcione")
print(Fore.RED + "")
print("[+]Activando...")
print("")
print(Fore.BLUE + "")
time.sleep(0.9)
print("       /` \/ `\_  _   ")
print("       \     /` \/ `\ ")
print("        '.  .\      /")
print("          \/  '.  .'")
print("                \/")
time.sleep(0.5)
print("                 /` \/ `\_  _  ")
print("                 \     /` \/ `\ ")
print("                  '.  .\      / ")
print("                    \/  '.  .' ")
print("                          \/ ")


time.sleep(2.3)
system("")
system("")
system("")
time.sleep(1)
print(Fore.RED + "By:Criftcking")
print(Fore.YELLOW + "▒█░░░ █░░ █▀▀█ █▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀")
print(Fore.YELLOW + "▒█░░░ █░░ █▄▄█ █░▀░█ █▄▄█ █░░█ █▄▄█ ▀▀█")
print(Fore.YELLOW + "▒█▄▄█ ▀▀▀ ▀░░▀ ▀░░░▀ ▀░░▀ ▀▀▀░ ▀░░▀ ▀▀▀")

print(Fore.BLUE + "")                                               
numero = input("[+]Numero:")                                              
print("\u001b[32;1m[+]Llamando...")
time.sleep(2)
subprocess.call("termux-telephony-call {}".format(numero),shell=True )
subprocess.call("termux-telephony-call {}".format(numero),shell=True )
