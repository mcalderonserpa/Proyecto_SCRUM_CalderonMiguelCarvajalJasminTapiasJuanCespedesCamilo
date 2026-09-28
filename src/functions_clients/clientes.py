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
    telefono_fijo = input("Ingrese el teléfono fijo: ").strip()

    print("\nSeleccione el estado:")
    print("1. En proceso de inscripción")
    print("2. Inscrito")
    print("3. Activo")
    print("4. Inactivo")

    opcion_estado = input("Seleccione una opción: ")
    
    estados = {
         "1": "En proceso de inscripción",
         "2": "Inscrito",
         "3": "Activo",
         "4": "Inactivo"
        }
    
    if opcion_estado not in estados:
        print("Estado no válido.")
        return
    
    estado = estados[opcion_estado]
    
    print("\nSeleccione el nivel de riesgo:")
    print("1. Alto")
    print("2. Medio")
    print("3. Bajo")
    
    opcion_riesgo = input("Seleccione una opción: ")
    
    riesgos = {
        "1": "Alto",
        "2": "Medio",
        "3": "Bajo"
        }
    
    if opcion_riesgo not in riesgos:
        print("Nivel de riesgo no válido.")
        return
    
    nivel_riesgo = riesgos[opcion_riesgo]
    
    nuevo_cliente = {
        "id": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "telefono_movil": telefono_movil,
        "telefono_fijo": telefono_fijo,
        "estado": estado,
        "nivel_riesgo": nivel_riesgo
        }

