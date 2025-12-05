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
        self.name: str = name
        self.lastname: str = lastname
        self.document_type: str = document_type
        self.document_number: str = document_number
        self.celphone: str = celphone
        self.email: str = email
        self.password: str = password
        self.age: str = age
        self.birthdate: str = birthdate
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
        # else:

    def update_user(self):
        print("Usuario Actualizado con éxito")
