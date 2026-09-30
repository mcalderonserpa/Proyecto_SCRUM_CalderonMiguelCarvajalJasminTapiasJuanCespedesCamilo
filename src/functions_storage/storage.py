import json

# FT08.01.01 Funcion get_clients
def get_clients():
    try:
        with open('clients.json', 'r') as file:
            clients = json.load(file)
        return clients
    except FileNotFoundError:
        return []

# FT08.01.02 Funcion save_clients
def save_clients(clients):
    with open('clients.json', 'w') as file:
        json.dump(clients, file, indent=4)

# FT08.02.01 Funcion get_services
def get_services():
    try:
        with open('services.json', 'r') as file:
            services = json.load(file)
        return services
    except FileNotFoundError:
        return []

# FT08.02.02 Funcion save_services
def save_services(services):
    with open('services.json', 'w') as file:
        json.dump(services, file, indent=4)

# FT08.03.01 Funcion get_instructors
def get_instructors():
    try:
        with open('instructors.json', 'r') as file:
            instructors = json.load(file)
        return instructors
    except FileNotFoundError:
        instructors = [
            {
                "nombre": "Miguel",
                "servicio": None
            }
        ]

        return []

# FT08.03.02 Funcion save_instructors
def save_instructors(instructors):
    with open('instructors.json', 'w') as file:
        json.dump(instructors, file, indent=4)

# FT08.04.01 Funcion get_attendance
def get_attendance():
    try:
        with open('asistencias.json', 'r') as file:
            asistencias = json.load(file)
        return asistencias
    except FileNotFoundError:
        return []

# FT08.04.02 Funcion save_attendance
def save_attendance(asistencias):
    with open('asistencias.json', 'w') as file:
        json.dump(asistencias, file, indent=4)

# FT08.04.03 Funcion get_evaluations
def get_evaluations():
    try:
        with open('evaluaciones.json', 'r') as file:
            evaluaciones = json.load(file)
        return evaluaciones
    except FileNotFoundError:
        return []

# FT08.04.04 Funcion save_evaluations
def save_evaluations(evaluaciones):
    with open('evaluaciones.json', 'w') as file:
        json.dump(evaluaciones, file, indent=4)