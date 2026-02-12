class MenuList:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.sub_list_menu: list[MenuList] = []

    def show_menu_list(self):
        print(self.__str__())

    def __str__(self):
        return f"  {self.id}:  {self.name}"

    def add_sub_list_menu(self, name_item_menu: str):
        newList = MenuList(len(self.sub_list_menu) + 1, name_item_menu)
        self.sub_list_menu.append(newList)


# menu_roles = MenuList(1, "Roles")

# menu_roles.show_menu()
