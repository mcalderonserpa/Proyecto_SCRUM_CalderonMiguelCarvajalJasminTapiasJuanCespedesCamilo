def menu_principal():
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


def menu_clientes():
    print("\n--- MENU DE CLIENTES ---")
    print("1. Acceso Perfil")
    print("2. Registro de actividades")
    print("3. Seguimiento de progreso")
    print("4. Modificar datos")
    print("5. Solicitud de registro")
    print("6. Submenu de servicios")
    print("7. Volver al menu principal")


def submenu_servicios():
    print("\n--- MENU DE SERVICIOS ---")
    print("1. Matricular servicio")
    print("2. Retirar servicio")
    print("3. Listar servicios disponibles")
    print("4. Volver al menu principal")


def menu_instructores():
    print("\n--- GESTION DE INSTRUCTORES ---")
    print("1. Registrar asistencia y progreso")
    print("2. Listar instructores")
    print("3. Volver al menu principal")


def menu_administrador():
    print("\n--- ADMINISTRADOR ---")
    print("1. Gestionar matriculas")
    print("2. Gestionar servicios")
    print("3. Reportes")
    print("4. Volver al menu principal")


def submenu_matriculas():
    print("\n--- GESTION DE MATRICULAS ---")
    print("1. Matricular cliente")
    print("2. Listar matriculas")
    print("3. Registrar asistencia")
    print("4. Registrar progreso")
    print("5. Volver al menu principal")


def submenu_gestion_servicios():
    print("\n--- GESTION DE SERVICIOS ---")
    print("1. Registrar servicios")
    print("2. Listar servicios")
    print("3. Eliminar servicios")
    print("4. Volver al menu principal")


def submenu_reportes():
    print("\n--- REPORTES ---")
    print("1. Clientes inscritos")
    print("2. Servicios y capacidad")
    print("3. Instructores activos")
    print("4. Clientes con riesgo alto")
    print("5. Progreso de clientes")
    print("6. Volver al menu principal")