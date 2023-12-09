from abc import ABC, abstractmethod
class celular (ABC):
    @abstractmethod
    def __int__(self, color, almacenamiento):
        self.color = color
        self.almacenamiento = almacenamiento
    def informacion(self):
            print(f"color:{self.color}")
            print(f"almacenamiento: {self.almacenamiento}GB")
    def prendido(self):
        print("prendido celular")
    def apagar(self):
        print("apagar celular")
class android(celular):
    def __int__(self, color, almacenamiento):
        super(android, self).__int__(color, almacenamiento)
    def expandir_almacenamiento(self):
        print("expandiendo almacenamiento del celular")

class aiphone(celular):
    def __int__(self, color, archivos):
        super(aiphone, self).__int__(color, archivos)
    def transferir_archivos(self):
        print("transifiriendo archivos a la computadora")

# objeto = celular ("negro", 128)

