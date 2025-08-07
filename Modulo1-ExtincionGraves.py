import os

def clear():
    return os.system("cls" if os.name == "nt" else "clear")
faltas_graves = {
    "inasistencia injustificada": {
        "descripcion": (
            "Faltar al trabajo sin justificación durante tres días consecutivos "
            "o cinco días no consecutivos en un mes calendario. Esto perjudica la continuidad de las labores."
        ),
        "explicacion_procedimiento": (
            "Se requiere procedimiento previo: el empleador debe enviar una carta de preaviso (carta de imputación) "
            "indicando la falta y otorgar un plazo razonable para que el trabajador haga sus descargos por escrito "
            "antes de tomar una decisión final sobre el despido."
        )
    },

    "violencia o injuria": {
        "descripcion": (
            "Agredir física o verbalmente al empleador, compañeros o superiores. "
            "Esto incluye amenazas, insultos graves o actos de violencia en el trabajo."
        ),
        "explicacion_procedimiento": (
            "No requiere procedimiento previo si el acto es evidente y grave. "
            "El empleador puede proceder con el despido inmediato si existen pruebas claras, "
            "como videos, testimonios u otros medios que respalden la falta."
        )
    },

    "hurto o apropiación indebida": {
        "descripcion": (
            "Tomar o usar bienes, dinero o recursos de la empresa sin autorización. "
            "Es una falta de confianza y puede ser considerada delito."
        ),
        "explicacion_procedimiento": (
            "No requiere procedimiento previo si la falta es evidente y comprobable. "
            "Se puede proceder al despido directo, especialmente si hay pruebas documentadas o confesión."
        )
    },

    "abandono de trabajo": {
        "descripcion": (
            "Dejar el puesto de trabajo sin autorización por más de tres días consecutivos, "
            "interrumpiendo el normal desarrollo de las actividades."
        ),
        "explicacion_procedimiento": (
            "Se debe seguir un procedimiento previo. El empleador debe notificar la ausencia, "
            "solicitar justificación y permitir descargo antes del despido."
        )
    },

    "estado de ebriedad o drogas": {
        "descripcion": (
            "Acudir al trabajo bajo efectos del alcohol o drogas que afecten el desempeño o pongan en riesgo a otros."
        ),
        "explicacion_procedimiento": (
            "No requiere procedimiento previo si la falta es evidente y representa un riesgo grave. "
            "Sin embargo, es recomendable documentar la situación (testigos, actas, etc.)."
        )
    },

    "incumplimiento grave de obligaciones": {
        "descripcion": (
            "No cumplir con responsabilidades clave del cargo, de forma reiterada o intencional, afectando el servicio o producción."
        ),
        "explicacion_procedimiento": (
            "Se requiere procedimiento previo: el empleador debe comunicar formalmente la falta, "
            "otorgar un plazo para descargos y evaluar la respuesta antes del despido."
        )
    },

    "negativa a cumplir tareas razonables": {
        "descripcion": (
            "Rehusarse injustificadamente a realizar labores propias del puesto o asignaciones adicionales dentro de lo razonable."
        ),
        "explicacion_procedimiento": (
            "Es necesario seguir un procedimiento previo, brindando oportunidad al trabajador para explicar las razones de su negativa."
        )
    }
}

def validacion_nombre():
    while True:
        clear()
        print("INGRESE NOMBRE DEL TRABAJADOR PARA SALIR INGRESE ('salir', 'cancelar')")
        try:
            print("NOMBRE:")
            nombre = input(">>> ").strip().lower()
            if nombre in ('salir', 'cancelar'):
                return None, False
            else:
                if len(nombre.split()) in range(3,6) and all(letra.isalpha() for letra in nombre.split()):
                    return nombre, True
                else:
                    raise ValueError
        except ValueError:
            input("NOMBRE NO VALIDO... ")

def validacion_cargo():
    while True:
        clear()
        print("INGRESE CARGO DEL TRABAJADOR PARA SALIR INGRESE ('salir', 'cancenlar')")
        try:
            print("CARGO:")
            cargo = input(">>> ").lower().strip()
            if cargo in ('salir', 'cancelar'):
                return None, False
            else:
                if len(cargo.split()) in range(2, 5) and all(letra.isalpha() for letra in cargo.split()):
                    return cargo, True
                else:
                    raise ValueError
        except ValueError:
            input("CARGO NO VALIDO...")

def mostrar_causas():
    for id, clave in enumerate(faltas_graves):
        print(f"{id + 1}) {clave.upper()}")

def validacion_causa():
    while True:
        clear()
        print("DIGITE LA CAUSA, PARA SALIR INHRESE ('salir', 'cancenlar')")
        mostrar_causas()
        print()
        try:
            print("ID")
            opt = input(">>> ").lower().strip()
            if opt in ('salir', 'cancelar'):
                return None, False
            else:
                if opt.isdigit() and (int(opt) - 1) in range(0,len(faltas_graves)):
                    clear()
                    id = int(opt) - 1
                    clave = list(faltas_graves.keys())[id]
                    descripcion = faltas_graves[clave]['descripcion']
                    explicacion_procedimiento = faltas_graves[clave]['explicacion_procedimiento']
                    print(f"{clave.upper()}: {descripcion}")
                    print(f"{explicacion_procedimiento}")
                    print()
                    if input("SELECCIONAR? (S/N): ").lower().strip().startswith('s'):
                        return (clave, descripcion, explicacion_procedimiento), True
                    else:
                        continue
                else:
                    raise ValueError
        except ValueError:
            input("CAUSA NO VALIDA.. ")

def obtencion_datos():
    while True:

        nombre, estado_nombre = validacion_nombre()
        if estado_nombre == False:
            return False
        
        cargo, estado_cargo = validacion_cargo()
        if estado_cargo == False:
            return False
        
        causa, estado_causa = validacion_causa()
        if estado_causa == False:
            return False
        global datos
        datos = {
            "nombre": nombre,
            "cargo": cargo,
            "causa": causa
        }
        return True

def resumen():
    clear()
    print("RESUMEN GENERAL")
    print()
    print("DATOS DEL TRABAJADOR:")
    print(f"NOMBRE: {datos['nombre'].upper()}")
    print(f"CARGO: {datos['cargo'].upper()}")
    print(f"CAUSA: {datos['causa'][0]}")
    print(f"Descripcion: {datos['causa'][1]}")
    print(f"Explicacion del Procedimiento: {datos['causa'][2]}")
    print()

def main():
    while True:
        clear()
        if obtencion_datos() == False:
            break
        resumen()
        print()
        if input("REALIZAR OTRA CONSULTA? (S/N): ").lower().strip().startswith('n'):
            break

main()