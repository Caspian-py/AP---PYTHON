import os, time

def clear():
    return os.system("cls" if os.name == "nt" else "clear")
causas_con_goce = {
    "Licencia por maternidad": {
        "descripcion": "Derecho protegido por ley. La trabajadora gestante tiene 98 días de descanso obligatorio: 49 antes y 49 después del parto.",
        "base_legal": "Ley N.º 26644, Art. 16 DS 003-97-TR",
        "duracion": "98 días",
        "observacion": "Subsidio otorgado por Essalud"
    },
    "Licencia por paternidad": {
        "descripcion": "Permite al padre trabajador ausentarse por el nacimiento de su hijo o hija. Pagado por el empleador.",
        "base_legal": "Ley N.º 29409",
        "duracion": "10 a 30 días",
        "observacion": "Duración depende de circunstancias (parto múltiple, prematuro, cesárea, etc.)"
    },
    "Licencia por adopción": {
        "descripcion": "Aplica el mismo tratamiento que la licencia por maternidad, si se adopta un menor de edad.",
        "base_legal": "Ley N.º 30311",
        "duracion": "98 días",
        "observacion": "Subsidio de Essalud, previa acreditación de adopción"
    },
    "Licencia sindical (dirigentes)": {
        "descripcion": "Suspensión para ejercer funciones sindicales sin afectar el sueldo del dirigente.",
        "base_legal": "Art. 31 del TUO del D.L. N.º 728",
        "duracion": "Según estatuto del sindicato",
        "observacion": "Debe estar autorizada y registrada"
    },
    "Vacaciones anuales": {
        "descripcion": "Descanso físico remunerado acumulado por un año de servicios. Se considera suspensión con goce.",
        "base_legal": "Art. 10 del Decreto Legislativo N.º 713",
        "duracion": "30 días calendario",
        "observacion": "Remuneración se mantiene íntegra"
    }
}

causas_sin_goce = {
    "Enfermedad común o accidente": {
        "descripcion": "Suspensión temporal del contrato mientras el trabajador se recupera. No se paga sueldo, pero puede recibir subsidio de Essalud.",
        "base_legal": "Art. 11 y 12 del Decreto Legislativo N.º 728",
        "duracion": "Hasta el alta médica",
        "observacion": "Debe presentar certificado médico y calificar para subsidio"
    },
    "Licencia sin goce de haber": {
        "descripcion": "El trabajador solicita una licencia por asuntos personales. No percibe remuneración.",
        "base_legal": "Art. 16 del D.S. N.º 003-97-TR",
        "duracion": "Según acuerdo entre trabajador y empleador",
        "observacion": "Debe estar formalizada por escrito"
    },
    "Huelga legal": {
        "descripcion": "Durante la huelga reconocida, se suspende la relación laboral sin pago. No se pierde antigüedad.",
        "base_legal": "Ley de Relaciones Colectivas de Trabajo, Art. 73",
        "duracion": "Mientras dure la huelga legal",
        "observacion": "Solo válida si está reconocida por la autoridad de trabajo"
    },
    "Detención preventiva": {
        "descripcion": "Si el trabajador es detenido sin sentencia, se suspende su contrato. Puede reincorporarse si queda libre.",
        "base_legal": "Art. 16 inciso d) del D.S. N.º 003-97-TR",
        "duracion": "Máximo 3 meses",
        "observacion": "Debe notificarse al empleador"
    },
    "Inhabilitación judicial o administrativa": {
        "descripcion": "Cuando una autoridad impide legalmente al trabajador ejercer su función (ej. por corrupción, sanción técnica).",
        "base_legal": "Art. 16 inciso e) del D.S. N.º 003-97-TR",
        "duracion": "Mientras dure la inhabilitación",
        "observacion": "Debe acreditarse mediante resolución"
    },
    "Fuerza mayor o caso fortuito": {
        "descripcion": "Suspensión colectiva autorizada por SUNAFIL cuando la empresa no puede operar por causa externa (terremoto, incendio, pandemia, etc).",
        "base_legal": "Art. 15 inciso g) del D.S. N.º 003-97-TR",
        "duracion": "Según resolución de la autoridad",
        "observacion": "Se tramita como suspensión perfecta"
    },
    "Servicio militar obligatorio o reservista": {
        "descripcion": "El trabajador es llamado al servicio militar. Se suspende su contrato durante ese período.",
        "base_legal": "Art. 16 inciso f) del D.S. N.º 003-97-TR",
        "duracion": "Según lo que disponga la ley militar",
        "observacion": "El trabajador puede reincorporarse luego"
    }
}


def validar_nombre():
    while True:
        clear()
        try:
            print("NOMBRE:")
            nombre = input(">>> ").lower().strip()
            if nombre in ("cancelar", "salir"):
                return None, True
            else:
                if len(nombre.split()) in (3, 4, 5) and all(palabra.isalpha() for palabra in nombre.split()):
                    return nombre, False
                else:
                    raise ValueError
        except ValueError:
            clear()
            input("NOMBRE NO VALIDO... ")

def validar_cargo():
    while True:
        clear()
        try:
            print("CARGO:")
            cargo = input(">>> ").lower().strip()
            if cargo in ("cancelar", "salir"):
                return None, True
            else:
                if len(cargo.split()) in (2, 3, 4) and all(palabra.isalpha() for palabra in cargo.split()):
                    return cargo, False
                else:
                    raise ValueError
        except ValueError:
            clear()
            input("CARGO NO VALIDO... ")

def validar_causa():
    while true:
        clear()
        try:
            print("DIGITE LA CAUSA DE SUSPENCION:")
            causa = input("CAUSA >>> ").lower().strip()
            if causa in ("cancelar", "salir"):
                return None, True
            else:
                print("llegaste lejos.")




def solicitar_datos():
    while True:
        nombre, estado_nombre = validar_nombre()
        if estado_nombre:
            clear()
            print("CANCELANDO... ")
            time.sleep(2)
            return False
        
        cargo, estado_cargo = validar_cargo()
        if estado_cargo:
            clear()
            print("CANCELANDO... ")
            time.sleep(2)
            return False
        
        causa, estado_causa = validar_causa():
        if estado_causa:
            clear()
            print("CANCENLANDO... ")
            time.sleep()
            return False

        
        
        


def main():
    while True:
        clear()
        solicitar_datos()
        input()



main()