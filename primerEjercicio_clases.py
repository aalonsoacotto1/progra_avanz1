class Animal:
	def __init__(self, tipo, nombre):
		self.tipo = tipo
		self.nombre = nombre
		self.pasos = 0

	def caminar(self):
		self.pasos += 1
		print("Caminando...")

	def ruido(self):
		if self.tipo == 'perro':
			print("Ladrando...")
		elif self.tipo == 'gato':
			print("Maullando...")
		else:
			print("Currucu")

class Ornitorrinco(Animal):
	def __init__(self, nombre):
		Animal.__init__(self, "ornitorrinco", nombre)

	def oigan_y_perry(self):
		print("prrrrrrrrrrr....")




perrito = Animal("perro", "sparky")
gatito = Animal("gato", "bigotes")
paloma = Animal("paloma", "KFC")
orni = Ornitorrinco("perry")


num1 = "20"

num2 = "7"

resultado = num1+num2

print(resultado)