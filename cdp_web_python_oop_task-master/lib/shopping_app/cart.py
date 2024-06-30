from ownable import Ownable  # Importar la clase Ownable desde ownable.py

class Cart:
    from item_manager import show_items  # Importar la función show_items desde item_manager.py
    
    def __init__(self, owner):
        """
        Inicializa un carrito con un propietario y una lista vacía de items.
        
        Args:
        - owner: Objeto Ownable que representa al propietario del carrito.
        """
        self.set_owner(owner)
        self.items = []
        
    def set_owner(self, owner):
        """
        Establece el propietario del carrito.
        
        Args:
        - owner: Objeto Ownable que representa al propietario del carrito.
        """
        self.owner = owner

    def items_list(self):
        """
        Retorna la lista de items en el carrito.
        
        Returns:
        - Lista de items actualmente en el carrito.
        """
        return self.items

    def add(self, item):
        """
        Agrega un item al carrito.
        
        Args:
        - item: Objeto que representa el item a agregar al carrito.
        """
        self.items.append(item)

    def total_amount(self):
        """
        Calcula el monto total de todos los items en el carrito.
        
        Returns:
        - Total del monto de todos los items en el carrito.
        """
        price_list = [item.price for item in self.items]
        return sum(price_list)

    def check_out(self):
        """
        Procesa el pago y la transferencia de items al propietario del carrito.
        Deposita el dinero correspondiente en la billetera del propietario y 
        retira el dinero de la billetera del propietario por cada item comprado.
        Luego, asigna al propietario como dueño de cada item y vacía la lista de items.
        """
        for item in self.items:
            item.owner.wallet.deposit(item.price)  # Depositar el precio del item en la billetera del propietario del item
            self.owner.wallet.withdraw(item.price)  # Retirar el precio del item de la billetera del propietario del carrito
            item.set_owner(self.owner)  # Establecer al propietario del item como el propietario del carrito
        
        self.items = []  # Vaciar la lista de items del carrito

