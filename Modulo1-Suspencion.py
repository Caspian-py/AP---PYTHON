import os, time

def clear():
    return os.system("cls" if os.name == "nt" else "clear")

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
        
        
        


def main():
    while True:
        clear()
        solicitar_datos()
        input()



main()