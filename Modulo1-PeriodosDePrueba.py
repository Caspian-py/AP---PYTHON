
import os
from colorama import Fore, Style
titulo = Fore.YELLOW + Style.BRIGHT
texto = Fore.CYAN + Style.BRIGHT
error = Fore.RED + Style.BRIGHT
exito = Fore.GREEN + Style.BRIGHT
blanco = Fore.WHITE + Style.BRIGHT

def clear():
    return ("cls" if os.name == 'nt' else "clear")

def validacion_nombre():
    while True:
        print("NOMBRE:")
        nombre = input(">>> ")

def datos():
    if not validacion_nombre:
        print("NOMBRE NO VALIDO")
        continue



def main():
    datos()


