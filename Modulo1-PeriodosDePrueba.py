
import os
from colorama import Fore, Style
titulo = Fore.YELLOW + Style.BRIGHT
texto = Fore.CYAN + Style.BRIGHT
error = Fore.RED + Style.BRIGHT
exito = Fore.GREEN + Style.BRIGHT
blanco = Fore.WHITE + Style.BRIGHT

def clear():
    return os.system("cls" if os.name == 'nt' else "clear")

def validacion_nombre():
    while True:
        clear()
        print("PARA CANCELAR INGRESE 'cancelar'.")
        try:
            print("NOMBRE:")
            nombre = input(">>> ").lower().strip()
            if nombre in ("cancelar", "salir"):
                return None, False
            else:
                if len(nombre.split()) in (3, 4, 5) and all(palabra.isalpha() for palabra in nombre.split()):
                    return nombre, True
                else:
                    raise ValueError
        except ValueError:
            input("NOMBRE NO VALIDO")

def validacion_cargo():
    while True:
        clear()
        print("PARA CANCELAR INGRESE 'CANCELAR'. ")
        try:
            print("CARGO:")
            cargo = input(">>> ").lower().strip()
            if cargo in ("cancelar", "salir"):
                return None, False
            else:
                if len(cargo.split()) in (2, 3, 4, 5) and all(palabra.isalpha() for palabra in cargo.split()):
                    return cargo, True
                else:
                    raise ValueError
        except ValueError:
            input("CARGO NO VALIDO")

def datos():

    nombre, estado_nombre = validacion_nombre()
    if not estado_nombre:
        input("CANCELADO")
        return

    cargo, estado_cargo = validacion_cargo()
    if not estado_cargo:
        input("CANCELADO")
        return

        



def main():
    datos()
    input()

main()


