import time, os
from colorama import Fore, Style

centro = os.get_terminal_size().columns

titulo = Fore.YELLOW + Style.BRIGHT
texto = Fore.CYAN + Style.BRIGHT
error = Fore.RED + Style.BRIGHT
exito = Fore.GREEN + Style.BRIGHT

datos = []

def clear():
    return os.system("cls") if os.name == "nt" else os.system("clear")

def validacion_nombre():
    while True:
        clear()
        print(f"{titulo}PARA SALIR INGRESE (cancelar)")
        print()
        try:
            print(f"{titulo}NOMBRE Y APELIIDO:")
            nombres = input(f"{texto}>>> ").strip()
            if nombres.lower() in ("cancelar", ""):
                return None, False
            else:
                if len(nombres.split()) in (3, 4, 5) and all(palabra.isalpha() for palabra in nombres.split()):
                    return nombres, True
                else:
                    raise ValueError
        except ValueError:
            input(F"{error}NOMBRE NO VALIDO ")

def validacion_dni():
    while True:
        clear()
        print(f"{titulo}PARA SALIR INGRESE (cancelar)")
        print()
        try:
            print(f"{titulo}DNI:")
            dni = input(f"{texto}>>> ").strip()
            if dni in ("cancelar", ""):
                return None, False
            else:
                if dni.isdigit() and len(str(dni)) == 8:
                    return int(dni), True
                else:
                    raise ValueError
        except ValueError:
            input(f"{error}DNI NO VALIDO")

def validacion_cargo():
    while True:
        clear()
        print(f"{titulo}PARA SALIR INGRESE (cancelar)")
        print()
        try:
            print(f"{titulo}CARGO O PUESTO:")
            cargo = input(f"{texto}>>> ").strip()
            if cargo in ("cancelar", ""):
                return None, False
            else:
                if len(cargo.split()) in (2, 3, 4) and all(palabra.isalpha() for palabra in cargo.split()):
                    return cargo, True
                else:
                    raise ValueError
        except ValueError:
            input(f"{error}CARGO NO VALIDO")

def Datos():
    while True:
        clear()
        nombres, estado_nombre = validacion_nombre()
        if not estado_nombre:
            input(f"{error}CANCELADO")
            return False

        dni, estado_dni = validacion_dni()
        if not estado_dni:
            input(f"{error}CANCELADO")
            return False

        cargo, estado_cargo = validacion_cargo()
        if not estado_cargo:
            input(f"{error}CANCELADO")
            return False
        
        datos.append(
            {
                "nombres": nombres.upper(),
                "dni": dni,
                "cargo": cargo.lower()
            }
        )
        return True

def Contratos():
    while True:
        clear()
        print(f"{titulo}SELECCIONA EL TIPO DE CONTRATO LABORAL:")
        print()
        input()
        return

def main():
    while True:
        clear()
        print(f"{titulo}BIENVENIDO AL SISTEMA DE CONTRATOS".center(centro))
        print()
        
        print(f"{texto}DATOS DEL TRABAJADOR")
        input("(enter para continuar) ")

        if Datos():
            clear()
            print(f"{exito}DATOS VALIDOS")
        else:
            clear()
            input(f"{error}PRESIONE (enter) PARA SALIR")
            return
        
        print(f"{texto}LISTA DE CONTRATOS DISPONIBLES")
        input("(enter para continuar) ")

        if Contratos():
            clear()
            input(f"{exito} CONTRATO SELECCIONADO")
        else:
            clear()
            input(f"{error} PRESIONE (enter) PARA SALIR")
            return
        

                
main()




