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
FORMATO_FECHA = "%d-%m-%Y"

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

# FT03.01 Registro periodico del instructor /  FT03.01.02 Asistencia

# Funcion auxiliar pedir_fecha
def pedir_fecha(mensaje="Ingrese la fecha (DD-MM-AAAA) o Enter para hoy: "):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            return date.today().strftime(FORMATO_FECHA)
        try:
            return datetime.strptime(texto, FORMATO_FECHA).strftime(FORMATO_FECHA)
        except ValueError:
            print("Formato de fecha invalido. Use DD-MM-AAAA.")            
            
def servicios_de_instructor(instructor):
    servicios = []
    for servicio in get_services():
        if servicio['instructor'] == instructor['nombre'] or servicio['servicio'] in instructor.get('servicios', []):
            servicios.append(servicio)
            return servicios

def seleccionar_servicio(instructor):
    servicios = servicios_de_instructor(instructor)
    if not servicios:
        print("No tiene servicios asignados.")
        return None
    print("\nSus servicios:")
    for i, servicio in enumerate(servicios, start=1):
        print(f"{i}. {servicio['servicio']} ({len(servicio['matriculas'])} matriculados)")
    try:
        opcion = int(input("Seleccione el numero del servicio: ")) - 1
        if opcion < 0:
            raise IndexError
        return servicios[opcion]
    except (ValueError, IndexError):
        print("Opcion no valida.")
        return None

def buscar_cliente(id_cliente):
    for cliente in get_clients():
        if cliente['id'] == id_cliente:
            return cliente
    return None

def nombre_cliente(id_cliente):
    cliente = buscar_cliente(id_cliente)
    if cliente is None:
        return f"Cliente {id_cliente} (no registrado)"
    return f"{cliente['nombres']} {cliente['apellidos']}"
    

# FT03.01.02 Funcion registrar_asistencia

def registrar_asistencia(instructor):
    servicio = seleccionar_servicio(instructor)
    if servicio is None:
        return
    if not servicio['matriculas']:
        print(f"No hay clientes matriculados en {servicio['servicio']}.")
        return

    fecha = pedir_fecha()
    asistencias = get_attendance()

    for sesion in asistencias:
        if sesion['servicio'] == servicio['servicio'] and sesion['fecha'] == fecha:
            print(f"Ya se registro la asistencia de {servicio['servicio']} para el {fecha}.")
            return

    asistentes = []
    ausentes = []
    print(f"\nAsistencia de {servicio['servicio']} - {fecha}  (SI = asistio, NO = no asistio)")
    for matricula in servicio['matriculas']:
        while True:
            respuesta = input(f"  [{matricula['id']}] {nombre_cliente(matricula['id'])}: ").strip().upper()
            respuesta = respuesta.replace("Í", "I")
            if respuesta in ("SI", "NO"):
                break
            print("  Responda SI o NO.")
        if respuesta == "SI":
            asistentes.append(matricula['id'])
        else:
            ausentes.append(matricula['id'])

    asistencias.append({
        "servicio": servicio['servicio'],
        "id_instructor": instructor['id'],
        "fecha": fecha,
        "asistentes": asistentes,
        "ausentes": ausentes
    })
    save_attendance(asistencias)
    print(f"\nAsistencia guardada: {len(asistentes)} asistentes, {len(ausentes)} ausentes.") 


# Funcion auxiliar resumen_asistencia    
def resumen_asistencia(id_cliente, nombre_servicio=None):
    asistio = 0
    falto = 0
    for sesion in get_attendance():
        if nombre_servicio is not None and sesion['servicio'] != nombre_servicio:
            continue
        if id_cliente in sesion['asistentes']:
            asistio += 1
        elif id_cliente in sesion['ausentes']:
            falto += 1
    total = asistio + falto
    porcentaje = round(asistio * 100 / total, 1) if total > 0 else None
    return {"asistencias": asistio, "inasistencias": falto, "sesiones": total, "porcentaje": porcentaje}


# FT03.01.03 Calculo del score de rendimiento

# Funcion auxiliar evaluaciones_cliente
def evaluaciones_cliente(id_cliente, nombre_servicio=None):
    lista = []
    for evaluacion in get_evaluations():
        if evaluacion['id_cliente'] != id_cliente:
            continue
        if nombre_servicio is not None and evaluacion['servicio'] != nombre_servicio:
            continue
        lista.append(evaluacion)
    lista.sort(key=lambda e: datetime.strptime(e['fecha'], FORMATO_FECHA))
    return lista

# Funcion auxiliar clasificar_rendimiento
def clasificar_rendimiento(score):
    if score is None:
        return "sin evaluar"
    if score < UMBRAL_BAJO:
        return "bajo"
    if score < UMBRAL_ALTO:
        return "medio"
    return "alto"

# score = (suma de calificaciones / numero de evaluaciones) - 0.1 * inasistencias
def calcular_score(id_cliente, nombre_servicio=None):
    evaluaciones = evaluaciones_cliente(id_cliente, nombre_servicio)
    asistencia = resumen_asistencia(id_cliente, nombre_servicio)

    if not evaluaciones:
        promedio = None
        score = None
    else:
        suma = 0
        for evaluacion in evaluaciones:
            suma += evaluacion['calificacion']
        promedio = suma / len(evaluaciones)
        score = promedio - PENALIZACION_INASISTENCIA * asistencia['inasistencias']
        score = round(max(0, min(CALIFICACION_MAX, score)), 2)
        promedio = round(promedio, 2)

    return {
        "promedio": promedio,
        "evaluaciones": len(evaluaciones),
        "inasistencias": asistencia['inasistencias'],
        "porcentaje_asistencia": asistencia['porcentaje'],
        "score": score,
        "nivel": clasificar_rendimiento(score)
    }

# FT03.01.01 Registro de evaluaciones

# Funcion auxiliar pedir_calificacion
def pedir_calificacion():
    while True:
        try:
            nota = float(input(f"Ingrese la calificacion ({CALIFICACION_MIN} a {CALIFICACION_MAX}): ").replace(",", "."))
        except ValueError:
            print("Debe ingresar un numero.")
            continue
        if CALIFICACION_MIN <= nota <= CALIFICACION_MAX:
            return round(nota, 1)
        print(f"La calificacion debe estar entre {CALIFICACION_MIN} y {CALIFICACION_MAX}.")

# Funcion auxiliar seleccionar_cliente_de_servicio
def seleccionar_cliente_de_servicio(servicio):
    matriculas = servicio['matriculas']
    if not matriculas:
        print(f"No hay clientes matriculados en {servicio['servicio']}.")
        return None
    print(f"\nClientes de {servicio['servicio']}:")
    for i, matricula in enumerate(matriculas, start=1):
        print(f"{i}. [{matricula['id']}] {nombre_cliente(matricula['id'])}")
    try:
        opcion = int(input("Seleccione el numero del cliente: ")) - 1
        if opcion < 0:
            raise IndexError
        return matriculas[opcion]['id']
    except (ValueError, IndexError):
        print("Opcion no valida.")
        return None

def registrar_evaluacion(instructor):
    servicio = seleccionar_servicio(instructor)
    if servicio is None:
        return
    id_cliente = seleccionar_cliente_de_servicio(servicio)
    if id_cliente is None:
        return

    fecha = pedir_fecha()
    calificacion = pedir_calificacion()
    observaciones = input("Observaciones (opcional): ").strip()

    evaluaciones = get_evaluations()
    evaluaciones.append({
        "id_cliente": id_cliente,
        "servicio": servicio['servicio'],
        "id_instructor": instructor['id'],
        "fecha": fecha,
        "calificacion": calificacion,
        "observaciones": observaciones
    })
    save_evaluations(evaluaciones)

    resultado = calcular_score(id_cliente, servicio['servicio'])
    print(f"\nEvaluacion guardada. Score actual en {servicio['servicio']}: "
          f"{resultado['score']} ({resultado['nivel']})")