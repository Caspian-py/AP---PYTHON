import os

def clear():
    return os.system("cls" if os.name == "nt" else "clear")

def validacion_nombre():
    while True:
        clear()

        print("INGRESE NOMBRE DEL TRABAJADOR")
        print("PARA SALIR O CANCELAR INGRESE ('salir', 'cancelar')")
        print()
        try:
            print("NOMBRE:")
            nombre = input(">>> ").lower().strip()
            if nombre in ('cancelar','salir'):
                return None, False
            else:
                if len(nombre.split()) in range(3, 6) and all(letra.isalpha() for letra in nombre.split()):
                    return nombre, True
                else:
                    raise ValueError
        except ValueError:
            input("NOMBRE NO VALIDO... ")


def recoleccion_datos():
    while True:
        clear()
        
        nombre, estado_nombre = validacion_nombre()
        if estado_nombre == False:
            return False
        

def main():
    while True:
        clear()
        if recoleccion_datos() == False:
            return True
        return True


main()