import os

class Inventario:
    def __init__(self, archivo):
        self.archivo = archivo
        self.inventario = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    producto, cantidad = linea.strip().split(',')
                    self.inventario[producto] = int(cantidad)
            print("Inventario cargado correctamente desde el archivo.")
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            self.guardar_inventario()
        except PermissionError:
            print("No se tiene permiso para acceder al archivo de inventario.")

    def guardar_inventario(self):
        with open(self.archivo, 'w') as file:
            for producto, cantidad in self.inventario.items():
                file.write(f"{producto},{cantidad}\n")
        print("Inventario guardado correctamente en el archivo.")

    def agregar_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad
        self.guardar_inventario()

    def actualizar_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] = cantidad
            self.guardar_inventario()
        else:
            print(f"El producto '{producto}' no existe en el inventario.")

    def eliminar_producto(self, producto):
        if producto in self.inventario:
            del self.inventario[producto]
            self.guardar_inventario()
        else:
            print(f"El producto '{producto}' no existe en el inventario.")


def menu():
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Salir")

def main():
    archivo_inventario = "inventario.txt"
    inventario = Inventario(archivo_inventario)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            inventario.agregar_producto(producto, cantidad)
        elif opcion == '2':
            producto = input("Ingrese el nombre del producto a actualizar: ")
            cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_producto(producto, cantidad)
        elif opcion == '3':
            producto = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(producto)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()