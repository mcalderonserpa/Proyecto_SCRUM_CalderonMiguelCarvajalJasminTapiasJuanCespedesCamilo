def menu_main():
    print("\n" + "=" * 40)
    print("       GIMNASIO FORCE TECH")
    print("       SISTEMA DE GESTION")
    print("=" * 40)
    print("1. Menu de clientes")
    print("2. Menu de servicios")
    print("3. Menu de instructores")
    print("4. ADMINISTRADOR")
    print("5. Reportes")
    print("6. Salir")
    print("=" * 40)

def menu_clients():
    print("\n--- MENU DE CLIENTES ---")
    print("1. Acceso Perfil")
    print("2. Registro de actividades")
    print("3. Seguimiento de progreso")
    print("4. Modificar datos")
    print("5. Solicitud de registro")
    print("6. Submenu de servicios")
    print("7. Volver al menu principal")


def submenu_services_clients():
    print("\n--- MENU DE SERVICIOS ---")
    print("1. Matricular servicio")
    print("2. Retirar servicio")
    print("3. Listar servicios disponibles")
    print("4. Volver al menu principal")


def menu_instructors():
    print("\n--- MENU DE INSTRUCTORES ---")
    print("1. Registrar asistencia y progreso")
    print("2. Listar instructores")
    print("3. Volver al menu principal")


def menu_admin():
    print("\n--- ADMINISTRADOR ---")
    print("1. Gestionar matriculas")
    print("2. Gestionar servicios")
    print("3. Gestionar instructores")
    print("4. Reportes")
    print("5. Volver al menu principal")


def submenu_enrollments():
    print("\n--- GESTION DE MATRICULAS ---")
    print("1. Registrar cliente")
    print("2. Listar clientes")
    print("3. Matricular cliente a un servicio")
    print("4. Retirar servicio")
    print("5. Volver al menu principal")

def submenu_services_admin():
    print("\n--- GESTION DE SERVICIOS ---")
    print("1. Registrar servicios")
    print("2. Listar servicios")
    print("3. Eliminar servicios")
    print("4. Volver al menu principal")

def submenu_instructors_admin():
    print("\n--- GESTION DE INSTRUCTORES ---")
    print("1. Registrar instructor")
    print("2. Listar instructores")
    print("3. Eliminar instructor")
    print("4. Volver al menu principal")

def submenu_reports():
    print("\n--- REPORTES ---")
    print("1. Clientes inscritos")
    print("2. Servicios y capacidad")
    print("3. Instructores activos")
    print("4. Clientes con riesgo alto")
    print("5. Progreso de clientes")
    print("6. Volver al menu principal")