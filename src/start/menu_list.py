class MenuList:
    def __init__(self, id: int, name: str, sub_menu_list: list = []):
        self.id: int = id
        self.name: str = name
        self.sub_menu_list: list[MenuList] = sub_menu_list


menu_list: list[MenuList] = []
menu_list_current_id = len(menu_list) + 1

menu_rol = MenuList(menu_list_current_id, "Roles")
menu_users = MenuList(menu_list_current_id, "Usuarios")
menu_supplier_stores = MenuList(menu_list_current_id, "Tiendas Provedoras")
menu_stock = MenuList(menu_list_current_id, "Stock Inventario")
menu_invoices = MenuList(menu_list_current_id, "Facturas")

menu_list.append(menu_rol, menu_users, menu_supplier_stores, menu_stock, menu_invoices)

print(menu_list)