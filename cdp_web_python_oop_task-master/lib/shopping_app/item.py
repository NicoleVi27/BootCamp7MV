from ownable import Ownable  # Importar la clase Ownable desde ownable.py

class Item:
    instances = []  # Variable de clase para almacenar todas las instancias de Item creadas

    def __init__(self, nombre, precio, propietario=None):
        """
        Constructor de la clase Item.

        Args:
        - nombre: Nombre del artículo.
        - precio: Precio del artículo.
        - propietario: Propietario inicial del artículo (opcional).
        """
        self.nombre = nombre
        self.precio = precio
        self.establecer_propietario(propietario)
        # Cuando se crea una instancia de Item, esa instancia (self) se almacena en la lista instances de la clase.
        Item.instances.append(self)

    def etiqueta(self):
        """
        Retorna un diccionario con el nombre y el precio del artículo.

        Returns:
        - dict: Diccionario con las claves "name" y "price".
        """
        return {"name": self.nombre, "price": self.precio}

    @staticmethod
    def item_all():
        """
        Método estático que retorna todas las instancias de Item creadas hasta el momento.

        Returns:
        - List: Lista de todas las instancias de Item.
        """
        return Item.instances
    
    def establecer_propietario(self, propietario):
        """
        Establece el propietario del artículo.

        Args:
        - propietario: Objeto Ownable que representa al propietario del artículo.
        """
        self.propietario = propietario

