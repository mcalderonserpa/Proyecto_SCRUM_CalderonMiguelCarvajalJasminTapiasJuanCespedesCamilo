from menus import (
    menu_principal,
    menu_clientes,
    submenu_servicios,
    menu_instructores,
    menu_administrador,
    submenu_matriculas,
    submenu_gestion_servicios,
    submenu_reportes
)


def main():
    while True:
        menu_principal()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_clientes()

        elif opcion == "2":
            submenu_servicios()

        elif opcion == "3":
            menu_instructores()

        elif opcion == "4":
            menu_administrador()

        elif opcion == "5":
            submenu_reportes()

        elif opcion == "6":
            print("Gracias por utilizar Gimnasio ForceTech.")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()
