class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def mostrar_rol(self):
        print(f"Usuario: {self.nombre} - Rol: {self.rol}")


class Administrador(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "Administrador")

    def gestionar_sistema(self):
        print(f"{self.nombre} tiene acceso completo al sistema.")


class Gerente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "Gerente")

    def supervisar_trabajadores(self):
        print(f"{self.nombre} está supervisando a los trabajadores.")


class EncargadoDeCompras(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "Encargado de Compras")

    def realizar_compra(self):
        print(f"{self.nombre} está realizando compras.")


class Trabajador(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "Trabajador")

    def realizar_tarea(self):
        print(f"{self.nombre} está realizando su tarea asignada.")


class Cliente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "Cliente")

    def realizar_pedido(self):
        print(f"{self.nombre} está realizando un pedido.")