### Investigacion (Modulos)
# 1: Uso de Modulo tkinter: Crear una interfaz grafica (GUI) básica que sea de 600 px de ancho y 400 px de alto, fondo negro y un botton en el centro de la pantalla
# 2: Como hacer manejo de archivos: Leer un archivo y mostrarlo en pantalla (consola), posteriormente agregar una linea al final del documento
# 3: Como hacer nuestros propios modulos: El ejercicio de la Caja Registradora (la funcion/metodo que se hizo) habrá que ponerlo en un módulo que podamos importar


### EJEMPLO DE LECTURA completa y generar un array (list) de cada linea:
##file_open = open('ejemplo.txt')
#print(file_open.readlines())  #  Nos retorna una lista o array de cada linea... 
#file_open.close()

### Ejemplo de escritura en python a un archivo de texto que ya tiene informacion, es decir: APPEND:
def escribirArchivo(archivo, texto):
	with open(archivo, 'a') as escritura:
		escritura.write('\n'+str(texto))

arch = 'ejemplo.txt'
miVar = input('Ingrese algo: ')
escribirArchivo(arch, miVar)