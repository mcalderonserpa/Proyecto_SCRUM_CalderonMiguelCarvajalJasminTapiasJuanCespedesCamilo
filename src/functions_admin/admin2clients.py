from src.functions_storage.storage import get_clients
from src.functions_storage.storage import save_clients
from src.functions_storage.storage import get_services
from src.functions_storage.storage import save_services

# FT04.01.01 Funcion add_client
def add_client():
    clients = get_clients()
    id_cliente = int(input("Ingrese el ID del cliente: "))
    nombres_cliente = input("Ingrese los nombres del cliente: ")
    apellidos_cliente = input("Ingrese los apellidos del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")
    telefono_movil_cliente = input("Ingrese el teléfono móvil del cliente: ")
    telefono_fijo_cliente = input("Ingrese el teléfono fijo del cliente: ")
    estado_cliente = input("Ingrese el estado del cliente: ")
    nivel_riesgo_cliente = input("Ingrese el nivel de riesgo del cliente: ")
    registro = {
        "id": id_cliente,
        "nombres": nombres_cliente,
        "apellidos": apellidos_cliente,
        "direccion": direccion_cliente,
        "telefono_movil": telefono_movil_cliente,
        "telefono_fijo": telefono_fijo_cliente,
	    "estado": estado_cliente,
	    "nivel_riesgo": nivel_riesgo_cliente,
        "servicios" : []
    }
    clients.append(registro)
    save_clients(clients)

# FT04.01.02 Funcion enroll_client
def enroll_client():
    clients = get_clients()
    servicios = get_services()
    id = int(input("Ingrese el ID del cliente que desea matricular: "))
    for cliente in clients:
        if cliente['id'] == id:
            servicio_matricula = input("Ingrese el servicio: ")
            for servicio in servicios:
                if servicio['servicio'] == servicio_matricula:
                    found = True
                    if servicio['cupos'] > 0:
                        servicio['cupos'] -= 1
                        fecha_inicio = input("Ingrese la fecha de inicio: ")
                        fecha_fin = input("Ingrese la fecha de finalizacion: ")
                        riesgo = cliente['nivel_riesgo']
                        servicio['matriculas'].append({
                            "id": cliente['id'],
                            "fecha_inicio": fecha_inicio,
                            "fecha_fin": fecha_fin,
                            "riesgo": riesgo
                        })
                        save_services(servicios)
                        cliente['servicios'].append({
                            "servicio": servicio['servicio'],
                            "fecha_inicio": fecha_inicio,
                            "fecha_fin": fecha_fin
                        })
                        save_clients(clients)
                    else:
                        print(f"No hay cupos disponibles para el servicio: {servicio['servicio']}")
                        break
            if not found:
                print("Servicio no encontrado.")
                break
        else: 
            print(f"No se encuentra el cliente con el ID: {id}")    

# FT04.01.03 Funcion show_clients
def show_clients():
    clientes = get_clients()
    if not clientes:
        print("No hay registros de clientes.")
    else:
        for registro in clientes:
            print(f"\nID: {registro['id']}\nNombres: {registro['nombres']}\nApellidos: {registro['apellidos']}\nDirección: {registro['direccion']}\nTeléfono Móvil: {registro['telefono_movil']}\nTeléfono Fijo: {registro['telefono_fijo']}\nEstado: {registro['estado']}\nNivel de Riesgo: {registro['nivel_riesgo']}")
