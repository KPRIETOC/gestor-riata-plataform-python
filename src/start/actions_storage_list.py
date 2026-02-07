from src.core.rol.main import *
from src.core.users.main import *
from src.start.menu_list import *

actions_list = [
    {"id": 1, "name": "Crear"},
    {"id": 2, "name": "Mostrar en listado"},
    {"id": 3, "name": "Editar"},
    {"id": 4, "name": "Eliminar"},
]


class ActionsStorageList:
    def __init__(self):
        self.roles: list[Roles] = []
        self.users: list[User] = []

    def actions_menu(self, menu_list_item: MenuList | None):
        print(f"Has seleccionado {menu_list_item.name} \n")

        for action in actions_list:
            print(f"{action["id"]}. {action["name"]}")

        action_id = int(input("Selecciona una acción: "))

        if action_id == 1:
            self.handle_actions(menu_list_item.id, 1)
        elif action_id == 2:
            self.handle_actions(menu_list_item.id, 2)
        elif action_id == 3:
            print("Editar")
        elif action_id == 4:
            print("Eliminar")
        else:
            menu_list_item = None

    def handle_actions(self, menu_list_item_id: int, action_id: int):
        if menu_list_item_id == 1:
            rol = Roles.create_role()
            self.add_rol(rol)
            print("Rol creado con éxito")
            menu_list_item = MenuList(1, "Roles")
            menu_list_item.add_sub_menu(MenuList(1, "Crear Rol"))
            menu_list_item.add_sub_menu(MenuList(2, "Mostrar Listado"))
            menu_list_item.add_sub_menu(MenuList(3, "Editar Rol"))
            menu_list_item.add_sub_menu(MenuList(4, "Eliminar Rol"))
        elif menu_list_item_id == 2:
            user = User()
            self.add_users(user)
            print("Usuario creado con éxito")
            menu_list_item = MenuList(2, "Usuarios")
            menu_list_item.add_sub_menu(MenuList(1, "Crear Usuario"))
            menu_list_item.add_sub_menu(MenuList(2, "Mostrar Listado"))
            menu_list_item.add_sub_menu(MenuList(3, "Editar Usuario"))
            menu_list_item.add_sub_menu(MenuList(4, "Eliminar Usuario"))
        else:
            menu_list_item = None

    def add_rol(self, rol: Roles):
        self.roles.append(rol)

    def add_users(self, user: User):
        if user.rol:
            self.users.append(user)
        else:
            user.register_user()
