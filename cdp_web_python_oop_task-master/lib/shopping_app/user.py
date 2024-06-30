from wallet import Wallet

class User:
    from item_manager import show_items, items_list, pick_items, show_items  # Importar funciones relacionadas con la gestión de ítems

    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)   # Cuando se crea una instancia de User o una instancia de una clase que hereda de User, se crea un Wallet con el propio usuario como propietario.
