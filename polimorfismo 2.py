class FiguraGeometrica:
    def calcular_area(self):
        pass

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2
def imprimir_area_y_tipo(figura):
    print(f"Área de la figura: {figura.calcular_area()}")

    if isinstance(figura, Cuadrado):
        print("Tipo de figura: Cuadrado")
    elif isinstance(figura, Triangulo):
        print("Tipo de figura: Triángulo")
cuadrado = Cuadrado(4)
triangulo = Triangulo(5, 8)
imprimir_area_y_tipo(cuadrado)
imprimir_area_y_tipo(triangulo)