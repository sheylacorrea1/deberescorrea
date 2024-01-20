class Bebe:
    def __init__(self, nombre, edad_meses):
        self._nombre = nombre
        self._edad_meses = edad_meses

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self._nombre = nuevo_nombre
        else:
            print("Error: El nombre debe ser una cadena de texto.")

    def get_edad_meses(self):
        return self._edad_meses

    def set_edad_meses(self, nueva_edad_meses):
        if isinstance(nueva_edad_meses, int) and nueva_edad_meses >= 0:
            self._edad_meses = nueva_edad_meses
        else:
            print("Error: La edad en meses debe ser un número entero no negativo.")

    def jugar(self):
        print(f"{self._nombre} está jugando.")

mi_bebe = Bebe("SABRINA", 9)
print(f"Nombre del bebé: {mi_bebe.get_nombre()}")
print(f"Edad del bebé en meses: {mi_bebe.get_edad_meses()}")
print(f"Nombre directo: {mi_bebe._nombre}")
mi_bebe.set_nombre("VIOLETA")
mi_bebe.set_edad_meses(11)
print(f"Nombre actualizado: {mi_bebe.get_nombre()}")
print(f"Edad actualizada en meses: {mi_bebe.get_edad_meses()}")
mi_bebe.jugar()