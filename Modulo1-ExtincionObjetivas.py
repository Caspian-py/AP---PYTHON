import os
causas_extincion = {
    "muerte del trabajador": "El fallecimiento del trabajador pone fin de forma automática al vínculo laboral. No se requiere trámite adicional por parte del empleador.",
    "muerte del empleador (persona natural)": "Si el empleador es una persona natural (no una empresa) y fallece, el contrato de trabajo se extingue automáticamente, salvo que los herederos decidan continuar con la relación laboral.",
    "renuncia voluntaria del trabajador": "El trabajador decide terminar su vínculo laboral por voluntad propia. Debe presentar una carta de renuncia con al menos 30 días de anticipación, salvo acuerdo distinto con el empleador.",
    "mutuo acuerdo": "Trabajador y empleador deciden de común acuerdo dar por terminada la relación laboral. Debe formalizarse por escrito, con los términos consensuados por ambas partes.",
    "expiración del plazo del contrato": "Cuando se cumple la fecha de finalización establecida en un contrato de duración determinada, el vínculo laboral termina automáticamente, sin necesidad de notificación adicional.",
    "conclusión de la obra o servicio": "Aplica cuando el contrato fue celebrado para una obra o tarea específica, y esta concluye. La extinción ocurre al finalizar la labor prevista, no se requiere notificación previa.",
    "invalidez permanente total": "Si el trabajador sufre una incapacidad permanente que le impide desempeñar sus funciones, el contrato de trabajo se extingue por imposibilidad sobrevenida.",
    "jubilación del trabajador": "Cuando el trabajador cumple los requisitos legales para jubilarse y accede a una pensión, puede solicitar el fin de su relación laboral. Debe comunicarse por escrito al empleador."
}

def clear():
    return os.system("cls" if os.name == 'nt' else "clear")

def validacion_nombre():
    while True:
        clear()
        print("PARA CERRAR O CANCELAR INGRESE (cancelar, salir)")
        print()
        try:
            print("NOMBRE:")
            nombre = input(">>> ").strip().lower()
            if nombre in ('cancelar', 'salir'):
                return None, False
            else:
                if len(nombre.split()) in range(3, 6) and all(letra.isalpha() for letra in nombre.split()):
                    return nombre, True
                else:
                    raise ValueError
        except ValueError:
            input("NOMBRE NO VALIDO... ")

def validacion_cargo():
    while True:
        clear()
        print("PARA CERRAR O CANCELAR INGRESE (cancelar, salir)")
        print()
        try:
            print("CARGO:")
            cargo = input(">>> ").strip().lower()
            if cargo in ('cancelar', 'salir'):
                return None, False
            else:
                if len(cargo.split()) in range(2, 5) and all(letra.isalpha() for letra in cargo.split()):
                    return cargo, True
                else:
                    raise ValueError
        except ValueError:
            input("CARGO NO VALIDO... ")

def lista_causas():
    for id, causa in enumerate(causas_extincion):
        print(f"{id + 1}) {causa.upper()}")

def validacion_causa():
    while True:
        clear()
        print("INGRESA LA CAUSA CORRESPONDIENTE, PARA SALIR INGRESE ('cancelar', 'salir')")
        print()
        lista_causas()
        print()
        try:
            print("ID:")
            opt = input(">>> ").strip().lower()
            if opt in ('cancelar', 'salir'):
                return None, False
            else:
                if opt.isdigit():
                    id = int(opt) - 1
                    if id in range(0, len(causas_extincion)):
                        temp = list(causas_extincion.keys())
                        clave = temp[id]
                        valor = causas_extincion[clave]
                        clear()
                        print(f"{clave.upper()}: {valor} ")
                        print()
                        if input("SELECCIONAR? (S/N) ").lower().strip() == "s":
                            return (clave, valor), True
                        else:
                            continue
                    else:
                        raise ValueError
                else:
                    raise ValueError
        except ValueError:
            input("OPCION NO VALIDA... ")

def datos_trabajador():
    while True:
        clear()
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

def resumen_extincion():
    clear()
    print("RESUMEN DE EXTINCION DEL CONTRATO LABORAL")
    print()
    print("DATOS DEL TRABAJADOR:")
    print(f"NOMBRE: {datos['nombre'].upper()}")
    print(f"CARGO: {datos['cargo'].upper()}")
    print(f"CAUSA LEGAL DE EXTINCION:")
    print(f"{datos['causa'][0].upper()}: {datos['causa'][1]}")
    print()
def main():
    while True:
        clear()
        if datos_trabajador() == False:
            break
        resumen_extincion()
        print()
        if input("REALIZAR OTRA CONSULTA? (S/N): ").strip().lower() == "n":
            break

main()