from src.functions_storage.storage import get_instructors
from src.functions_storage.storage import save_instructors
from src.functions_storage.storage import get_services

# FT04.03.01 Funcion add_instructor
def add_instructor():
    instructors = get_instructors()
    servicios = get_services()
    
    try:
        id_instructor = int(input("Ingrese la cedula del instructor: "))
    except ValueError:
        print("La cedula debe ser un numero.")
        return

    for registro in instructors:
        if registro.get('id') == id_instructor:
            print(f"Ya existe un instructor con el ID: {id_instructor}")
            return

    nombre = input("Ingrese el nombre del instructor: ").strip().lower()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    for registro in instructors:
        if registro['nombre'] == nombre:
            print(f"Ya existe un instructor llamado {nombre}.")
            return
        
    
    telefono = input("Ingrese el telefono del instructor: ").strip()
    especialidad = input("Ingrese la especialidad del instructor: ").strip().lower()

        
    instructor = {
        "id": id_instructor,
        "nombre": nombre,
        "telefono": telefono,
        "especialidad": especialidad,
        "estado": "activo",
        "servicios": []
    }


    for servicio in servicios:
        if servicio['instructor'] == instructor['nombre']:
            instructor['servicios'].append(servicio['servicio'])
            
    instructors.append(instructor)
    save_instructors(instructors)
    print(f"Instructor {nombre} registrado con exito.")
