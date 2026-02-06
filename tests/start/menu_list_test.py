import unittest
from src.start.menu_list import MenuList

# para ejecutar los tests
# python -m unittest tests/start/menu_list_test.py

class MenuListTest(unittest.TestCase):
    def test_menu_list(self):
        menu_list = MenuList(1, "Crear Usuario")
        self.assertEqual(menu_list.id, 1)
        self.assertEqual(menu_list.name, "Crear Usuario")
    #   self.assertEqual(menu_list.description, "Crear Usuario")


if __name__ == "__main__":
    unittest.main()

