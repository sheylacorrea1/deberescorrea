#Encapsulacion
class cliente:
    def __int__(self):
        self._codigo = 1100
    def _cuenta(self):
        print("cuenta de procesamiento")
    def getcodigo(self):
        return self._codigo

persona = cliente()
#objeto._nombreclase_nombre atributo
print('persona', 'cliente', 'codigo')
print('1100')


