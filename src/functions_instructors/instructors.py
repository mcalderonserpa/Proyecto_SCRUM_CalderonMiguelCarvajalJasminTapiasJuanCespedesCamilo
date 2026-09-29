from datetime import date, datetime

from src.functions_storage.storage import get_instructors
from src.functions_storage.storage import get_services
from src.functions_storage.storage import get_clients
from src.functions_storage.storage import get_attendance
from src.functions_storage.storage import save_attendance
from src.functions_storage.storage import get_evaluations
from src.functions_storage.storage import save_evaluations
from src.functions_menu.menus import menu_instructors

PENALIZACION_INASISTENCIA = 0.1
CALIFICACION_MIN = 0.1
CALIFICACION_MAX = 10
UMBRAL_BAJO = 5.0   
UMBRAL_ALTO = 7.0

# ---------------------------------------------------------------------
# FT03.03 Inicio de sesion del instructor
# ---------------------------------------------------------------------

# FT03.03.01 Funcion login_instructor
def login_instructor():
    instructores = get_instructors()
    if not instructores:
        print("No hay instructores registrados. Solicite al administrador que lo registre.")
        return None
    try:
        id_instructor = int(input("Ingrese su ID de instructor: "))
    except ValueError:
        print("El ID debe ser un numero.")
        return None
    for instructor in instructores:
        if instructor.get('id') == id_instructor:
            if instructor.get('estado', 'activo') != "activo":
                print("Su usuario de instructor esta inactivo.")
                return None
            print(f"\nBienvenido(a), {instructor['nombre'].title()}.")
            return instructor
    print(f"No se encuentra el instructor con el ID: {id_instructor}")
    return None