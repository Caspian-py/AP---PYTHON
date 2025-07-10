import time, os
from colorama import Fore, Style

centro = os.get_terminal_size().columns

titulo = Fore.YELLOW + Style.BRIGHT
texto = Fore.CYAN + Style.BRIGHT

datos = []

def clear():
    return os.system("cls") if os.name == "nt" else os.system("clear")

def Datos():
    while True:
        clear()
        print(f"{titulo}NOMBRES Y APELLIDOS")
        nombres = input(f"{texto}>>> ").strip()
        print(f"{titulo}DNI:")
        dni = int(input(f"{texto}>>> ").strip())
        print(f"{titulo}CARGO O PUESTO:")
        cargo = input(f"{texto}>>> ").strip()

        datos.append()
        return
        

def main():
    while True:
        clear()
        print(f"{titulo}BIENVENIDO AL SISTEMA DE CONTRATOS".center(centro))
        print()
        input("VAMOS A PEDIRTE QUE LLENES TUS DATOS POR FAVOR (enter para continuar) ")
        Datos()
        input()
        

                
main()




