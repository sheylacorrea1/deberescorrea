class Animal:
	def makeNoise(self):
		raise NotImplementedError
class Cat(Animal):
	def makeNoise(self):
		print("Meoooowwwww")
<<<<<<< HEAD
class Dog(Animal):
	def makeNoise(self):
		print("Woooooof")
a = Cat()
a.makeNoise() #Prints Meeeowwwwww
=======

class Dog(Animal):
	def makeNoise(self):
		print("Woooooof")

a = Cat()
a.makeNoise() #Prints Meeeowwwwww

>>>>>>> b41d6d5 (polimorfismo)
a = Dog()
a.makeNoise() #Prints Woooooof