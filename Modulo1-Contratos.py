
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
    "Indeterminado": "Este contrato no tiene una fecha de finalización establecida. Se utiliza cuando existe una relación laboral continua y estable en el tiempo, donde el trabajador presta servicios de forma subordinada y recibe un salario periódico. Es el contrato más común y otorga mayor estabilidad laboral.",

    "Naturaleza temporal": {
        "Inicio o incremento de actividades": "Se emplea cuando la empresa inicia operaciones o abre una nueva sede, sucursal o línea de negocio. Permite contratar personal durante la fase de expansión o consolidación inicial. Su duración máxima es de 3 años, y debe justificarse con documentos que demuestren el crecimiento de la empresa.",
        "Necesidades del mercado": "Se utiliza para cubrir un aumento ocasional o estacional en la demanda de productos o servicios. Ideal para campañas comerciales, temporadas altas o proyectos puntuales. Puede renovarse sucesivamente, hasta un máximo de 5 años, siempre que se justifique la necesidad.",
        "Reconversion empresarial": "Se aplica cuando la empresa realiza transformaciones internas, como cambios tecnológicos, mejoras en procesos productivos o adquisición de nueva maquinaria. Este contrato permite capacitar o adaptar personal por un plazo máximo de 2 años mientras se implementan los cambios."
    },

    "Naturaleza accidental": {
        "Ocasional": "Se utiliza para cubrir tareas que no forman parte de la actividad habitual de la empresa. Ideal para trabajos extraordinarios, como remodelaciones, mudanzas, eventos especiales, etc. Tiene una duración limitada, y solo puede celebrarse hasta un máximo acumulado de 6 meses por año calendario.",
        "Suplencia": "Sirve para reemplazar temporalmente a un trabajador cuya relación laboral está suspendida por licencia médica, maternidad, vacaciones u otra causa justificada. El contrato debe indicar claramente a quién se reemplaza y por cuánto tiempo.",
        "Emergencia": "Se celebra en situaciones imprevistas como desastres naturales (sismos, incendios, inundaciones), fallas técnicas graves o situaciones sanitarias. La duración dependerá del tiempo que dure la emergencia. Su justificación debe estar claramente documentada."
    },

    "Naturaleza obra o servicio": {
        "Especifico": "Contrato vinculado a una labor concreta y delimitada, como una campaña publicitaria, una consultoría, el desarrollo de un software o la construcción de una estructura. Termina automáticamente cuando concluye la tarea. Ideal para trabajos con objetivos definidos y temporales.",
        "Intermitente": "Se usa cuando las actividades laborales ocurren en períodos irregulares a lo largo del año. Por ejemplo, empresas que requieren personal solo en ciertos eventos, ferias o actividades promocionales. El contrato debe especificar los periodos de actividad.",
        "Temporada": "Diseñado para actividades que se repiten cada año en la misma época, como cosechas agrícolas, campañas navideñas, turismo de verano, etc. El contrato debe especificar la duración de la temporada y puede renovarse cada año bajo las mismas condiciones."
    }
}

def clear():
    return os.system("cls") if os.name == "nt" else os.system("clear")

def generar_resumen(c):
    clear()
    print(f"{blanco}=" * 60)
    print(f"{titulo}RESUMEN DEL CONTRATO LABORAL".center(60))
    print(f"{blanco}=" * 60)
    print()
    datos_trabajador()
    print()
    print(f"{titulo}TIPO DE CONTRATO ASIGNADO:")
    print(f"{titulo}Modalidad: {texto}{c.upper()}")
    print(f"{titulo}Descripcion: ", end="")

    for clave, valor in contratos.items():
        if clave == c:
            print(f"{texto} {valor}")
        elif isinstance(valor, dict):
            for cl, desc in valor.items():
                if cl == c:
                    print(f"{texto} {desc}")
    print()
    print(f"{blanco}=" * 60)
    print()
    input(f"FINALIZAR... ")

def datos_trabajador():
    print(f"{titulo}DATOS DEL TRABAJADOR".center(40))
    print(f"{titulo}DNI: {datos['dni']}")
    print(f"{titulo}NOMBRE: {datos['nombres']}")
    print(f"{titulo}CARGO: {datos['cargo']}")

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
        print(f"{titulo}ESCRIBE EL TIPO DE CONTRATO LABORAL O (salir) PARA SALIR:")
        c = input(f"{titulo}>>> ").strip()
        if c.lower() in ("cancelar", 'salir'):
            return
        elif c.lower() in ("indeterminado", "inicio o incremento de actividades", "necesidades del mercado", "reconversion empresarial", "ocasional", "suplencia", "emergencia","especifico" , "intermitente", "temporada"):
            generar_resumen(c.capitalize())
        else:
            input(f"{error}CONTRATO NO VALIDO. ")
            continue
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

