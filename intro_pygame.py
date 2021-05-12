#Importamos el modulo de pygame
import pygame

# Ajustamos el tamaño de la pantalla y elegimos un titulo
title = "PONG"
size = [400, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption(title)

# Definimos nuestro clock-reloj (FPS)
clock = pygame.time.Clock()
FPS = 60

# guardamos la paleta de colores a utilizar...
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

# GAME LOOP
gameover = False

# Parámetros del personaje:
width = 10
height = 10
x_coord = 10
y_coord = 120
des_x = 0
des_y = 0
score = 0

# GENERAL
vel = 2

#parametros oponente
x_opo = 380
y_opo = 120
des_y_opo = 0
score_opo = 0

#pelota
x_pelota = 200
y_pelota = 150
vel_pelota = 2
direccion_x = 1 # si es positivo es derecha, negativo izquierda
direccion_y = 1 # si es positivo es abajo, negativo arriba
'''
	direccion_x		direccion_y
		1				1			abajo-derecha
		1				-1			arriba-derecha
		-1				1			abajo-izquierda
		-1				-1			arriba-izquierda
'''

def dibujarPersonaje(x, y, color, screen, w, h):
	return pygame.draw.rect(screen, color, (x,y,w,h*6))

def dibujarPelota(x, y, color, screen):
	return pygame.draw.rect(screen, color, (x,y,10,10))

while not gameover:
	# Recorremos lista de eventos
	for event in pygame.event.get():
		# Si hacemos click en cerrar (x)
		if event.type == pygame.QUIT:
			gameover = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				des_y = -vel
			elif event.key == pygame.K_DOWN:
				des_y = vel

			if event.key == pygame.K_w:
				des_y_opo = -vel
			elif event.key == pygame.K_s:
				des_y_opo = vel

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				des_y = 0
			elif event.key == pygame.K_DOWN:
				des_y = 0

			if event.key == pygame.K_w:
				des_y_opo = 0
			elif event.key == pygame.K_s:
				des_y_opo = 0
	
	# ejecutar acciones
	y_coord = y_coord + des_y
	y_opo = y_opo + des_y_opo
	# acciones de pelota update
	x_pelota += vel_pelota*direccion_x
	y_pelota += vel_pelota*direccion_y

	#colisiones
	#limites del campo
	#sup-inf
	if y_pelota > 290: # chocó con la parte de arriba
		direccion_y *= -1
	if y_pelota < 0: # chocó con la parte de abajo
		direccion_y *= -1
	#der-izq
	if x_pelota > 390: # choque con derecha
		# PUNTO PARA IZQ-barrita1
		score += 1
		print("SCORE:")
		print("Barrita 1: " + str(score))
		print("Barrita 2: " + str(score_opo))
		x_pelota = 190
		y_pelota = 150
		direccion_x *= -1
		vel_pelota += 0.75

	if x_pelota < 0: #choque con izquierda
		# PUNTO PARA DER-barrita2
		score_opo += 1
		print("SCORE:")
		print("Barrita 1: " + str(score))
		print("Barrita 2: " + str(score_opo))
		x_pelota = 190
		y_pelota = 150
		direccion_x *= -1
		vel_pelota += 0.75

	if score >= 5 or score_opo >= 5:
		gameover = True

	if y_coord >= 240:
		y_coord = 240
	if y_coord <= 0:
		y_coord = 0

	if y_opo >= 240:
		y_opo = 240
	if y_opo <= 0:
		y_opo = 0

	screen.fill(black)
	barrita1 = dibujarPersonaje(x_coord, y_coord, white, screen, width, height)
	barrita2 = dibujarPersonaje(x_opo, y_opo, white, screen, width, height)

	pelota = dibujarPelota(x_pelota, y_pelota, white, screen)

	if barrita1.colliderect(pelota):
		direccion_x *= -1
	if barrita2.colliderect(pelota):
		direccion_x *= -1

	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()