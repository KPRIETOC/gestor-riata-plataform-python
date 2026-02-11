from src.controllers.menu_list import MenuList


class GestoRiataPlatForm(MenuList):
    menu_list_default = []
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
        print(key)
        return len(self[key]) + 1

    def create_menu(self):
        # ROLES
        menu_roles = MenuList(1, "Roles")
        self.add_menu_list(menu_roles)
        # USERS
        menu_users = MenuList(self.next_id("menu_list_default"), "Users")
        self.add_menu_list(menu_users)

    # Ejecutar antes de create_menu
    def on_menu_list(self):
        self.running_menu = True

        if len(self.menu_list_default) == 0:
            print("No hay menu de momento")

        while self.running_menu:
            break
