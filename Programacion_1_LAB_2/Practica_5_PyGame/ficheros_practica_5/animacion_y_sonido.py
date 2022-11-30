import pygame
from pygame.locals import *
import time

# Constantes para la inicialización de la superficie de dibujo
SCREEN_W = 640
SCREEN_H = 480
WHITE = (255, 255, 255)

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
    (cat_size_x, cat_size_y) = cat.get_size()

    # Inicialización de ángulo de gato
    cat_angle = (input("¿Hacia que angulo quieres que vaya el gato?: "))
    
    # Bucle principal del juego
    finished = False
    direction = cat_angle
    screen.fill(WHITE)
    while not finished: 
        previous_direction = direction
        print(cat_x, cat_y)
        
        if direction == 'NE':
            cat_x += 5
            cat_y += 5
            if cat_x >= SCREEN_W or cat_y <= SCREEN_H:
                direction = 'SE'

        elif direction == 'SE':
            cat_x += 5
            cat_y -= 5
            if cat_x >= SCREEN_W or cat_y >= SCREEN_H:
                direction = 'SO'

        elif direction == 'SO':
            cat_x -= 5
            cat_y -= 5
            if cat_x <= SCREEN_W or cat_y >= SCREEN_H:
                direction = 'NO'

        elif direction == 'NO':
            cat_x -= 5
            cat_y += 5
            if cat_x <= SCREEN_W or cat_Y <= SCREEN_H:
                direction = 'NE'

        """
        if direction == 'E': # Este
            cat_x += 5
            if cat_x+cat_size_x >= SCREEN_W:
                cat_x -= 5
                direction = 'S'
        elif direction == 'S': # Sur
            cat_y += 5
            if cat_y+cat_size_y >= SCREEN_H:
                cat_y -= 5
                direction = 'O'
        elif direction == 'O': # Oeste
            cat_x -= 5
            if cat_x <= 0:
                cat_x += 5
                direction = 'N'
        elif direction == 'N': # Norte
            cat_y -= 5
            if cat_y <= 0:
                cat_y += 5
                direction = 'E'
        """        

        
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

if __name__ == '__main__':
    main()
