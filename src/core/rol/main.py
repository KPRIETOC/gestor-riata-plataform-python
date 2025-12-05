class Roles:
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name

    def __str__(self):
        return f"{self.id}. {self.name}"


Rol_Admin = Roles(1, "Administrador")
Rol_Gerente = Roles(2, "Gerente")
Rol_Supervisor = Roles(3, "Supervisor")
Rol_Encargado_Compras = Roles(4, "Encargado de compras")
Rol_Trabajador = Roles(5, "Trabajador")
Rol_Cliente = Roles(6, "Cliente")
