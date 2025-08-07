import os

def clear():
    return os.system("cls" if os.name == "nt" else "clear")

def validacion_nombre():
    while True:
        clear()
        print("DIGITE NOMBRE DEL TRABAJADOR PARA SALIR INGRESE ('salir', 'cancelar')")
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
            

def obtencion_datos():
    while True:

        nombre, estado_nombre = validacion_nombre()
        if estado_nombre == False:
            return False
        
        return True
        



def main():
    while True:
        clear()
        if obtencion_datos() == False:
            break

main()