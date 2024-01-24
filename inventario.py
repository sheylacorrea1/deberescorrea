class SistemaGestionInventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre, categoria, precio, cantidad):
        if nombre in self.inventario:
            print("El producto ya existe en el inventario.")
        else:
            self.inventario[nombre] = {"categoria": categoria, "precio": precio, "cantidad": cantidad}
            print("Producto agregado correctamente.")

    def actualizar_producto(self, nombre, categoria=None, precio=None, cantidad=None):
        if nombre in self.inventario:
            if categoria is not None:
                self.inventario[nombre]["categoria"] = categoria
            if precio is not None:
                self.inventario[nombre]["precio"] = precio
            if cantidad is not None:
                self.inventario[nombre]["cantidad"] = cantidad
            print("Producto actualizado correctamente.")
        else:
            print("El producto no existe en el inventario.")

    def eliminar_producto(self, nombre):
        if nombre in self.inventario:
            del self.inventario[nombre]
            print("Producto eliminado correctamente.")
        else:
            print("El producto no existe en el inventario.")

    def buscar_producto(self, nombre):
        if nombre in self.inventario:
            producto = self.inventario[nombre]
            print(f"Nombre: {nombre}, Categoría: {producto['categoria']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        print("Inventario:")
        for nombre, producto in self.inventario.items():
            print(f"Nombre: {nombre}, Categoría: {producto['categoria']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")


# Ejemplo de uso
sistema_inventario = SistemaGestionInventario()

sistema_inventario.agregar_producto("Manzanas", "Frutas", 2.99, 100)
sistema_inventario.agregar_producto("Leche", "Lácteos", 1.50, 50)
sistema_inventario.mostrar_inventario()

sistema_inventario.actualizar_producto("Manzanas", precio=3.49)
sistema_inventario.mostrar_inventario()

sistema_inventario.buscar_producto("Leche")

sistema_inventario.eliminar_producto("Manzanas")
sistema_inventario.mostrar_inventario()