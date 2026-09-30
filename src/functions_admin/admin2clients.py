from src.functions_utils.validaciones import pedir_fecha
from src.functions_storage.storage import get_clients
from src.functions_storage.storage import save_clients
from src.functions_storage.storage import get_services
from src.functions_storage.storage import save_services


# FT04.01.01 Funcion add_client
def accept_client():
    clients = get_clients()
    pendientes = [c for c in clients if c['estado'] == "En proceso de inscripción"]
    if not pendientes:
        print("No hay solicitudes de inscripcion pendientes.")
        return
    for cliente in clients:
        if cliente['estado'] == "En proceso de inscripción":
            print("Cliente en proceso de inscripción: ", cliente['nombres'], cliente['apellidos'])
            opcion = input("¿Desea aceptar el cliente? (s/n): ")
            if opcion.lower() == "s":
                cliente['estado'] = "Inscrito"
                save_clients(clients)
                print("Cliente aceptado exitosamente.")
            elif opcion.lower() == "n":
                print("Cliente no aceptado.")
            else:
                print("Opcion no valida.")
                break
            
            

# FT04.01.02 Funcion enroll_client
def enroll_client(id):
    clients = get_clients()
    servicios = get_services()
    cliente = None
    for registro in clients:
        if str(registro['id']) == str(id):
            cliente = registro
            break
    if cliente is None:
        print(f"No se encuentra el cliente con el ID: {id}")
        return
    if cliente['estado'] not in ("Inscrito", "Activo"):
        print("El cliente debe ser aceptado por el administrador antes de matricularse.")
        return

    nombre_servicio = input("Ingrese el servicio: ").strip().lower()
    servicio = None
    for registro in servicios:
        if registro['servicio'] == nombre_servicio:
            servicio = registro
            break
    if servicio is None:
        print("Servicio no encontrado.")
        return
    for matricula in servicio['matriculas']:
        if str(matricula['id']) == str(cliente['id']):
            print(f"El cliente ya esta matriculado en {servicio['servicio']}.")
            return
    if servicio['cupos'] <= 0:
        print(f"No hay cupos disponibles para el servicio: {servicio['servicio']}")
        return

    fecha_inicio = pedir_fecha("Ingrese la fecha de inicio (DD-MM-AAAA): ")
    fecha_fin = pedir_fecha("Ingrese la fecha de finalizacion (DD-MM-AAAA): ")
    servicio['cupos'] -= 1
    servicio['matriculas'].append({
        "id": cliente['id'],
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "riesgo": cliente['nivel_riesgo']
    })
    save_services(servicios)
    print(f"Matricula en {servicio['servicio']} registrada.")


# FT04.01.03 Funcion show_clients
def show_clients():
    clientes = get_clients()
    if not clientes:
        print("No hay registros de clientes.")
    else:
        for registro in clientes:
            print(f"\nID: {registro['id']}\nNombres: {registro['nombres']}\nApellidos: {registro['apellidos']}\nDirección: {registro['direccion']}\nTeléfono Móvil: {registro['telefono_movil']}\nTeléfono Fijo: {registro['telefono_fijo']}\nEstado: {registro['estado']}\nNivel de Riesgo: {registro['nivel_riesgo']}")
