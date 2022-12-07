import pygame
from pygame.locals import *
import sys

from random import randint

# Variables
toculto = []
tvisible = []
onoff = False

# Constantes
C0='0'
C1='1'
C2='2'
C3='3'
C4='4'
C5='5'
C6='6'
C7='7'
C8='8'
CBOMBA='B'
CFLAG='F'
COCULTA='-'

# Función para crear el tablero visible
def crear_tablero_visible(filas, columnas):
	# El código de la función debe ir aquí
	for i in filas:
		tvisible.append([C0].append(columnas))

# Función para crear el tablero oculto
def crear_tablero_oculto(filas, columnas):
	# El código de la función debe ir aquí
	for i in filas:
		toculto.append([COCULTA].append(columnas))

# Función para poner las bombas en el tablero oculto
def poner_bombas_tablero_oculto(toculto, bombas):
	# El código de la función debe ir aquí
	for i in bombas:
		toculto.append([CBOMBA].append(bombas))

# Función para poner la información en el tablero oculto
def poner_info_tablero_oculto(toculto):
	filas = len(toculto)
	columnas = len(toculto[0])

	for f in range(filas):
		for c in range(columnas):
			if toculto[f][c] != CBOMBA:
				adyacentes = []
				## Añadir a adyacentes las tres casillas superiores, si las hay
				## (solo cuando f>0, teniendo en cuenta que para la superior izda.
				## c>0, y que para la superior dcha. c<columnas-1)
				if f > 0:
					if c > 0:
						adyacentes.append(toculto[f-1][c-1])
					adyacentes.append(toculto[f-1][c])
					if c < columnas-1:
						adyacentes.append(toculto[f-1][c+1])


				## Añadir a adyacentes las casillas a la izda. y la dcha., si las
				## hay (teniendo en cuenta que para la izda. c>0, y que para la
				## dcha c<columnas-1)
				if c > 0:
					adyacentes.append(toculto[f][c-1])
				if c < columnas-1:
					adyacentes.append(toculto[f][c+1])
				## Añadir a adyacentes las tres casillas inferiores, si las hay
				## (solo cuando f<filas-1, teniendo en cuenta que para la inferior
				## izda. c>0, y que para la inferior dcha. c<columnas-1)
				if f < filas-1:
					if c > 0:
						adyacentes.append(toculto[f+1][c-1])
					adyacentes.append(toculto[f+1][c])
					if c < columnas-1:
						adyacentes.append(toculto[f+1][c+1])

				toculto[f][c] = str(adyacentes.count(CBOMBA))


def imprimir_tablero(tablero):
	# El código de la función debe ir aquí
	for i in (tablero):
		print(tablero)

def tablero_visible_destapar(tvisible, toculto, fila, columna):
	# El código de la función debe ir aquí



def tablero_visible_marcar(tvisible, fila, columna, onoff):
	# El código de la función debe ir aquí


def comprobar_tablero_visible(tvisible, toculto, bombas):
	# El código de la función debe ir aquí


def menu_buscaminas():
	# El código de la función debe ir aquí

	opcion = 0
	while opcion < 0 or opcion > 5:
		print("1. Destapar casilla")
		print("2. Marcar casilla")
		print("3. Comprobar tablero")
		print("4. Bombas por detectar")
		print("5. Salir")
		opcion = int(input("Opción: "))
	return opcion

def main():
	# El código de la función debe ir aquí
	imprimir_tablero(toculto)
	imprimir_tablero(tvisible)

	menu_buscaminas()



# –- Programa principal –-
# Ejecutar el test solo al ejecutar el fichero (y no al importarlo)
if __name__ == "__main__":
	# El código para probar todas las funciones anteriores debe ir aquí
	# ...
	main()
