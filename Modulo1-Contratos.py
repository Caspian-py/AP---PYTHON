import time, os
from colorama import Fore, Style

centro = os.get_terminal_size().columns

titulo = Fore.YELLOW + Style.BRIGHT
texto = Fore.CYAN + Style.BRIGHT
error = Fore.RED + Style.BRIGHT
exito = Fore.GREEN + Style.BRIGHT
blanco = Fore.WHITE + Style.BRIGHT

datos = {}

contratos = {
    "Indeterminado": "No tiene fecha de termino. Se asume cuando hay continuidad, subordinacion y pago.",
    "Naturaleza Temporal": {
        "Inicio o incremento de actividades": "Para empresas nuevas o que abren nueva sede o linea de negocio. Max 3 años",
        "Necesidades del mercado": "Por aumento temporal de la demanda. Renovable hasta 5 años.",
        "Reconversion empresarial": "Cambios en procesos, tecnologia o maquinaria . Max. 2 años."
    },
    "Naturaleza Accidental": {
        "Ocasional": "Actividades no habituales, por un tiempo corto, Max. 6 meses al año.",
        "Suplencia": "Para reemplazar a un trabajador con vinculo suspendido (por licencia, etc..).",
        "Emergencia": "Por eventos inesperados: sismos, inundaciones, etc. Dure lo que dure la emergencia."
    },
    "Naturaleza Obra o servicio": {
        "Especifico": "Para una tarea concreta con fecha fin (ej. Campaña publicitaria puntual).",
        "Intermitente": "Actividades que ocurren varias veces al año, pero no de forma continua.",
        "Temporada": "Actividades que se repiten cada año en la misma epoca (ej. cosecha, navidad)."
    }

}

def clear():
    return os.system("cls") if os.name == "nt" else os.system("clear")

def datos_trabajador():
    print(f"{blanco}=" * 30)
    print(f"{titulo}DATOS DEL TRABAJADOR".center(40))
    print(f"{titulo}DNI: {datos['dni']}")
    print(f"{titulo}NOMBRE: {datos['nombres']}")
    print(f"{titulo}CARGO: {datos['cargo']}")
    print()
    print(f"{blanco}=" * 30)
def mostrar_contratos():
    datos_trabajador()
    print(f"{titulo}TIPOS DE CONTRATOS".center(centro))
    for tipo, contenido in contratos.items():
        print(f"{titulo}{tipo}: ")
        if isinstance(contenido, dict):
            for subtipo, descripcion in contenido.items():
                print(f"{titulo}{subtipo}: {texto}{descripcion}")
            print()
        else:
            print(f"{texto}{contenido}")
            print()

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
        global datos
        datos = {
                "nombres": nombres.upper(),
                "dni": dni,
                "cargo": cargo.upper()
            }
        return True

def Contratos():
    while True:
        clear()
        mostrar_contratos()
        print()
        print(f"{titulo}SELECCIONA EL TIPO DE CONTRATO LABORAL:")
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

