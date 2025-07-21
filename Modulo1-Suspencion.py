import os, time

def clear():
    return os.system("cls" if os.name == "nt" else "clear")
causas_con_goce = {
    "licencia por maternidad": """Cuando una trabajadora está embarazada, tiene derecho a descansar antes y después del parto sin perder su sueldo ni su trabajo.
Se trata de un permiso de 98 días (49 días antes y 49 días después del parto).
Durante ese tiempo, EsSalud paga un subsidio en lugar del sueldo.
Duración: 98 días.
Base legal: Ley N.º 26644 y D.S. N.º 003-97-TR, Art. 16.
    """,
    "licencia por paternidad": """Si eres papá y acaba de nacer tu hijo o hija, tienes derecho a unos días de descanso pagado para estar con tu familia.
La cantidad de días puede ser de 10 a 30, dependiendo del tipo de parto.
Durante esos días, tu empleador sigue pagándote tu sueldo.
Duración: 10 a 30 días.
Base legal: Ley N.º 29409.
""",
"licencia por adopcion": """Si adoptas legalmente a un niño o niña, tienes derecho al mismo descanso que una madre biológica.
Durante ese tiempo no trabajas, pero recibes un subsidio de EsSalud.
Duración: 98 días.
Base legal: Ley N.º 30311.
""",
"licencia sindical (para dirigentes)":"""Si eres dirigente sindical, puedes ausentarte del trabajo para realizar tus actividades del sindicato.
Seguirás recibiendo tu sueldo y no perderás antigüedad ni beneficios.
Duración: Lo que diga el estatuto del sindicato.
Base legal: D.L. N.º 728, Art. 31.
""",
"vacaciones anuales":"""Después de trabajar un año, tienes derecho a 30 días de descanso pagado.
Durante ese mes no trabajas, pero te pagan tu sueldo normal.
Duración: 30 días calendario.
Base legal: D.L. N.º 713, Art. 10.
"""
}

causas_sin_goce = {
    "enfermedad comun o accidente": """Si te enfermas o sufres un accidente y no puedes trabajar, el empleador no te paga, pero puedes recibir un subsidio de EsSalud (si estás asegurado).
Mientras estés con descanso médico, tu contrato se suspende y no pierdes tu puesto.
Duración: Hasta que te recuperes.
Base legal: D.L. N.º 728, Art. 11 y 12.
""",
"licencia sin goce de haber": """Si necesitas tiempo para resolver asuntos personales (como viajar, estudiar, etc.), puedes pedir una licencia sin sueldo.
Debe estar por escrito y aprobada por el empleador.
No trabajas ni cobras, pero mantienes tu puesto.
Duración: El tiempo que acuerdes con tu empleador.
Base legal: D.S. N.º 003-97-TR, Art. 16.
""",
"huelga legal": """Si participas en una huelga que fue aprobada por la autoridad laboral, tu contrato se suspende.
Durante ese tiempo no cobras, pero no pierdes antigüedad ni el trabajo.
Duración: Mientras dure la huelga.
Base legal: Ley de Relaciones Colectivas de Trabajo, Art. 73.
""",
"detencion preventiva": """Si estás detenido sin condena (por un juicio en proceso), tu contrato se suspende por un máximo de 3 meses.
Si luego te liberan y no tienes condena, puedes regresar al trabajo.
Duración: Hasta 3 meses.
Base legal: D.S. N.º 003-97-TR, Art. 16(d).
""",
"inhabilitacion judicial o administrativa": """Si te suspenden legalmente de ejercer tu profesión (por ejemplo, si pierdes la colegiatura o tienes una sanción judicial), no puedes trabajar.
Tu contrato se suspende sin sueldo, pero se mantiene hasta que puedas volver.
Duración: Mientras dure la inhabilitación.
Base legal: D.S. N.º 003-97-TR, Art. 16(e).
""",
"fuerza mayor o caso fortuito": """Cuando ocurren situaciones graves e imprevistas (terremoto, pandemia, incendio, etc.) que impiden seguir trabajando, la empresa puede pedir autorización para suspender los contratos.
Durante ese tiempo no se paga sueldo, pero se mantiene el vínculo laboral.
Duración: Lo que autorice SUNAFIL.
Base legal: D.S. N.º 003-97-TR, Art. 15(g).
""",
"servicio militar obligatorio o reservista": """Si eres convocado al servicio militar o a la reserva del ejército, puedes ausentarte del trabajo.
No se te paga, pero al terminar puedes regresar al mismo puesto.
Duración: Según lo que diga el ejército.
Base legal: D.S. N.º 003-97-TR, Art. 16(f).
"""
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
    while True:
        clear()
        try:
            print(causas_con_goce)
            print("DIGITE LA CAUSA DE SUSPENCION:")
            causa = input("CAUSA >>> ").lower().strip()
            if causa in ("cancelar", "salir"):
                return None, True
            else:
                print("llegaste lejos.")
        except ValueError:
            clear()
            input("CAUSA NO ENCONTRADA")





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
        
        causa, estado_causa = validar_causa()
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