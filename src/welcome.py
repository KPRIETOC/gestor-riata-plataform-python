def welcome_grp() -> str:
    print("\n¡Bienvenido a Gestor Riata Plataform!")

    print("\n El sistema que gestiona tu empresa de forma controlada y eficiente. \n")

    name_business: str = input("Introduce tu nombre de empresa: ")

    print(f"\nEmpresa registrada con el nombre de {name_business}")

    return name_business
