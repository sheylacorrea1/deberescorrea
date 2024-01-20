class Avion:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def despegar(self):
        return "Despegando"

    def aterrizar(self):
        return "Aterrizando"

    def mostrar_info(self):
        return f"Avión - Marca: {self.marca}, Modelo: {self.modelo}"


class Bote(Avion):
    def __init__(self, marca, modelo, tipo):
        # Llamamos al constructor de la clase base usando super()
        super().__init__(marca, modelo)
        self.tipo = tipo

    def navegar(self):
        return "Navegando por el agua"

    def mostrar_info(self):
        # Sobrescribimos el método de la clase base
        return f"Bote - {super().mostrar_info()}, Tipo: {self.tipo}"


# Crear una instancia de la clase derivada
mi_bote = Bote("Yamaha", "Modelo X", "Velero")

# Acceder a atributos y llamar a métodos de la clase base
print(mi_bote.mostrar_info())

# Llamar a métodos específicos de la clase derivada
print(mi_bote.navegar())
