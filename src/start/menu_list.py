class MenuList:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.sub_menu_list = []
        self.menu_list = [
            {"id": 1, "name": "Roles", "sub_menu_list": []},
            {"id": 2, "name": "Usuarios", "sub_menu_list": []},
            {
                "id": 3,
                "name": "Tiendas Provedoras",
                "sub_menu_list": [
                    {"id": 1, "name": "Materiales", "sub_menu_list": []},
                ],
            },
            {"id": 4, "name": "Stock Inventario", "sub_menu_list": []},
            {
                "id": 5,
                "name": "Facturación",
                "sub_menu_list": [
                    {"id": 1, "name": "Facturas de Materiales", "sub_menu_list": []},
                    {"id": 2, "name": "Facturas de Stock Vendido", "sub_menu_list": []},
                ],
            },
            {"id": 6, "name": "Cerrar Programa", "sub_menu_list": []},
        ]
