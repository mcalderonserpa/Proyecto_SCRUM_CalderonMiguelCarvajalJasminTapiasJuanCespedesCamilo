import json


# Lee un JSON; si no existe, esta vacio o danado devuelve [] sin cerrar el programa
def leer_json(ruta):
    try:
        with open(ruta, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Aviso: el archivo {ruta} esta vacio o danado. Se usara una lista vacia.")
        return []

# FT08.01.01 Funcion get_clients
def get_clients():
    return leer_json('clients.json')

# FT08.01.02 Funcion save_clients
def save_clients(clients):
    with open('clients.json', 'w') as file:
        json.dump(clients, file, indent=4)

# FT08.02.01 Funcion get_services
def get_services():
    return leer_json('services.json')

# FT08.02.02 Funcion save_services
def save_services(services):
    with open('services.json', 'w') as file:
        json.dump(services, file, indent=4)

# FT08.03.01 Funcion get_instructors
def get_instructors():
    return leer_json('instructors.json')

# FT08.03.02 Funcion save_instructors
def save_instructors(instructors):
    with open('instructors.json', 'w') as file:
        json.dump(instructors, file, indent=4)

# FT08.04.01 Funcion get_attendance
def get_attendance():
    return leer_json('asistencias.json')

# FT08.04.02 Funcion save_attendance
def save_attendance(asistencias):
    with open('asistencias.json', 'w') as file:
        json.dump(asistencias, file, indent=4)

# FT08.04.03 Funcion get_evaluations
def get_evaluations():
    return leer_json('evaluaciones.json')

# FT08.04.04 Funcion save_evaluations
def save_evaluations(evaluaciones):
    with open('evaluaciones.json', 'w') as file:
        json.dump(evaluaciones, file, indent=4)