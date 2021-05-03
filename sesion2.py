###MÉTODOS O FUNCIONES???
# Dinero y tiempo
# Tasa: 10% anual
# 										   $50
# Después del 1er año: $50 + ($50 * 10%) = $55
# Después del 2ndo año: $55 + ($55 * 10%) = $60.5
# Después del 3er año: $60.5 + ($60.5 * 10%) = $66.55
#						dinero*(1+tasa) = dinero + (dinero * 10%)
#[dinero(1 + tasa)](1 + tasa)(1 + tasa)(1 + tasa)(1 + tasa)(1 + tasa)
# dinero(1+tasa)^años

def interesCompuesto(inicial, tasa, años):
	# pow(x,y) = x^y
	return inicial*pow((1+tasa), años) # (1+tasa)^años

n = int(input("Cuantas inversiones quieres hacer? "))
for i in range(n):
	dinero = float(input("Ingresa el dinero que quieras invertir: "))
	tasa = float(input("Ingresa la tasa de inversión: "))
	años = int(input("A cuantos años será tu inversión: "))
	inversion = interesCompuesto(dinero, tasa, años)
	print(inversion)

### EJERCICIO (Funciones)
# Somos una caja registradora...
# El cliente nos paga con "x" cantidad de dinero, y compra un articulo de "y" precio
# Cuanto nos sobra? (imprimir)
# Podemos tener varios clientes (tenemos que usar un ciclo)
# Entrega por correo: alvaro.moreno@cetys.mx
# Fecha: Antes del lunes siguiente
# funcion recibe 2 parametros (dinero recibido, precio del producto)
# La funcion nos retorna cuantos billetes de "x" denominacion y/o monedas de "y" denominacion entregar
# Ejemplo 65.5 -> 3 billetes de 20, 1 moneda de 5 pesos, 1 50 centavos
# Limites Billetes: 100, 50, 20 ... Moneda: 50 centavos, 1 peso, 2 pesos, 5 pesos, 10 pesos