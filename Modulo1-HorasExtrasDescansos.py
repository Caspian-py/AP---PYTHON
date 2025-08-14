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

def validacion_cargo():
    while True:
        clear()

        print("INGRESE CARGO DEL TRABAJADOR")
        print("PARA SALIR O CANCELAR INGRESE ('salir', 'cancelar')")
        print()
        try:
            print("CARGO:")
            cargo = input(">>> ").lower().strip()
            if cargo in ('cancelar', 'salir'):
                return None, False
            else:
                if len(cargo.split()) in range(2, 6) and all(letra.isalpha() for letra in cargo.split()):
                    return cargo, True
                else:
                    raise ValueError
        except ValueError:
            input("CARGO NO VALIDO... ")

def validacion_renumeracion_mensual():
    while True:
        clear()

        print("INGRESE LA RENUMERACION MENSUAL DEL TRABAJADOR")
        print("PARA SALIR O CANCELAR INGRESE ('salir', 'cancelar')")
        print()
        try:
            print("RENUMERACION MENSUAL:")
            renumeracion_mensual = input(">>> ").lower().strip().replace(",", "")
            if renumeracion_mensual in ('cancelar', 'salir'):
                return None, False
            elif float(renumeracion_mensual) and 1025 <= float(renumeracion_mensual) <= 50000:
                return renumeracion_mensual, True
            else:
                raise ValueError
        except ValueError:
            input("RENUMERACION MENSUAL NO VALIDO... ")

def validacion_horas():
    while True:
        clear()
        print("INGRESE SUS HORAS ORDINARIAS Y HORAS EXTRAS TRABAJADAS DEL TRABAJADOR")
        print("PARA SALIR O CANCELAR INGRESE ('salir','cancelar')")
        print()
        try:
            print("HORAS DE LA JORNADA MENSUAL:")
            if (jornada_mensual := input(">>> ").lower().strip()) in ('salir','cancelar'):
                return None, False
            elif not jornada_mensual.isdigit() or not jornada_mensual in range(120, 193):
                raise ValueError
            
            while True:
                print("TOTAL DE HORAS EXTRAS POR MES QUE ESTAN DENTRO DEL LIMITE DE 2 HORAS DIAS (25%)")
                if (extras25:=input(">>> ").strip().lower()) in ('salir','cancelar'):
                    return None, False
                elif not extras25.isdigit() or not extras25 in range(0, 49):
                    input("HORAS NO VALIDAS... ")
                    continue

                print("TOTAL DE HORAS EXTRAS POR MES QUE EXCEDEN LAS 2 HORAS DIARIAS (35%)")
                if (extras35:=input(">>> ").strip().lower()) in ('salir', 'cancelar'):
                    return None, False
                elif not extras35.isdigit() or not extras35 in range(0, 61):
                    input("HORAS NO VALIDAS... ")
                    continue
                
                if (extras25 + extras35) <= 96:
                    break

        except ValueError:
            input("HORAS NO VALIDAS... ")


def recoleccion_datos():
    while True:
        clear()
        
        nombre, estado_nombre = validacion_nombre()
        if estado_nombre == False:
            return False
        
        cargo, estado_cargo = validacion_cargo()
        if estado_cargo == False:
            return False
        
        renumeracion_mensual, estado_renumeracion_mensual = validacion_renumeracion_mensual()
        if estado_renumeracion_mensual == False:
            return False
        
        horas, estado_horas = validacion_horas()
        if estado_horas == False:
            return False
        

def main():
    while True:
        clear()
        if recoleccion_datos() == False:
            return True
        return True


main()