class Animal:
	def makeNoise(self):
		raise NotImplementedError

class Cat(Animal):
	def makeNoise(self):
		print("Meoooowwwww")

class Dog(Animal):
	def makeNoise(self):
		print("Woooooof")

a = Cat();
a.makeNoise() #Prints Meeeowwwwww

a = Dog();
a.makeNoise() #Prints Woooooof