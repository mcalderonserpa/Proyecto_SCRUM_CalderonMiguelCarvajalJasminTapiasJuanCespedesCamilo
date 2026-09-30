from datetime import datetime

FORMATO_FECHA = "%d-%m-%Y"


# Pide un entero y vuelve a preguntar hasta que sea valido
def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
        except ValueError:
            print("Debe ingresar un numero entero.")
            continue
        if minimo is not None and numero < minimo:
            print(f"El valor minimo es {minimo}.")
            continue
        if maximo is not None and numero > maximo:
            print(f"El valor maximo es {maximo}.")
            continue
        return numero


# Pide una fecha DD-MM-AAAA y la devuelve normalizada
def pedir_fecha(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            return datetime.strptime(texto, FORMATO_FECHA).strftime(FORMATO_FECHA)
        except ValueError:
            print("Formato de fecha invalido. Use DD-MM-AAAA.")