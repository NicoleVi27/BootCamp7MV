from user import User  # Importar la clase User desde user.py
from cart import Cart  # Importar la clase Cart desde cart.py

class Cliente(User):
    """
    Clase Cliente que hereda de la clase User.

    Atributos heredados:
    - name: Nombre del cliente (heredado de User).
    - cart: Instancia de Cart asociada al cliente.

    Métodos definidos:
    - __init__(self, name): Constructor para inicializar un objeto Cliente con un nombre dado.
    """
    def __init__(self, nombre):
        """
        Constructor de la clase Cliente.

        Args:
        - nombre: Nombre del cliente.
        """
        super().__init__(nombre)  # Llamada al constructor de la clase base (User)
        self.carrito = Cart(self)  # Crear una instancia de Cart con el cliente como propietario (self)
