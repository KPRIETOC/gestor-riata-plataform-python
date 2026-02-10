# Importamos todos los roles
from src.core.rol.main import *


class User:
    def __init__(
        self,
        name: str,
        lastname: str,
        document_number: str,
        celphone: str,
        email: str,
        password: str,
        age: int,
        document_type: str = "C.C",
        birthdate: str = "",
    ):
        # Asignamos los valores recibidos como argumentos
        self.name = name
        self.lastname = lastname
        self.document_type = document_type
        self.document_number = document_number
        self.celphone = celphone
        self.email = email
        self.password = password
        self.age = age
        self.birthdate = birthdate
        self.active = False
        self.is_registered = False  # Corregido el typo 'registred'
        self.rol = None

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

    def create_user():
        name = input("Ingrese su nombre: ")
        lastname = input("Ingrese su apellido: ")
        document_number = input("Ingrese su documento: ")
        document_type = input("Ingrese su tipo de documento: ")
        celphone = input("Ingrese su celular: ")
        email = input("Ingrese su email: ")
        password = input("Ingrese su contraseña: ")
        age = input("Ingrese su edad: ")
        birthdate = input("Ingrese su fecha de nacimiento: ")
        
        
        
        print("Usuario creado con éxito")
