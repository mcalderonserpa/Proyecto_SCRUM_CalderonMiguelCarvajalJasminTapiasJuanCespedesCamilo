from src.functions_menu.menus import menu_main
from src.functions_menu.menus import menu_clients
from src.functions_menu.menus import menu_instructors
from src.functions_menu.menus import menu_admin
from src.functions_menu.menus import submenu_enrollments
from src.functions_menu.menus import submenu_services_clients
from src.functions_menu.menus import submenu_services_admin
from src.functions_menu.menus import submenu_reports
from src.functions_menu.menus import submenu_instructors_admin

from src.functions_admin.admin2clients import add_client
from src.functions_admin.admin2clients import show_clients
from src.functions_admin.admin2clients import enroll_client
from src.functions_admin.admin2services import add_service
from src.functions_admin.admin2instructors import add_instructor

def main():
    start = True
    while start:
        menu_main()
        opcion = input("\nSeleccione una opcion: ")

        match opcion:
            case "1": # 1. modulo clientes
                menu_clients()
                print("En Construccion")

            case "2": # 2. modulo instructores
                menu_instructors()
                print("En Construccion")

            case "3": # 3. modulo ADMIN
                start2 = True
                while start2:
                    menu_admin()
                    opcion2 = input("\nSeleccione una opcion: ")

                    match opcion2:
                        case "1": # 3.1 Admitir inscripciones
                            print("En construccion")
                            
                        case "2": # 3.2 Listar clientes
                            show_clients()

                        case "3": # 3.3 Gestion de servicios
                            submenu_services_admin()
                            opcion3 = input("\nSeleccione una opcion: ")

                            match opcion3:
                                case "1": # 3.3.1 Registrar servicios
                                    add_service()

                                case "2": # 3.3.2 Listar servicios
                                    print("En Construccion")
                                    

                                case "3": # 3.3.3 Modificar servicios
                                    print("En Construccion")

                                case "4":
                                    print("Volviendo al menu ADMIN")

                                case _:
                                    print("Opcion no valida. Intente nuevamente.")

                        case "4": # 3.4 Gestion de instructores
                            submenu_reports()
                            opcion3 = input("\nSeleccione una opcion: ")

                            match opcion3:
                                case "1": # 3.4.1 Registrar instructor
                                    print("En Construccion")

                                case "2": # 3.4.2 Listar instructores
                                    print("En Construccion")

                                case "3": # 3.4.3 Eliminar instructor
                                    print("En Construccion")

                                case "4": # 3.4.4 Volver al menu principal
                                    print("Volviendo al menu ADMIN")

                                case _:
                                    print("Opcion no valida. Intente nuevamente.")

                        case "5": # 3.5 Volver al menu principal
                            start2 = False
                            print("\n Volviendo al menu principal.")

                        case _:
                            print("Opcion no valida. Intente nuevamente.")

            case "4": # 4. Modulo reportes
                submenu_reports()
                print("En Construccion")

            case "5": # 5. Salir
                start = False
                print("Gracias por utilizar Gimnasio ForceTech.")

            case _:
                print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    main()
