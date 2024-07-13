class TorreHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.source = list(range(num_discos, 0, -1))
        self.auxiliary = []
        self.destination = []

    def resolver(self):
        self.mover_discos(self.num_discos, self.source, self.destination, self.auxiliary)

    def mover_discos(self, n, origen, destino, auxiliar):
        if n > 0:
            # Mover n-1 discos de origen a auxiliar, usando destino como auxiliar
            self.mover_discos(n - 1, origen, auxiliar, destino)
            # Mover el disco n de origen a destino
            destino.append(origen.pop())
            self.imprimir_estado()
            # Mover n-1 discos de auxiliar a destino, usando origen como auxiliar
            self.mover_discos(n - 1, auxiliar, destino, origen)

    def imprimir_estado(self):
        print("Estado actual:")
        print("Source: " + str(self.source))
        print("Auxiliary: " + str(self.auxiliary))
        print("Destination: " + str(self.destination))
        print()

if __name__ == "__main__":
    num_discos = int(input("Ingrese el número de discos: "))
    torre_hanoi = TorreHanoi(num_discos)
    torre_hanoi.resolver()

