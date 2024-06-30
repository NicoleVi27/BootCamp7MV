class Wallet:
    def __init__(self, owner):
        self.set_owner(owner)  # Establece el propietario del wallet
        self.balance = 0  # Inicializa el saldo en cero al crear una instancia de Wallet para el propietario dado.

    def deposit(self, amount):
        self.balance += int(amount)  # Aumenta el saldo del wallet con la cantidad especificada.

    def withdraw(self, amount):
        if not self.balance >= amount:  # Verifica si hay suficiente saldo para retirar la cantidad especificada.
            return  # Si no hay suficiente saldo, no realiza ninguna operación de retiro.
        self.balance -= int(amount)  # Reduce el saldo del wallet en la cantidad especificada.
        return amount  # Devuelve la cantidad retirada.

    def set_owner(self, owner):
        self.owner = owner  # Establece el propietario del wallet con el objeto proporcionado.
