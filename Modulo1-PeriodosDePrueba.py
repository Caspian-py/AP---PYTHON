
import os
from colorama import Fore, Style

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

def informacion():

    nombre, estado_nombre = validacion_nombre()
    if not estado_nombre:
        input("CANCELADO")
        return False

    cargo, estado_cargo = validacion_cargo()
    if not estado_cargo:
        input("CANCELADO")
        return False
    
    contrato, estado_contrato = validacion_contrato()
    if not estado_contrato:
        input("CANCELADO")
        return False
    global datos
    datos = {
        "nombre": nombre.upper(),
        "cargo": cargo.upper(),
        "contrato": contrato.upper()
    }
    return True

def asignacion_periodo():
    cargo = datos['cargo'].lower()
    global justificacion, tiempo
    if any(palabra in cargo for palabra in cargos_direccion):
        tiempo = 12
        justificacion = justificacion_por_tipo[12]
    elif any(palabra in cargo for palabra in cargos_confianza):
        tiempo = 6
        justificacion = justificacion_por_tipo[6]
    else:
        tiempo = 3
        justificacion = justificacion_por_tipo[3]

def resumen_final():
    clear()
    print("=" * 60)
    print("EVALUCACION DEL PERIODO DE PRUEBA")
    print("=" * 60)
    print()
    print("Datos del trabajador: ")
    print(f"Nombres: {datos['nombre'].upper()}")
    print(f"Cargo: {datos['cargo'].upper()}")
    print(f"Contrato: {datos['contrato'].upper()}")
    print()
    print("Resultado:")
    print(f"Periodo de prueba asignado: {tiempo} meses")
    print(f"Justificaion: {justificacion}")
    print()
    print("=" * 60)
    print()
    if input("REALIZAR OTRA CONSULTA? (s/n) ").strip().lower() == "n":
        return False
    else:
        return True

def main():
    while True:
        if not informacion():
            break
        asignacion_periodo()
        if not resumen_final():
            break

main()


