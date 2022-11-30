import pygame
from pygame.locals import *
import sys

from prac05ej04ej06 import *

# Constantes adicionales
NUMFIL=16
NUMCOL=30
MINAS=99

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

PANTANCHO = 640     # Ancho de la pantalla
PANTALTO = 480      # Alto de la pantalla
(C_TAMX, C_TAMY) = COCULTAimage.get_size()  # Tamaño de las casillas
TAMSEP = 1          # Tamaño de la separación entre casillas

TABANCHO = ...      # Ancho del tablero (definir a partir de las anteriores)
TABALTO  = ...      # Alto del tablero (definir a partir de las anteriores)
TABORIGX = ...      # Origen X del tablero (definir a partir de las anteriores)
TABORIGY = ...      # Origen Y del tablero (definir a partir de las anteriores)

BLUE = (0, 0, 255)
GREY = (192, 192, 192)

    
def crear_imagen_tablero_visible():
    # El código de la función debe ir aquí
    ...
    return img_tablero

def colocar_casillas_tablero_visible(pant, x, y, img_tab, tab):
    # El código de la función debe ir aquí
    ...
    
def leer_movimiento_raton():
    # El código de la función debe ir aquí
    ...
    return fila, columna

def main():
    pygame.init()
    # Creación de la ventana
    screen = pygame.display.set_mode((PANTANCHO, PANTALTO))
    pygame.display.set_caption("BUSCAMINAS")

    screen.fill(BLUE)

    ...
    
    imagen_tablero=crear_imagen_tablero_visible()
    screen.blit(imagen_tablero, (TABORIGX,TABORIGY))
    colocar_casillas_tablero_visible(screen, TABORIGX, TABORIGY, imagen_tablero, ...)
    pygame.display.update()

    ...
    
    fin=False
    while not fin:

        ...
        
        colocar_casillas_tablero_visible(screen, TABORIGX, TABORIGY, imagen_tablero, ...)
        pygame.display.update()                       
    
    print 'El juego ha terminado.'
    pygame.quit()

if __name__ == "__main__":
    main()

