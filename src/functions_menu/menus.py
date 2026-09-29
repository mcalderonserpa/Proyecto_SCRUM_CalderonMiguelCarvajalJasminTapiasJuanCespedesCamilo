# FT
def menu_main():
    print("\n" + "=" * 40)
    print("       GIMNASIO FORCE TECH")
    print("       MENU PRINCIPAL")
    print("=" * 40)
    print("1. Modulo de clientes")
    print("2. Modulo de instructores")
    print("3. Modulo de administrador")
    print("4. Modulo de reportes")
    print("5. Salir")
    print("=" * 40)

# FT
def menu_clients():
    print("\n--- MODULO DE CLIENTES ---")
    print("1. Solicitud nuevo registro")
    print("2. Ver perfil")
    print("3. Volver al menu principal")

# FT
def submenu_profile():
    print("\n--- PERFIL ---")
    print("1. Ver datos de perfil")
    print("2. Ver servicios matriculados")
    print("3. Seguimiento de proceso")
    print("4. Modificar datos")
    print("5. Submenu de servicios")
    print("6. Volver al menu de clientes")

# FT
def menu_instructors():
    print("\n--- MODULO DE INSTRUCTORES ---")
    print("1. Evaluacion periodica")
    print("2. Listar instructores")
    print("3. Volver al menu principal")

# FT
def menu_admin():
    print("\n--- ADMINISTRADOR ---")
    print("1. Admitir inscripciones clientes")
    print("2. Listar clientes")
    print("3. Gestion de servicios")
    print("4. Gestion de instructores")
    print("5. Volver al menu principal")

# FT
def submenu_services_admin():
    print("\n--- ADMINISTRADOR: GESTION DE SERVICIOS ---")
    print("1. Registrar servicio")
    print("2. Listar servicios")
    print("3. Modificar servicio")
    print("4. Volver al menu principal")

# FT
def submenu_instructors_admin():
    print("\n--- ADMINISTRADOR: GESTION DE INSTRUCTORES ---")
    print("1. Registrar instructor")
    print("2. Listar instructores")
    print("3. Eliminar instructor")
    print("4. Volver al menu principal")

# FT
def submenu_reports():
    print("\n--- MODULO REPORTES ---")
    print("1. Clientes inscritos")
    print("2. Servicios y capacidad")
    print("3. Instructores activos")
    print("4. Clientes con riesgo alto")
    print("5. Progreso de clientes")
    print("6. Volver al menu principal")