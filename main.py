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
from src.functions_instructors.instructores import add_instructor

def main():
    start = True
    while start:
        menu_main()
        opcion = int(input("\nSeleccione una opcion: "))

        match opcion:
            case 1:
                menu_clients()
                print("En Construccion")

            case 2:
                submenu_services_clients()
                print("En Construccion")

            case 3:
                menu_instructors()
                print("En Construccion")

            case 4:
                start2 = True
                while start2:
                    menu_admin()
                    opcion2 = int(input("\nSeleccione una opcion: "))

                    match opcion2:
                        case 1:
                            submenu_enrollments()
                            opcion3 = int(input("\nSeleccione una opcion: "))

                            match opcion3:
                                case 1:
                                    add_client()
                                case 2:
                                    show_clients()
                                case 3:
                                    enroll_client()
                                case 4:
                                    print("Volviendo al menu principal...")
                                case _:
                                    print("Opcion no valida. Intente nuevamente.")

                        case 2:
                            submenu_services_admin()
                            opcion3 = int(input("\nSeleccione una opcion: "))

                            match opcion3:
                                case 1:
                                    add_service()
                                case 2:
                                    print("En Construccion")
                                case 3:
                                    print("En Construccion")
                                case 4:
                                    print("Volviendo al menu principal...")
                                case _:
                                    print("Opcion no valida. Intente nuevamente.")

                        case 3:
                            submenu_instructors_admin()
                            opcion3 = int(input("\nSeleccione una opcion: "))

                            match opcion3:
                                case 1:
                                    add_instructor()
                                case 2:
                                    print("En Construccion")
                                case 3:
                                    print("En Construccion")
                                case 4:
                                    print("Volviendo al menu principal...")
                                case _:
                                    print("Opcion no valida. Intente nuevamente.")

                        case 4:
                            submenu_reports()
                            opcion3 = int(input("\nSeleccione una opcion: "))

                            match opcion3:
                                case 1:
                                    print("En Construccion")
                                case 2:
                                    print("En Construccion")
                                case 3:
                                    print("En Construccion")
                                case 4:
                                    print("En Construccion")
                                case 5:
                                    print("En Construccion")
                                case 6:
                                    print("Volviendo al menu principal...")
                                case _:
                                    print("Opcion no valida. Intente nuevamente.")

                        case 5:
                            start2 = False
                            print("Gracias por utilizar Gimnasio ForceTech.")

                        case _:
                            print("Opcion no valida. Intente nuevamente.")

            case 5:
                submenu_reports()
                print("En Construccion")

            case 6:
                start = False
                print("Gracias por utilizar Gimnasio ForceTech.")

            case _:
                print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    main()
