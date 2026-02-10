from typing import List
from src.start.welcome import welcomeText
from src.start.menu_list import menu_list, MenuList
from src.start.actions_storage_list import ActionsStorageList


class GestorRiataPlataform(ActionsStorageList):
    def __init__(self):
        self.company_name = ""
        self.id = 1
        self.menu_list: List[MenuList] = []
        self.menu__list_item: None | MenuList = None
        self.is_running = False

    def on_program(self):
        print(welcomeText)
        self.company_name = input("Ingresa el nombre: ")
        print(f"Empresa: {self.company_name}")

        self.create_menu()
        self.running_menu()

    def create_menu(self):
        self.menu_list = menu_list

    def running_menu(self):
        if len(self.menu_list):
            self.is_running = True

            while self.is_running:

                print("\n")
                print("---- Menu principal ----")
                for index in range(len(self.menu_list)):
                    item_menu = self.menu_list[index]
                    print(f"{item_menu.id}. {item_menu.name}")

                item_menu_selected = int(
                    input("Escriba el número al módulo o acción que quiera ingresar: ")
                )

                self.menu__list_item = self.menu_list[item_menu_selected - 1]

                print(f"Seleccionado: {self.menu__list_item.name}")

                self.actions_menu(self.menu__list_item, item_menu_selected)
        else:
            print("No se pudo no mostrar el menú")

    def close_program(self):
        self.is_running = False
        print("Cerrar del programa")


fisrtCompany = GestorRiataPlataform()

fisrtCompany.on_program()
