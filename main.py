from typing import List
from src.start.welcome import welcomeText
from src.start.menu_list import MenuList


class GestorRiataPlataform:
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
        menu = MenuList()
        self.menu_list = menu.menu_list

    def running_menu(self):
        if len(self.menu_list):
            self.is_running = True

            while self.is_running:
                if self.menu__list_item == None:
                    for index in range(len(self.menu_list)):
                        item_menu = self.menu_list[index]
                        print(f"{item_menu["id"]}. {item_menu["name"]}")

                item_menu_selected = int(
                    input("Escriba el número al acción que quiera ingresar: ")
                )

                def item_found():
                    self.menu__list_item = self.menu_list[item_menu_selected - 1]
                    print(f"Has seleccionado {self.menu__list_item["name"]}")
                    return self.menu__list_item

                if item_menu_selected == 1:
                    item_found()
                elif item_menu_selected == 2:
                    item_found()
                elif item_menu_selected == 3:
                    item_found()
                elif item_menu_selected == 4:
                    item_found()
                elif item_menu_selected == 5:
                    item_found()
                elif item_menu_selected == 6:
                    is_sure_program = input(
                        "Está seguro que quiere cerrar el programa: (yes / no) "
                    )
                    if is_sure_program == "yes":
                        self.is_running = False
                else:
                    self.is_running = False

        else:
            print("No se pudo no mostrar el menú")


fisrtCompany = GestorRiataPlataform()

fisrtCompany.on_program()
