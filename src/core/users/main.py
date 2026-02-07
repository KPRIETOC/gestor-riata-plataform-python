# Importamos todos los roles
from src.core.rol.main import *


class User:
    def __init__(
        self,
        name: str = "",
        lastname: str = "",
        celphone: str = "",
        email: str = "",
        password: str = "",
        document_number: str = "",
        document_type: str = "C.C",
        age: int = 18,
        birthdate: str = "",
    ):
        self.name: str = input("Ingrese su nombre: ")
        self.lastname: str = input("Ingrese su apellido: ")
        self.document_type: str = input("Ingrese su tipo de documento: ")
        self.document_number: str = input("Ingrese su documento: ")
        self.celphone: str = input("Ingrese su celular: ")
        self.email: str = input("Ingrese su email: ")
        self.password: str = input("Ingrese su contraseña: ")
        self.age: str = input("Ingrese su edad: ")
        self.birthdate: str = input("Ingrese su fecha de nacimiento: ")
        self.active: str = False
        self.is_registred: str = False
        self.rol: Roles | None = None

    def register_user(self):
        confirm = input(
            "El usuario no ha sido registrado. ¿Desea registrarlo?. (yes / no) "
        )
        if confirm == "yes":
            self.is_registred = True
            self.active = True
            print("Usuario registrado con éxito!")
        else:
            print("Usuario no registrado")

    def assign_rol_user(self, rol: Roles):
        if not rol:
            print("El rol es requerido")
        elif self.rol:
            print("Ya tienes un rol asignado")
        elif self.is_registred:
            self.rol = rol
            print(f"Se ha asignado el rol {rol.name} de forma exitosa!")
        else:
            self.register_user()

    def update_user(self, key: str, value: str | int):
        if key == "name":
            self.name = value
            print("Se ha actualizado el nombre de usuario")
        elif key == "lastname":
            self.lastname = value
            print("Se ha actualizado el apellido de usuario")
        elif key == "document_number":
            self.document_number = value
            print("Se ha actualizado el documento de usuario")
        elif key == "document_type":
            self.document_type = value
            print("Se ha actualizado el tipo de documento de usuario")
        elif key == "celphone":
            self.celphone = value
            print("Se ha actualizado el celular de usuario")
        elif key == "birthdate":
            self.birthdate = value
            print("Se ha actualizado la fecha de nacimiento de usuario")
        else:
            print("La clave no existe")

    def delete_user(self):
        confirm = input("¿Desea eliminar el usuario? (yes / no) ")
        if confirm == "yes":
            print("Usuario eliminado con éxito")
        else:
            print("Usuario no eliminado")

    def show_user(self):
        print(
            f"""
        Nombre: {self.name}
        Apellido: {self.lastname}
        Documento: {self.document_number}
        Tipo de documento: {self.document_type}
        Celular: {self.celphone}
        Email: {self.email}
        Contraseña: {self.password}
        Edad: {self.age}
        Fecha de nacimiento: {self.birthdate}
        Rol: {self.rol.name}
        Activo: {self.active}
        Registrado: {self.is_registred if "Si" else "No"}
        """
        )

    def __str__(self):
        return self.show_user()

    def create_user(self):
        self.name = input("Ingrese su nombre: ")
        self.lastname = input("Ingrese su apellido: ")
        self.document_number = input("Ingrese su documento: ")
        self.document_type = input("Ingrese su tipo de documento: ")
        self.celphone = input("Ingrese su celular: ")
        self.email = input("Ingrese su email: ")
        self.password = input("Ingrese su contraseña: ")
        self.age = input("Ingrese su edad: ")
        self.birthdate = input("Ingrese su fecha de nacimiento: ")
        self.register_user()
        self.assign_rol_user(Roles.ADMIN)
        print("Usuario creado con éxito")
