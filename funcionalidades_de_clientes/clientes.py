import json
import os

ARCHIVO = "funcionalidades_clientes/clientes.json"

def cargar_clientes():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_clientes(clientes):
    # Crea la carpeta si aún no existe
    directorio = os.path.dirname(ARCHIVO)
    if directorio:
        os.makedirs(directorio, exist_ok=True)

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(clientes, archivo, indent=4, ensure_ascii=False)

def registrar_cliente():
    clientes = cargar_clientes()

    print("\n========== REGISTRAR CLIENTE ==========")

    identificacion = input("Ingrese la identificación: ").strip()

    if not identificacion:
        print("La identificación no puede estar vacía.")
        return

    for cliente in clientes:
        if cliente["id"] == identificacion:
            print("Ya existe un cliente con esa identificación.")
            return

    nombres = input("Ingrese los nombres: ").strip()
    apellidos = input("Ingrese los apellidos: ").strip()
    direccion = input("Ingrese la dirección: ").strip()
    telefono_movil = input("Ingrese el teléfono móvil: ").strip()
    telefono_fijo = input("Ingrese el teléfono fijo: ").strip(