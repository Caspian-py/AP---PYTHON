
import os
from colorama import Fore, Style
titulo = Fore.YELLOW + Style.BRIGHT
texto = Fore.CYAN + Style.BRIGHT
error = Fore.RED + Style.BRIGHT
exito = Fore.GREEN + Style.BRIGHT
blanco = Fore.WHITE + Style.BRIGHT

contratos_validos = ("indeterminado", "inicio o incremento de actividades", "necesidades del mercado", "reconversion empresarial", "ocasional", "suplencia", "emergencia", "especifico", "intermitente", "temporada")
cargos_direccion = ["director", "gerente", "jefe general", "subgerente"]
cargos_confianza = ["analista", "especialista", "supervisor", "coordinador", "encargado", "jefe"]
justificacion_por_tipo = {
    12: "Se trata de un cargo de dirección (como gerente o director). "
        "La ley permite ampliar el período de prueba hasta 12 meses. "
        "(Art. 10, D.S. N.º 003-97-TR).",

    6: "Se trata de un cargo calificado o de confianza (como analista, supervisor o coordinador). "
       "La ley permite ampliar el período de prueba hasta 6 meses. "
       "(Art. 10, D.S. N.º 003-97-TR).",

    3: "No se identificaron funciones especiales en el cargo. "
       "Se aplica el período de prueba estándar de 3 meses. "
       "(Art. 10, D.S. N.º 003-97-TR)."
}
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
        print("PARA CANCELAR INGRESE 'cancelar'. ")
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

def validacion_contrato():
    while True:
        clear()
        print("PARA CANCELAR INGRESE 'cancelar'. ")
        try:
            print("CONTRATO:")
            contrato = input(">>> ").lower().strip()
            if contrato in ("cancelar", "salir"):
                return None, False
            else:
                if len(contrato.split()) <= 5 and all(palabra.isalpha() for palabra in contrato.split()) and contrato in contratos_validos:
                    return contrato, True
                else:
                    raise ValueError
        except ValueError:
            input("CONTRATO NO ENCONTRADO")

def datos():

    nombre, estado_nombre = validacion_nombre()
    if not estado_nombre:
        input("CANCELADO")
        return

    cargo, estado_cargo = validacion_cargo()
    if not estado_cargo:
        input("CANCELADO")
        return
    
    contrato, estado_contrato = validacion_contrato()
    if not estado_contrato:
        input("CANCELADO")
        return
    global datos
    datos = {
        "nombre": nombre.upper(),
        "cargo": cargo.upper(),
        "contrato": contrato.upper()
    }

def asignacion_periodo():
    cargo = datos['cargo'].lower()
    
    if any(palabra in cargo for palabra in cargos_direccion):
        print("ENCONTRADO EN DIRECCION")
    elif any(palabra in cargo for palabra in cargos_confianza):
        print("ENCONTRADO EN CONFIANZA")
    else:
        print("NO HEMOS ENCONTRADO")
def main():
    datos()
    asignacion_periodo()
    input()

main()


