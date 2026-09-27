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

    clientes.append(nuevo_cliente)
    guardar_clientes(clientes)

    print("\nCliente registrado correctamente.")

def listar_clientes():
    clientes = cargar_clientes()

    if not clientes:
        print("\nNo hay clientes registrados.")
        return

    print("\n========== LISTA DE CLIENTES ==========")

    for cliente in clientes:
        print("\n----------------------------------------")
        print(f"ID: {cliente['id']}")
        print(f"Nombres: {cliente['nombres']}")
        print(f"Apellidos: {cliente['apellidos']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Teléfono móvil: {cliente['telefono_movil']}")
        print(f"Teléfono fijo: {cliente['telefono_fijo']}")
        print(f"Estado: {cliente['estado']}")
        print(f"Nivel de riesgo: {cliente['nivel_riesgo']}")

def buscar_cliente():
    clientes = cargar_clientes()

    identificacion = input("\nIngrese la identificación del cliente: ").strip()

    for cliente in clientes:
        if cliente["id"] == identificacion:
            print("\n========== CLIENTE ENCONTRADO ==========")
            print(f"ID: {cliente['id']}")
            print(f"Nombres: {cliente['nombres']}")
            print(f"Apellidos: {cliente['apellidos']}")
            print(f"Dirección: {cliente['direccion']}")
            print(f"Teléfono móvil: {cliente['telefono_movil']}")
            print(f"Teléfono fijo: {cliente['telefono_fijo']}")
            print(f"Estado: {cliente['estado']}")
            print(f"Nivel de riesgo: {cliente['nivel_riesgo']}")
            return

    print("Cliente no encontrado.")

def modificar_cliente():
    clientes = cargar_clientes()

    identificacion = input("\nIngrese la identificación del cliente: ").strip()

    for cliente in clientes:
        if cliente["id"] == identificacion:
            print("\nCliente encontrado.")
            print("Deje vacío el campo si no desea modificarlo.")

            nombres = input(f"Nombres [{cliente['nombres']}]: ").strip()
            apellidos = input(f"Apellidos [{cliente['apellidos']}]: ").strip()
            direccion = input(f"Dirección [{cliente['direccion']}]: ").strip()
            telefono_movil = input(f"Teléfono móvil [{cliente['telefono_movil']}]: ").strip()
            telefono_fijo = input(f"Teléfono fijo [{cliente['telefono_fijo']}]: ").strip()

            if nombres:
                cliente["nombres"] = nombres
            if apellidos:
                cliente["apellidos"] = apellidos
            if direccion:
                cliente["direccion"] = direccion
            if telefono_movil:
                cliente["telefono_movil"] = telefono_movil
            if telefono_fijo:
                cliente["telefono_fijo"] = telefono_fijo

            guardar_clientes(clientes)
            print("\nCliente modificado correctamente.")
            return

    print("Cliente no encontrado.")

def cambiar_estado():
    clientes = cargar_clientes()

    identificacion = input("\nIngrese la identificación del cliente: ").strip()

    for cliente in clientes:
        if cliente["id"] == identificacion:
            print("\nSeleccione el nuevo estado:")
            print("1. En proceso de inscripción")
            print("2. Inscrito")
            print("3. Activo")
            print("4. Inactivo")

            opcion = input("Seleccione una opción: ")

            estados = {
                "1": "En proceso de inscripción",
                "2": "Inscrito",
                "3": "Activo",
                "4": "Inactivo"
            }

            if opcion not in estados:
                print("Opción no válida.")
                return

            cliente["estado"] = estados[opcion]
            guardar_clientes(clientes)

            print("Estado actualizado correctamente.")
            return

    print("Cliente no encontrado.")

def cambiar_riesgo():
    clientes = cargar_clientes()

    identificacion = input("\nIngrese la identificación del cliente: ").strip()

    for cliente in clientes:
        if cliente["id"] == identificacion:
            print("\nSeleccione el nivel de riesgo:")
            print("1. Alto")
            print("2. Medio")
            print("3. Bajo")

            opcion = input("Seleccione una opción: ")

            riesgos = {
                "1": "Alto",
                "2": "Medio",
                "3": "Bajo"
            }

            if opcion not in riesgos:
                print("Opción no válida.")
                return

            cliente["nivel_riesgo"] = riesgos[opcion]
            guardar_clientes(clientes)

            print("Nivel de riesgo actualizado correctamente.")
            return

    print("Cliente no encontrado.")

def eliminar_cliente():
    clientes = cargar_clientes()

    identificacion = input("\nIngrese la identificación del cliente: ").strip()

    for cliente in clientes:
        if cliente["id"] == identificacion:
            confirmar = input(f"¿Está seguro de eliminar al cliente {cliente['nombres']} {cliente['apellidos']}? (s/n): ").lower()
            
            if confirmar == "s":
                clientes.remove(cliente)
                guardar_clientes(clientes)
                print("Cliente eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return

    print("Cliente no encontrado.")

def menu_clientes():
    while True:
        print("\n" + "=" * 40)
        print("       GESTIÓN DE CLIENTES")
        print("=" * 40)

        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Modificar cliente")
        print("5. Cambiar estado")
        print("6. Cambiar nivel de riesgo")
        print("7. Eliminar cliente")
        print("8. Volver")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            modificar_cliente()
        elif opcion == "5":
            cambiar_estado()
        elif opcion == "6":
            cambiar_riesgo()
        elif opcion == "7":
            eliminar_cliente()
        elif opcion == "8":
            break
        else:
            print("Opción no válida.")