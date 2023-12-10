class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
<<<<<<< HEAD

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


=======
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

>>>>>>> d6b2b11 (herencia)
class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

<<<<<<< HEAD

=======
>>>>>>> d6b2b11 (herencia)
c = Coche("azul", 4, 150, 1200)
print(c)