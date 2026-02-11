from src.controllers.menu_list import MenuList


class GestoRiataPlatForm(MenuList):
    menu_list_default: list[MenuList] = []
    menu_list_selected: MenuList | None = None
    roles = []
    users = []
    running_menu = False

    def __init__(self, name_business: str):
        self.name_business = name_business

    def show_name_business(self):
        print(f"Nombre de la empresa gestora: {self.name_business}")

    def add_menu_list(self, menu: MenuList):
        self.menu_list_default.append(menu)

    def next_id(self, key: str):
        if key == "menu_list_default":
            return len(self.menu_list_default) + 1
        elif key == "roles":
            return len(self.roles) + 1
        else:
            return len(self.users) + 1

    def add_menu_list_key(self, key: str):
        newMenu = MenuList(len(self.menu_list_default) + 1, key)
        self.add_menu_list(newMenu)

    def create_menu(self):
        # TODO: REPLACE FOR "add_menu_list_key" AND add array keys

        key = "menu_list_default"
        # ROLES
        menu_roles = MenuList(self.next_id(key), "Roles")
        self.add_menu_list(menu_roles)

        # USERS
        menu_users = MenuList(self.next_id(key), "Usuarios")
        self.add_menu_list(menu_users)

        # SUPPLIER STORES | MATERIALS
        menu_stores = MenuList(self.next_id(key), "Tiendas provedoras")
        self.add_menu_list(menu_stores)
        menu_stores.add_sub_list_menu("Materiales")

        # STOCK INVENTORY
        menu_stock_inventory = MenuList(self.next_id(key), "Inventario")
        self.add_menu_list(menu_stock_inventory)
        menu_stock_inventory.add_sub_list_menu("Categorías")

        # INVOICES | INVOICES MATERIALS | INVOICES INVENTORY
        menu_stock_invoices = MenuList(self.next_id(key), "Facturas")
        self.add_menu_list(menu_stock_invoices)
        menu_stock_invoices.add_sub_list_menu("Facturas de materiales")
        menu_stock_invoices.add_sub_list_menu("Facturas de inventario")
        # CLOSE PROGRAM
        menu_close_program = MenuList(self.next_id(key), "Cerrar Programa")
        self.add_menu_list(menu_close_program)

    def found_menu_list(self, opcion: int):
        for menu_item in self.menu_list_default:
            if opcion == menu_item.id:
                return menu_item
            else:
                return None

    # Ejecutar antes de create_menu
    def on_menu_list(self):
        self.running_menu = True

        if len(self.menu_list_default) == 0:
            print("\nNo hay menu de momento")
            return

        while self.running_menu:
            print("\n***** Menu de la empresa *****\n")
            def show_menu_list_program():
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

            # Llamamos al menú
            show_menu_list_program()
            # TODO: add retry again program
            def valid_option():
                opcion = input("\n Seleccione un módulo escribiendo su número: ")
                self.menu_list_selected = self.found_menu_list(int(opcion))
                if self.menu_list_selected == None:
                    print("\nEl módulo no existe, escribe un nuevo núevo número otra:")
                    show_menu_again = input("\nMostrar nuevamente el menu, si o no: ").lower() == "si"
                    if show_menu_again:
                        show_menu_list_program()
                    valid_option()
                else:
                    print(
                        f"\nHas seleccionado el módulo de {self.menu_list_selected.name}"
                    )

            valid_option()

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
