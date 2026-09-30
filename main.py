from src.functions_menu.menus import menu_main
from src.functions_menu.menus import menu_clients
from src.functions_menu.menus import menu_instructors
from src.functions_menu.menus import menu_admin
from src.functions_menu.menus import submenu_profile
from src.functions_menu.menus import submenu_services_admin
from src.functions_menu.menus import submenu_reports
from src.functions_menu.menus import submenu_instructors_admin

from src.functions_admin.admin2clients import accept_client  
from src.functions_admin.admin2clients import show_clients
from src.functions_admin.admin2clients import enroll_client
from src.functions_admin.admin2services import add_service
from src.functions_admin.admin2services import show_services
from src.functions_admin.admin2services import modify_service
from src.functions_admin.admin2instructors import add_instructor

from src.functions_instructors.instructors import instructor_menu
from src.functions_instructors.instructors import listar_instructores_activos
from src.functions_instructors.instructors import eliminar_instructor


from src.functions_clients.clientes import registrar_cliente

def main():
    start = True
    while start:
        menu_main() # Menu principal
        opcion = input("\nSeleccione una opcion: ")

        match opcion:
            case "1": # 1. Modulo clientes
                start2 = True
                while start2:
                    menu_clients() 
                    opcion2 = input("\nSeleccione una opcion: ")

                    match opcion2:
                        case "1": # 1.1 Nuevo Registro
                            registrar_cliente()
                        case "2": # 1.2 Entrar al perfil
                            enroll_client()
                        case "3": # 1.3 Volver al menu principal
                            start2 = False
                            print("Volviendo al menu principal...")
                        case _:
                            print("Opcion no valida. Intente nuevamente.")

            case "2": # 2. modulo instructores
                menu_instructors()
                instructor_menu()
                    

            case "3": # 3. modulo ADMIN
                start2 = True
                while start2:
                    menu_admin()
                    opcion2 = input("\nSeleccione una opcion: ")

                    match opcion2:
                        case "1": # 3.1 Admitir inscripciones
                            accept_client()

                        case "2": # 3.2 Listar clientes
                            show_clients()

                        case "3": # 3.3 Gestionar servicios
                            start3 = True
                            while start3:
                                submenu_services_admin()
                                opcion3 = input("\nSeleccione una opcion: ")

                                match opcion3:
                                    case "1": # 3.3.1 Nuevo Servicio
                                        add_service()

                                    case "2": # 3.3.2 Listar servicios
                                        show_services()

                                    case "3": # 3.3.3 Modificar servicios
                                        modify_service()

                                    case "4": # 3.3.4 Volver al menu de admin
                                        start3 = False
                                        print("Volviendo al menu principal...")

                                    case _:
                                        print("Opcion no valida. Intente nuevamente.")

                        case "4": # 3.4 Gestionar instructores
                            start3 = True
                            while start3:
                                submenu_instructors_admin()
                                opcion3 = input("\nSeleccione una opcion: ")

                                match opcion3:
                                    case "1": # 3.4.1 Nuevo instructor
                                        add_instructor()

                                    case "2": # 3.4.2 Listar instructores
                                        listar_instructores_activos()

                                    case "3": # 3.4.3 Eliminar instructor
                                        eliminar_instructor()

                                    case "4": # 3.4.4 Volver al menu de admin
                                        start3 = False
                                        print("Volviendo al menu principal...")

                                    case _:
                                        print("Opcion no valida. Intente nuevamente.")

                        case "5": # 3.5 Volver al menu principal
                            start2 = False
                            print("Gracias por utilizar Gimnasio ForceTech.")

                        case _:
                            print("Opcion no valida. Intente nuevamente.")

            case "4": # 4. Menu reportes
                submenu_reports()
                print("En Construccion")

            case "4": # 4. Menu reportes
                start2 = True
                while start2:
                    submenu_reports()
                    opcion2 = input("\nSeleccione una opcion: ")

                    match opcion2:
                        case "1": # 4.1 Clientes inscritos
                            show_clients()

                        case "2": # 4.2 Servicios y capacidad
                            show_services()

                        case "3": # 4.3 Instructores activos
                            listar_instructores_activos()

                        case "4": # 4.4 Clientes con riesgo alto
                            print("En Construccion")

                        case "5": # 4.5 progreso clientes
                            print("En Construccion")

                        case "6": # 4.6 Volver al menu principal
                            start2 = False
                            print("Volviendo al menu principal...")

                        case _:
                            print("Opcion no valida. Intente nuevamente.")

            case "5": # 5. Salir
                start = False
                print("Gracias por utilizar Gimnasio ForceTech.")

            case _:
                print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    main()
