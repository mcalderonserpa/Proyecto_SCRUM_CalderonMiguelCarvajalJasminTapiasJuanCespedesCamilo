from src.functions_storage.storage import get_instructors
from src.functions_storage.storage import save_instructors
from src.functions_storage.storage import get_services

def add_instructor():
    instructors = get_instructors()
    servicios = get_services()

    nombre = input("Ingrese el nombre del instructor: ").lower()

    instructor = {
        "nombre": nombre,
        "servicios": []
    }

    for servicio in servicios:
        if servicio['instructor'] == instructor['nombre']:
            instructor['servicios'].append(servicio['servicio'])

    instructors.append(instructor)
    
    save_instructors(instructors)
