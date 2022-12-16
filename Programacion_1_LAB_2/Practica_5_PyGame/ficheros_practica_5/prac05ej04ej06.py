import pygame
from pygame.locals import *
import sys

from random import randint

# Variables
toculto = []
tvisible = []
onoff = False

# Constantes
C0 = '0'
C1 = '1'
C2 = '2'
C3 = '3'
C4 = '4'
C5 = '5'
C6 = '6'
C7 = '7'
C8 = '8'
CBOMBA = 'B'
CFLAG = 'F'
COCULTA = '-'


# Función para crear el tablero visible
def crear_tablero_visible(filas, columnas):
	# El código de la función debe ir aquí
	tvisible = []
	for i in range(filas):
		tvisible.append([C0] * columnas)
	return tvisible


# Función para crear el tablero oculto
def crear_tablero_oculto(filas, columnas):
	# El código de la función debe ir aquí
	toculto = []
	for f in range(filas):
		toculto.append([COCULTA] * columnas)
	return toculto


# Función para poner las bombas en el tablero oculto
def poner_bombas_tablero_oculto(toculto, bombas):
	# El código de la función debe ir aquí
	i = 0
	while i < bombas:
		fila = randint(0, len(toculto) - 1)
		columna = randint(0, len(toculto) - 1)

		if toculto[fila][columna] != CBOMBA:
			toculto[fila][columna] = CBOMBA
			i += 1


# Función para poner la información en el tablero oculto
def poner_info_tablero_oculto(toculto):
	filas = len(toculto)
	columnas = len(toculto[0])

	for f in range(filas):
		for c in range(columnas):
			if toculto[f][c] != CBOMBA:
				adyacentes = []
				cont_bombas = 0
				# Añadir a adyacentes las tres casillas superiores, si las hay
				# (solo cuando f>0, teniendo en cuenta que para la superior izda.
				# c>0, y que para la superior dcha. c<columnas-1)
				if f > 0:
					if c > 0:
						adyacentes.append(toculto[f - 1][c - 1])
					adyacentes.append(toculto[f - 1][c])
					if c < columnas - 1:
						adyacentes.append(toculto[f - 1][c + 1])

				# Añadir a adyacentes las casillas a la izda. y la dcha., si las
				# hay (teniendo en cuenta que para la izda. c>0, y que para la
				# dcha c<columnas-1)
				if c > 0:
					adyacentes.append(toculto[f][c - 1])

				if c < columnas - 1:
					adyacentes.append(toculto[f][c + 1])

				# Añadir a adyacentes las tres casillas inferiores, si las hay
				# (solo cuando f<filas-1, teniendo en cuenta que para la inferior
				# izda. c>0, y que para la inferior dcha. c<columnas-1)
				if f < filas - 1:
					if c > 0:
						adyacentes.append(toculto[f + 1][c - 1])
					adyacentes.append(toculto[f + 1][c])
					if c < columnas - 1:
						adyacentes.append(toculto[f + 1][c + 1])

				# Recorrer adyacentes
				for elem in adyacentes:
					if elem == CBOMBA:
						cont_bombas += 1

				# Poner bombas según el numero de bombas adyacentes
				if cont_bombas == 0:
					toculto[f][c] = C0
				elif cont_bombas == 1:
					toculto[f][c] = C1
				elif cont_bombas == 2:
					toculto[f][c] = C2
				elif cont_bombas == 3:
					toculto[f][c] = C3
				elif cont_bombas == 4:
					toculto[f][c] = C4
				elif cont_bombas == 5:
					toculto[f][c] = C5
				elif cont_bombas == 6:
					toculto[f][c] = C6
				elif cont_bombas == 7:
					toculto[f][c] = C7
				elif cont_bombas == 8:
					toculto[f][c] = C8


def imprimir_tablero(tablero):
	# El código de la función debe ir aquí
	for i in range(len(tablero)):
		for j in range(len(tablero)):
			print(tablero[i][j], end='\t')
		print()


def tablero_visible_destapar(tvisible, toculto, fila, columna):
	# El código de la función debe ir aquí
	print("Introduce la fila y la columna a destapar")
	(fila, columna) = int(input('Introduce la fila: ')), int(input('Introduce la columna: '))
	if toculto[fila][columna] == CBOMBA:
		tvisible[fila][columna] = CBOMBA
		print("Has perdido")
		return False
	else:
		tvisible[fila][columna] = toculto[fila][columna]
		return True
# def tablero_visible_marcar(tvisible, fila, columna, onoff):
# El código de la función debe ir aquí


# def comprobar_tablero_visible(tvisible, toculto, bombas):
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
	tvisible = crear_tablero_visible(5, 5)
	toculto = crear_tablero_oculto(5, 5)

	imprimir_tablero(tvisible)
	imprimir_tablero(toculto)
	poner_bombas_tablero_oculto(toculto, 5)
	poner_info_tablero_oculto(toculto)
	imprimir_tablero(toculto)


# menu_buscaminas()


# –- Programa principal –-
# Ejecutar el test solo al ejecutar el fichero (y no al importarlo)
if __name__ == "__main__":
	# El código para probar todas las funciones anteriores debe ir aquí
	# ...
	main()
