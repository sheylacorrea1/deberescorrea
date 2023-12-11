class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_disponibilidad(self):
        print(f"Disponibilidad en {self.nombre}:")
        for habitacion in self.habitaciones:
            estado = "Disponible" if habitacion.disponible else "Ocupada"
            print(f"- Habitación {habitacion.numero}: {estado}")

class Habitacion:
    def __init__(self, numero, tipo, capacidad):
        self.numero = numero
        self.tipo = tipo
        self.capacidad = capacidad
        self.disponible = True
        self.cliente_actual = None

    def reservar(self, cliente):
        if self.disponible:
            self.disponible = False
            self.cliente_actual = cliente
            print(f"{cliente.nombre} ha reservado la Habitación {self.numero}.")
        else:
            print(f"Lo siento, la Habitación {self.numero} no está disponible.")

    def liberar(self):
        self.disponible = True
        cliente_nombre = self.cliente_actual.nombre if self.cliente_actual else "N/A"
        print(f"Habitación {self.numero} liberada. Ocupada por: {cliente_nombre}")
        self.cliente_actual = None

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un hotel
    hotel = Hotel("Hotel Ejemplo")

    # Agregar habitaciones al hotel
    habitacion1 = Habitacion(101, "Doble", 2)
    habitacion2 = Habitacion(102, "Individual", 1)
    habitacion3 = Habitacion(103, "Suite", 3)

    hotel.agregar_habitacion(habitacion1)
    hotel.agregar_habitacion(habitacion2)
    hotel.agregar_habitacion(habitacion3)

    # Mostrar disponibilidad antes de reservar
    hotel.mostrar_disponibilidad()

    # Crear clientes
    cliente1 = Cliente("ALEX")
    cliente2 = Cliente("LUCIA")

    # Realizar reservas
    habitacion1.reservar(cliente1)
    habitacion2.reservar(cliente2)

    # Mostrar disponibilidad después de reservar
    hotel.mostrar_disponibilidad()

    # Liberar una habitación después de la estancia
    habitacion1.liberar()

    # Mostrar disponibilidad después de liberar
    hotel.mostrar_disponibilidad()

