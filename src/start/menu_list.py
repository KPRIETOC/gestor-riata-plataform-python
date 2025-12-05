class MenuList:
    def __init__(self, id: int, name: str, sub_menu_list: list = []):
        self.id: int = id
        self.name: str = name
        self.sub_menu_list: list[MenuList] = sub_menu_list

    def add_sub_menu(self, sub_menu_list):
        self.sub_menu_list.append(sub_menu_list)

    def remove_sub_menu(self, sub_menu_list):
        self.sub_menu_list.remove(sub_menu_list)


menu_list: list[MenuList] = []

menu_rol = MenuList(1, "Roles")
menu_users = MenuList(2, "Usuarios")
menu_supplier_stores = MenuList(3, "Tiendas Provedoras")
menu_supplier_stores_materials = MenuList(1, "Materiales")
menu_stock = MenuList(4, "Stock Inventario")
menu_invoices = MenuList(5, "Facturas")
menu_invoices_materials = MenuList(1, "Facturas de materiales")
menu_invoices_stock = MenuList(2, "Facturas de stock vendido")

menu_closed = MenuList(6, "Cerrar Programa")

# Main Menu Stores
menu_supplier_stores.add_sub_menu(menu_supplier_stores_materials)
# Main Menu Invoces
menu_invoices.add_sub_menu(menu_invoices_materials)
menu_invoices.add_sub_menu(menu_invoices_stock)

# Main Menu
menu_list.append(menu_rol)
menu_list.append(menu_users)
menu_list.append(menu_supplier_stores)
menu_list.append(menu_stock)
menu_list.append(menu_invoices)
menu_list.append(menu_closed)
