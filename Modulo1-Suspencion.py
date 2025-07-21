import os, time

def clear():
    return os.system("cls" if os.name == "nt" else "clear")

def validar_nombre():
    while True:
        clear()
        try:
            print("NOMBRE:")
            nombre = input().lower().strip()
            if nombre in ("cancelar", "salir"):
                return None, True
            else:
                if len(nombre.split()) in (3, 4, 5) and all(palabra.isalpha() for palabra in nombre.split()):
                    return nombre, False
                else:
                    raise ValueError
        except ValueError:
            clear()
            input("NOMBRE NO VALIDO")

        


def solicitar_datos():
    while True:
        nombre, estado_nombre = validar_nombre()
        if estado_nombre:
            clear()
            print("CANCELANDO...")
            time.sleep(2)
            return False
        
        


def main():
    while True:
        clear()
        solicitar_datos()
        input()



main()