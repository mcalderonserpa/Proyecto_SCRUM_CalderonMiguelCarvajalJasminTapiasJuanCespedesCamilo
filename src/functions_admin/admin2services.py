from src.functions_storage.storage import get_services
from src.functions_storage.storage import save_services

# FT04.02.01 Funcion add_service
def add_service():
    services = get_services()
    service = input("Ingrese el nombre del servicio: ").lower()
    cupos = int(input("Ingrese el numero de cupos: "))
    instructor = input("Ingrese el nombre del instructor: ").lower()
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