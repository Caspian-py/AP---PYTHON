import time, os
from colorama import Fore, Style

centro = os.get_terminal_size().columns

titulo = Fore.YELLOW + Style.BRIGHT
texto = Fore.CYAN + Style.BRIGHT
error = Fore.RED + Style.BRIGHT

datos = []

def clear():
    return os.system("cls") if os.name == "nt" else os.system("clear")


def validacion_nombre():
    try:
        print(f"{titulo}NOMBRE Y APELIIDO:")
        nombres = input(f"{texto}>>> ").strip()
        if len(nombres.split()) in (3, 4, 5) and all(palabra.isalpha() for palabra in nombres.split()):
            return nombres, True
        else:
            raise ValueError
        
    except ValueError:
        return None, False

def validacion_dni():
    try:
        print(f"{titulo}DNI:")
        dni = input(f"{texto}>>> ").strip()
        if dni.isdigit() and len(str(dni)) == 8:
            return int(dni), True
        else:
            raise ValueError
    except ValueError:
        return None, False

def validacion_cargo():
    try:
        print(f"{titulo}CARGO O PUESTO:")
        cargo = input(f"{texto}>>> ").strip()
        if len(cargo.split()) in (1, 2, 3, 4) and all(palabra.isalpha() for palabra in cargo.split()):
            return cargo, True
        else:
            raise ValueError
    except ValueError:
        return None, False
    

def Datos():
    while True:
        clear()
        nombres, estado_nombre = validacion_nombre()
        if estado_nombre == False:
            input(F"{error}NOMBRE NO VALIDO")
            continue
        print(nombres)

        dni, estado_dni = validacion_dni()
        if estado_dni == False:
            input(f"{error}DNI NO VALIDO ")
            continue
        print(dni)

        cargo, estado_cargo = validacion_cargo()
        if estado_cargo == False:
            input(f"{error}CARGO NO VALIDO")
            continue

        
        return
        

def main():
    while True:
        clear()
        print(f"{titulo}BIENVENIDO AL SISTEMA DE CONTRATOS".center(centro))
        print()
        input(f"{texto}VAMOS A PEDIRTE QUE LLENES TUS DATOS POR FAVOR (enter para continuar) ")
        Datos()
        input()
        

                
main()




