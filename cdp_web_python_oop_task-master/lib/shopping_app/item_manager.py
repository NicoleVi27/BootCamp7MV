from item import Item  # Importar la clase Item desde item.py
from tabulate import tabulate  # Importar la función tabulate del módulo tabulate
from itertools import groupby  # Importar la función groupby del módulo itertools

def items_list(self):
    """
    Retorna todos los objetos Item que el propio objeto (self) posee como propietario.
     
    Returns:
    - List: Lista de objetos Item que son propiedad del objeto actual (self).
    """
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):
    """
    Retorna una cantidad específica de objetos Item que el objeto actual (self) posee,
    correspondientes al número especificado.

    Args:
    - number: Número específico asociado a los objetos Item que se desean obtener.
    - quantity: Cantidad de objetos Item que se desea obtener.

    Returns:
    - List: Lista de objetos Item que coinciden con el número especificado y la cantidad deseada.
    """
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):
    """
    Muestra la situación de stock de los objetos Item que el objeto actual (self) posee como propietario,
    en formato de tabla con las columnas ["番号", "商品名", "金額", "数量"].

    Imprime la tabla en formato grid utilizando el módulo tabulate.
    """
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["番号", "商品名", "金額", "数量"], tablefmt="grid"))

def _stock(self):
    """
    Retorna la situación de stock de los objetos Item que el objeto actual (self) posee como propietario.
    Agrupa los items por nombre y cuenta la cantidad disponible de cada uno.

    Returns:
    - List: Lista de diccionarios representando la situación de stock, con las claves "number", "label" y "items".
    """
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})
    return stock
