import pygame
from pygame.locals import *
import sys

from prac05ej04ej06 import *

# Constantes adicionales
NUMFIL = 16
NUMCOL = 30
MINAS = 99

# Imágenes de las casillas
C0image = pygame.image.load('./empty.png')
C1image = pygame.image.load('./1.png')
C2image = pygame.image.load('./2.png')
C3image = pygame.image.load('./3.png')
C4image = pygame.image.load('./4.png')
C5image = pygame.image.load('./5.png')
C6image = pygame.image.load('./6.png')
C7image = pygame.image.load('./7.png')
C8image = pygame.image.load('./8.png')
CBOMBAimage = pygame.image.load('./bomb.png')
CFLAGimage = pygame.image.load('./flag.png')
COCULTAimage = pygame.image.load('./normal.png')

PANTANCHO = 1000  # Ancho de la pantalla
PANTALTO = 800  # Alto de la pantalla
(C_TAMX, C_TAMY) = COCULTAimage.get_size()  # Tamaño de las casillas
TAMSEP = 1  # Tamaño de la separación entre casillas

TABANCHO = PANTANCHO - 200  # Ancho del tablero (definir a partir de las anteriores)
TABALTO = PANTALTO - 200  # Alto del tablero (definir a partir de las anteriores)
TABORIGX = 100  # Origen X del tablero (definir a partir de las anteriores)
TABORIGY = 100  # Origen Y del tablero (definir a partir de las anteriores)
print(TABANCHO, TABALTO, TABORIGX, TABORIGY)

BLUE = (0, 0, 100)
GREY = (192, 192, 192)


def crear_imagen_tablero_visible():
	# El código de la función debe ir aquí
	imagen = pygame.Surface((TABANCHO, TABALTO))
	imagen.fill(GREY)
	return imagen


def colocar_casillas_tablero_visible(pant, x, y, img_tab, tab):
	# El código de la función debe ir aquí

	for i in range(len(tab)):
		for j in range(len(tab)):
			pant.blit(COCULTAimage, (x + j * C_TAMX, y + i * C_TAMY))


def leer_movimiento_raton():
	# El código de la función debe ir aquí
	pos = 0
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()

	pos_x = pos[0]
	pos_y = pos[1]
	if TABORIGX <= pos_x <= TABORIGX + TABANCHO and TABORIGY <= pos_y <= TABORIGY + TABALTO:
		fila = (pos_y - TABORIGY) // C_TAMY
		columna = (pos_x - TABORIGX) // C_TAMX
		return fila, columna
	else:
		return None


def main():
	pygame.init()
	# Creación de la ventana
	screen = pygame.display.set_mode((PANTANCHO, PANTALTO))
	pygame.display.set_caption("BUSCAMINAS")

	toculto = crear_tablero_oculto(NUMFIL, NUMCOL)
	tvisible = crear_tablero_visible(NUMFIL, NUMCOL)
	poner_bombas_tablero_oculto(toculto, MINAS)
	poner_info_tablero_oculto(toculto)

	imprimir_tablero(toculto)

	screen.fill(BLUE)
	imagen_tablero = crear_imagen_tablero_visible()
	screen.blit(imagen_tablero, (TABORIGX, TABORIGY))

	pygame.display.update()

	...

	fin = False
	while not fin:
		...

		colocar_casillas_tablero_visible(screen, TABORIGX, TABORIGY, imagen_tablero, tvisible)
		pygame.display.update()

	print('El juego ha terminado.')
	pygame.quit()


if __name__ == "__main__":
	main()
