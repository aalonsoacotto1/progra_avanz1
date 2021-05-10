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

# GENERAL
vel = 2

#parametros oponente
x_opo = 380
y_opo = 120
des_y_opo = 0

def dibujarPersonaje(x, y, color, screen, w, h):
	pygame.draw.rect(screen, color, (x,y,w,h*6))

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

	screen.fill(red)
	dibujarPersonaje(x_coord, y_coord, white, screen, width, height)
	dibujarPersonaje(x_opo, y_opo, white, screen, width, height)
	pygame.display.flip()
	clock.tick(FPS)
	
pygame.quit()