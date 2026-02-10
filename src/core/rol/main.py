class Roles:
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name

    def __str__(self):
        return f"{self.id}. {self.name}"

    def update_role(self, key: str, value: str | int):
        if key == "name":
            self.name = value
            print("Se ha actualizado el nombre de rol")
        else:
            print("La clave no existe")

    def delete_role():
        confirm = input("¿Desea eliminar el rol? (yes / no) ")
        if confirm == "yes":
            print("Rol eliminado con éxito")
        else:
            print("Rol no eliminado")

    def create_role(end_rol_creation: int = 0):
        name = input("Ingrese el nombre del rol: ")
        print("Rol creado con éxito")
        return Roles(end_rol_creation + 1, name)


Rol_Admin = Roles(1, "Administrador")
Rol_Gerente = Roles(2, "Gerente")
Rol_Supervisor = Roles(3, "Supervisor")
Rol_Encargado_Compras = Roles(4, "Encargado de compras")
Rol_Trabajador = Roles(5, "Trabajador")
Rol_Cliente = Roles(6, "Cliente")
