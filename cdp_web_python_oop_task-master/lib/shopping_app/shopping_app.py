from customer import Customer
from item import Item
from seller import Seller

# Crear una instancia de Seller (vendedor) con el nombre "DICストア"
vendedor = Seller("DICストア")

# Agregar varios artículos al vendedor
for i in range(10):
    Item("CPU", 40830, vendedor)            # Añadir CPU
    Item("Memoria RAM", 13880, vendedor)    # Añadir Memoria RAM
    Item("Placa Base", 28980, vendedor)     # Añadir Placa Base
    Item("Unidad de Fuente de Alimentación", 8980, vendedor)  # Añadir Unidad de Fuente de Alimentación
    Item("Caja de PC", 8727, vendedor)      # Añadir Caja de PC
    Item("HDD de 3.5 pulgadas", 10980, vendedor)  # Añadir HDD de 3.5 pulgadas
    Item("SSD de 2.5 pulgadas", 13370, vendedor)  # Añadir SSD de 2.5 pulgadas
    Item("SSD M.2", 12980, vendedor)        # Añadir SSD M.2
    Item("Refrigeración de CPU", 13400, vendedor)  # Añadir Refrigeración de CPU
    Item("Tarjeta Gráfica", 23800, vendedor)  # Añadir Tarjeta Gráfica

print("🤖 Por favor, dime tu nombre")  # Mensaje para solicitar el nombre del cliente
nombre_cliente = input()  # Entrada del nombre del cliente

print("🏧 Por favor, introduce la cantidad a cargar en tu billetera")  # Mensaje para solicitar el depósito en la billetera
cantidad_deposito = int(input())  # Entrada del monto a depositar en la billetera del cliente

print("🛍️ Comenzando la compra")  # Mensaje de inicio de la compra
fin_compra = False  # Variable para controlar la finalización de la compra

while not fin_compra:
    print("📜 Lista de productos")  # Mensaje para mostrar la lista de productos disponibles
    vendedor.show_items()  # Mostrar los artículos disponibles en el vendedor

    print("️️⛏ Por favor, introduce el número del producto")  # Mensaje para solicitar el número de producto
    numero_producto = int(input())  # Entrada del número de producto

    print("⛏ Por favor, introduce la cantidad del producto")  # Mensaje para solicitar la cantidad de producto
    cantidad_producto = int(input())  # Entrada de la cantidad de producto

    # Obtener los artículos del vendedor según el número y cantidad especificados
    items = vendedor.pick_items(numero_producto, cantidad_producto)

    # Agregar los artículos seleccionados al carrito del cliente
    for item in items:
        cliente.cart.add(item)

    print("🛒 Contenido del carrito")  # Mensaje para mostrar el contenido del carrito
    cliente.cart.show_items()  # Mostrar los artículos en el carrito del cliente
    print(f"🤑 Total a pagar: {cliente.cart.total_amount()}")  # Mostrar el total a pagar del carrito

    print("😭 ¿Deseas finalizar la compra? (si/no)")  # Mensaje para preguntar si desea finalizar la compra
    fin_compra = input() == "si"  # Verificar si el cliente desea finalizar la compra

print("💸 ¿Deseas confirmar la compra? (si/no)")  # Mensaje para confirmar la compra
if input() == "si":
    cliente.cart.check_out()  # Procesar el pago de los artículos en el carrito del cliente

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")

print(f"️🛍️ ️Propiedades de {cliente.name}")  # Mostrar las propiedades del cliente
cliente.show_items()  # Mostrar los artículos en propiedad del cliente
print(f"😱👛 Saldo en la billetera de {cliente.name}: {cliente.wallet.balance}")  # Mostrar el saldo de la billetera del cliente

print(f"📦 Estado del inventario de {vendedor.name}")  # Mostrar el estado del inventario del vendedor
vendedor.show_items()  # Mostrar los artículos disponibles en el vendedor
print(f"😻👛 Saldo en la billetera de {vendedor.name}: {vendedor.wallet.balance}")  # Mostrar el saldo de la billetera del vendedor

print("🛒 Contenido del carrito")  # Mostrar el contenido del carrito del cliente
cliente.cart.show_items()  # Mostrar los artículos en el carrito del cliente
print(f"🌚 Total a pagar: {cliente.cart.total_amount()}")  # Mostrar el total a pagar del carrito del cliente

print("🎉 Fin del programa")  # Mensaje de fin del programa
