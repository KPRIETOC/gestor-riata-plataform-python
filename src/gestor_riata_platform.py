from src.controllers.menu_list import MenuList


class GestoRiataPlatForm(MenuList):
    menu_list_default: list[MenuList] = []
    menu_list_selected: MenuList | None = None
    actions_list = [
        {"id": 1, "name": "Crear"},
        {"id": 2, "name": "Mostrar"},
        {"id": 3, "name": "Actualizar"},
        {"id": 4, "name": "Eliminar"},
    ]
    roles = []
    users = []
    running_menu = False

    def __init__(self, name_business: str):
        self.name_business = name_business

    def show_name_business(self):
        print(f"Nombre de la empresa gestora: {self.name_business}")

    def add_menu_list(self, menu: MenuList):
        self.menu_list_default.append(menu)

    def add_menu_list_key(self, key: str):
        newMenu = MenuList(len(self.menu_list_default) + 1, key)
        self.add_menu_list(newMenu)

    def create_menu(self):
        new_menu_list = [
            {"name": "Roles", "sub_list": []},
            {"name": "Usuarios", "sub_list": []},
            {"name": "Tiendas provedoras", "sub_list": [{"name": "Materiales"}]},
            {"name": "Inventario", "sub_list": [{"name": "Categorías"}]},
            {
                "name": "Facturas",
                "sub_list": [
                    {"name": "Facturas de materiales"},
                    {"name": "Facturas de inventario"},
                ],
            },
            {"name": "Cerrar programa", "sub_list": []},
        ]
        # Recorremos el menu list que creamos
        for item in new_menu_list:
            new_menu = MenuList(len(self.menu_list_default) + 1, item["name"])
            self.add_menu_list(new_menu)
            # Recorremos el sub menu list que creamos
            if len(item["sub_list"]):
                for sub_item in item["sub_list"]:
                    new_menu.add_sub_list_menu(sub_item["name"])

    def found_menu_list(self, opcion: str):
        menu = None
        for menu_item in self.menu_list_default:
            if opcion == str(menu_item.id):
                menu = menu_item
                break
        return menu

    def show_menu_list_program(self):
        for menu_item in self.menu_list_default:
            menu_item.show_menu_list()
            # Buscamos si tiene una lista interna o hija
            size_sub_menu = len(menu_item.sub_list_menu)
            if size_sub_menu >= 1:
                for menu_sub_item in menu_item.sub_list_menu:
                    # Evaluar si es la ultima de la lista para que haga el salto de linea
                    if not (menu_sub_item.id == size_sub_menu):
                        print("   ", menu_sub_item.__str__())
                    else:
                        print("   ", menu_sub_item.__str__(), "\n")

    def valid_option_menu(self, retry: int = 10):
        opcion = input("\n Seleccione un módulo escribiendo su número: ")
        # Guardamos en la variable de arriaba para acceder en otras funciones
        self.menu_list_selected = self.found_menu_list(opcion)

        if retry <= 0:
            return None

        if self.menu_list_selected == None:
            retry = retry - 1
            print(f"Intentos restantes {retry}")
            print("\nEl módulo no existe, escribe un nuevo núevo número otra:")
            show_menu_again = (
                input("\nMostrar nuevamente el menu, si o no: ").lower() == "si"
            )
            if show_menu_again:
                self.show_menu_list_program()
            self.valid_option_menu(retry)
        else:
            print(f"\nHas seleccionado el módulo de {self.menu_list_selected.name}")

    # Ejecutar antes de create_menu
    def on_menu_list(self):
        self.running_menu = True

        if len(self.menu_list_default) == 0:
            print("\nNo hay menu de momento")
            return
        while self.running_menu:
            print("\n***** Menu de la empresa *****\n")

            # Llamamos al menú
            self.show_menu_list_program()

            # TODO: add retry again program

            self.valid_option_menu()

            action_selected = input(
                f"\nSeleccione ahora la accion que quiere realizar en el módulo de {self.menu_list_selected.name}: "
            )
            if action_selected == "1":
                print(f"Crear {1}")
            elif action_selected == "2":
                print(f"")
            else:
                print("Cerrar programa")

            break
