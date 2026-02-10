from src.core.rol.main import *
from src.core.users.main import *
from src.start.menu_list import *

actions_list = [
    {
        "id": 1,
        "name": "Crear",
    },
    {
        "id": 2,
        "name": "Mostrar en listado",
    },
    {
        "id": 3,
        "name": "Editar",
    },
    {
        "id": 4,
        "name": "Eliminar",
    },
]


class ActionsStorageList:
    def __init__(self):
        self.roles: list[Roles] = []
        self.users: list[User] = []

    def actions_menu(self, menu_list_item: MenuList | None, action_id: int = 0):
        print("\n")
        print(f"Has seleccionado {menu_list_item.name} \n")

        for action in actions_list:
            print(f"{action["id"]}. {action["name"]}")

        action_id = int(input("Selecciona una acción: "))

        if action_id == 1:
            print(f"Crear nuevo {menu_list_item.name}")
            self.handle_actions(menu_list_item.id)
            return True
        elif action_id == 2:
            print("Mostrar en listado")
            # self.handle_actions(menu_list_item.id, 2)
            return True
        elif action_id == 3:
            print("Editar")
            return True
        elif action_id == 4:
            print("Eliminar")
            # Volver al menú una vez que termine la acción
            return True
        else:
            # Terminar programa
            menu_list_item = None

    def handle_actions(self, menu_list_item_id: int):
        if menu_list_item_id == 1:
            # Crear nuevo rol
            newRol = Roles.create_role()
            self.add_rol(newRol)

        elif menu_list_item_id == 2:
            user = User.create_user()
            print(user.__str__())
        else:
            menu_list_item = None

    def add_rol(self, rol: Roles):
        self.roles.append(rol)

    def add_users(self, user: User):
        if user.rol:
            self.users.append(user)
        else:
            user.register_user()
