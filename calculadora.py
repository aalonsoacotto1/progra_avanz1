# Modulo calculadora

def pedirEntrada():
	num = float(input("Ingrese el monto a pagar: "))
	return num

def pedirPrecio():
	num = float(input("Ingrese el precio del articulo: "))
	return num

#sumar
def sumar(num1, num2):
	return (num1+num2)

#restar
def restar(num1, num2):
	return (num1-num2)

#multiplicar
def multiplicar(num1, num2):
	return (num1*num2)

#dividir
def dividir(num1, num2):
	return (num1/num2)

# Exponente
# num^2 = num*num
# num^3 = num*num*num
# ...
def elevar(base, exp):
	temp = base
	for x in range(exp-1):
		temp *= base
	return temp
