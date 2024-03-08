class Libro:
    def __init__(self, titulo, autor, categoria, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ISBN = ISBN

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []

    def __str__(self):
        return self.nombre


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.ISBN] = libro

    def quitar_libro(self, ISBN):
        if ISBN in self.libros_disponibles:
            del self.libros_disponibles[ISBN]
        else:
            print("El libro no está disponible en la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario.usuario_id)

    def dar_baja_usuario(self, usuario):
        if usuario.usuario_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario.usuario_id)
        else:
            print("El usuario no está registrado en la biblioteca.")

    def prestar_libro(self, libro, usuario):
        if libro.ISBN in self.libros_disponibles:
            self.libros_disponibles.pop(libro.ISBN)
            usuario.libros_prestados.append(libro)
            print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
        else:
            print("El libro no está disponible en la biblioteca.")

    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            self.agregar_libro(libro)
            print(f"El libro '{libro.titulo}' ha sido devuelto.")
        else:
            print("El usuario no tiene prestado ese libro.")

    def buscar_libro(self, criterio, valor):
        libros_encontrados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                libros_encontrados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                libros_encontrados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear objetos de libro
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "9780142437230")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "9780307350488")
    libro3 = Libro("Python for Dummies", "Stef Maruch", "Programación", "9781119736218")

    # Crear objetos de usuario
    usuario1 = Usuario("Felipe", "001")
    usuario2 = Usuario("Laura", "002")

    # Crear objeto de biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Registrar usuarios en la biblioteca
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros a usuarios
    biblioteca.prestar_libro(libro1, usuario1)
    biblioteca.prestar_libro(libro2, usuario2)

    # Buscar libros por autor
    libros_encontrados = biblioteca.buscar_libro("autor", "García Márquez")
    print("Libros encontrados por autor:")
    for libro in libros_encontrados:
        print(libro)

    # Listar libros prestados a un usuario
    biblioteca.listar_libros_prestados(usuario1)

    # Devolver libro
    biblioteca.devolver_libro(libro1, usuario1)