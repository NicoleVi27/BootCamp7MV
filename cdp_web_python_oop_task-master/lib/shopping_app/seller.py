from user import User  # Importar la clase User desde user.py

class Seller(User):
    def __init__(self, nombre):
        """
        Constructor de la clase Seller.

        Args:
        - nombre: Nombre del vendedor.
        """
        super().__init__(nombre)
