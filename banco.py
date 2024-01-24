class Banco:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.saldo = saldo_inicial
        print(f"Bienvenido al Banco {self.nombre}.")
        print(f"Su saldo inicial es de {self.saldo}.")

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} en su cuenta.")
        print(f"Su saldo actual es de {self.saldo}.")

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} de su cuenta.")
            print(f"Su saldo actual es de {self.saldo}.")
        else:
            print("No tiene suficiente saldo en su cuenta.")

    def __del__(self):
        print(f"Gracias por usar el Banco {self.nombre}.")


banco = Banco("Futuesperanza", 200)
banco.depositar(1500)
banco.retirar(122)
del banco