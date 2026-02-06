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
            print("Crear")
        elif action_id == 2:
            print("Mostrar Listado")
        elif action_id == 3:
            print("Editar")
        elif action_id == 4:
            print("Eliminar")
        else:
            menu_list_item = None

    def add_rol(self, rol: Roles):
        self.roles.append(rol)

    def add_users(self, user: User):
        if user.rol:
            self.users.append(user)
        else:
            user.register_user()
