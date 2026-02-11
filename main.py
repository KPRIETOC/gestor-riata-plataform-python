from src.gestor_riata_platform import GestoRiataPlatForm
from src.welcome import welcome_grp

# Binvenida para la creación del sistema
name_buiness = welcome_grp()

# Inicializador del sistema
business = GestoRiataPlatForm(name_buiness)

business.create_menu()

business.on_menu_list()