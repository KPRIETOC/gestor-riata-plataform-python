def welcome_grp() -> str:
    print("Bienvenido a Gestor Riata Plataform")

    print("El sistema que gestiona tu empresa de forma controlada y eficiente.")

    name_business: str = input("Introduce tu nombre de empresa: ")

    print(f"Empresa registrada con el nombre de {name_business}")

    return name_business
