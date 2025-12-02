from src.start.welcome import welcomeText

class GestorRiataPlataform:
    def __init__(self):
        self.company_name = ""
        self.id = 1
        self.menu_list = []

    def on_program(self):
        print(welcomeText)

        self.company_name = input("Ingresa el nombre: ")

        print(f"Empresa: {self.company_name}")

    def create_menu(self):
        self.menu_list = [
           
            "",
            "",
            "",
            " --> Productos de tiendas",
        ]


fisrtCompany = GestorRiataPlataform()

fisrtCompany.on_program()
