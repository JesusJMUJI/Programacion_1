from random import randint

import pygame
from pygame.locals import *
import time

# Constantes para la inicialización de la superficie de dibujo
SCREEN_W = 640
SCREEN_H = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la velocidad de refresco
    FPS = 30
    fpsClock = pygame.time.Clock()

    # Inicialización de la superficie de dibujo (display surface)
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption('Gato con animación y sonido')

    # Inicialización del sonido
    beep = pygame.mixer.Sound('beeps.wav')
    # Inicialización de la imagen del gato y del color del fondo
    cat = pygame.image.load('cat.png')
    cat_x = int(input("Coodernada X del gato: "))
    cat_y = int(input("Coodernada X del gato: "))

    # Variables
    width, height = pygame.display.get_surface().get_size()
    (cat_size_x, cat_size_y) = cat.get_size()

    # Inicialización de ángulo de gato
    cat_angle = (input("¿Hacia que angulo quieres que vaya el gato?: "))
    cat_speed = int(input("¿A que velocidad quieres que vaya el gato?: "))

    # Bucle principal del juego
    finished = False
    direction = cat_angle
    screen.fill(WHITE)
    while not finished:
        previous_direction = direction
        print(cat_x, cat_y)
        print(direction)
        if direction == 'NE':
            cat_x += cat_speed
            cat_y += cat_speed
            if cat_x > width - cat_size_x or cat_y > height - cat_size_y:
                random_direction = randint(0, 1)
                if random_direction == 0:
                    direction = 'NO'
                else:
                    direction = 'SO'

        elif direction == 'SE':
            cat_x += cat_speed
            cat_y -= cat_speed
            if cat_x > width - cat_size_x or cat_y < 0:
                random_direction = randint(0, 1)
                if random_direction == 0:
                    direction = 'NE'
                else:
                    direction = 'SO'

        elif direction == 'SO':
            cat_x -= cat_speed
            cat_y -= cat_speed
            if cat_x < 0 or cat_y < 0:
                random_direction = randint(0, 1)
                if random_direction == 0:
                    direction = 'NE'
                else:
                    direction = 'NO'

        elif direction == 'NO':
            cat_x -= cat_speed
            cat_y += cat_speed
            if cat_x < 0 or cat_y > height - cat_size_y:
                random_direction = randint(0, 1)
                if random_direction == 0:
                    direction = 'NE'
                else:
                    direction = 'SE'

        if previous_direction != direction:
            beep.play()
            time.sleep(1)
            beep.stop()
        # Copiar la imagen del gato a la superficie de dibujo
        screen.fill(WHITE)
        screen.blit(cat, (cat_x, cat_y))
        # Tratar los eventos (teclado, ratón, etc)
        for event in pygame.event.get():
            if event.type == QUIT:
                finished = True
        # Visualizar en pantalla la superficie de dibujo
        pygame.display.update()
        fpsClock.tick(FPS)

    # Be IDLE friendly, my friend!!
    pygame.quit()


def punto_dentro(posx, posy, dimx, dimy, x, y):
    if posx <= x <= posx + dimx and posy <= y <= posy + dimy:
        return True
    else:
        return False



if __name__ == '__main__':
    main()
