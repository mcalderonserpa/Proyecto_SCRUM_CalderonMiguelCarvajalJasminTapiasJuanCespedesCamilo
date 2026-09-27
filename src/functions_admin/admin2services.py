from src.functions_storage.storage import save_instructors
from src.functions_storage.storage import get_services
from src.functions_storage.storage import save_services
from src.functions_storage.storage import get_instructors

from src.functions_admin.admin2instructors import add_instructor

# FT04.02.01 Funcion add_service
def add_service():
    services = get_services()
    service = input("Ingrese el nombre del servicio: ").lower()
    cupos = int(input("Ingrese el numero de cupos: "))
    instructores = get_instructors()
    if instructores == []:
        print("No hay instructores registrados. Por favor, registre un instructor.")
        add_instructor()
        instructores = get_instructors()
    i = 1
    for instructor in instructores:
        print(f"{i}. {instructor['nombre']}")
        i += 1
    opcion = int(input("Seleccione el numero del instructor: ")) - 1
    instructor = instructores[opcion]['nombre']
    instructores[opcion]['servicios'].append(service)
    save_instructors(instructores)
    registro = {
        "servicio" : service ,
        "cupos" : cupos,
        "instructor" : instructor,
        "matriculas" : []
    }
    services.append(registro)
    save_services(services)

# FT04.02.02 Funcion modify_service
def modify_service():
    services = get_services()
    service = input("Ingrese el nombre del servicio que desea modificar: ").lower()
    for service in services:
        if service['servicio'] == service:
            cupos_adicionales = int(input("Ingrese la cantidad de cupos que desea añadir o quitar (-): "))
            service['cupos'] += cupos_adicionales
            instructor = input("Ingrese el nuevo nombre del instructor: ").lower()
            service['instructor'] = instructor
            save_services(services)
            break
