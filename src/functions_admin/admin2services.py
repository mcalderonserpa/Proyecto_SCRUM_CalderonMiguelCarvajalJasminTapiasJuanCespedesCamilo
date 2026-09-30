from src.functions_utils.validaciones import pedir_entero
from src.functions_storage.storage import save_instructors
from src.functions_storage.storage import get_services
from src.functions_storage.storage import save_services
from src.functions_storage.storage import get_instructors

from src.functions_admin.admin2instructors import add_instructor

# FT04.02.01 Funcion add_service
# FT04.02.01 Funcion add_service
def add_service():
    services = get_services()
    service = input("Ingrese el nombre del servicio: ").strip().lower()
    if not service:
        print("El nombre del servicio no puede estar vacio.")
        return
    for registro in services:
        if registro['servicio'] == service:
            print(f"Ya existe el servicio: {service}")
            return
    cupos = pedir_entero("Ingrese el numero de cupos: ", minimo=1)
    instructores = [i for i in get_instructors() if i.get('estado', 'activo') == "activo"]
    if not instructores:
        print("No hay instructores activos. Por favor, registre un instructor.")
        add_instructor()
        instructores = [i for i in get_instructors() if i.get('estado', 'activo') == "activo"]
        if not instructores:
            return
    for n, instructor in enumerate(instructores, start=1):
        print(f"{n}. {instructor['nombre']}")
    opcion = pedir_entero("Seleccione el numero del instructor: ", 1, len(instructores))
    elegido = instructores[opcion - 1]
    todos = get_instructors()
    for instructor in todos:
        if instructor.get('id') == elegido.get('id'):
            instructor.setdefault('servicios', []).append(service)
    save_instructors(todos)
    services.append({"servicio": service, "cupos": cupos, "instructor": elegido['nombre'], "matriculas": []})
    save_services(services)
    print(f"Servicio {service} registrado.")


# FT04.02.02 Funcion modify_service
def show_services():
    services = get_services()
    if not services:
        print("No hay servicios registrados.")
    else:
        for service in services:
            print(f"\nServicio: {service['servicio']}\nCupos: {service['cupos']}\nInstructor: {service['instructor']}")

# FT04.02.03 Funcion modify_service
def modify_service():
    services = get_services()
    if not services:
        print("No hay servicios registrados.")
        return
    n = 1
    for service in services:
        print(f"{n}. Servicio: {service['servicio']}\nCupos: {service['cupos']}\nInstructor: {service['instructor']}")
        n += 1
    
    opcion = pedir_entero("Seleccione el numero del servicio que desea modificar: ", 1, len(services)) - 1
    services[opcion]['cupos'] += pedir_entero("Ingrese la cantidad de cupos que desea añadir o quitar (-): ")
    if services[opcion]['cupos'] < 0:
        print("No se puede tener cupos negativos. Se establecera en 0")
        services[opcion]['cupos'] = 0
    save_services(services)