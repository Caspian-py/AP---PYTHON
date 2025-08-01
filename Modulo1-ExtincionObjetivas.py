import os

def clear():
    return os.system("cls" if os.name == 'nt' else "clear")
def validacion_nombre():
    while True:
        clear()
        print("PARA CERRAR O CANCELAR INGRESE (cancelar)")
        print()
        try:
            print("NOMBRE:")
            nombre = input(">>> ").strip().lower()
            if nombre in ('cancelar'):
                input('hello')
                return None, False
            else:
                if len(nombre.split()) in range(3, 5):
                    return nombre, True
                else:
                    
                    raise ValueError
        except ValueError:
            input("NOMBRE NO VALIDO... ")


def datos_trabajador():
    while True:
        clear()
        nombre, estado_nombre = validacion_nombre()
        if estado_nombre == False:
            print("cancelado")
            return False
        
def main():
    while True:
        clear()
        if datos_trabajador() == False:
            break
        break

main()