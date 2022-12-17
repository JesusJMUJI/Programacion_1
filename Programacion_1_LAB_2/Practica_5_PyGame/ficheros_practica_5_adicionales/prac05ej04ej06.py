from random import randint

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
	for i in range(len(tablero)):
		for j in range(len(tablero)):
			print(tablero[i][j], end='\t')
		print()


# Función para destapar una casilla
def tablero_visible_destapar(tvisible, toculto, fila, columna):
	print()
	print("Destapando casilla")
	fila, columna = seleccionar_fila_columnas(fila, columna, "Introduce la fila y la columna a destapar")
	print()

	print("Has destapado la casilla {0},{1}".format(fila + 1, columna + 1))
	if toculto[fila][columna] == CBOMBA:
		tvisible[fila][columna] = CBOMBA
		print("Has perdido")
		return True
	else:
		tvisible[fila][columna] = toculto[fila][columna]
		return False


# Función para marcar una casilla
def tablero_visible_marcar(tvisible, fila, columna, onoff):
	celda_marcada = 0
	print()
	print("Marcando casilla...")

	columna, fila = seleccionar_fila_columnas(columna, fila, "Introduce la fila y la columna a marcar")
	if onoff:
		if tvisible[fila][columna] == C0:
			tvisible[fila][columna] = CFLAG
			celda_marcada = 1
			print("Has marcado la casilla {0},{1}".format(fila + 1, columna + 1))

	elif not onoff:
		if tvisible[fila][columna] == CFLAG:
			tvisible[fila][columna] = C0
			celda_marcada = -1
			print("Has desmarcado la casilla {0},{1}".format(fila + 1, columna + 1))

	else:
		print("Introduce una opción válida")
		print()
		celda_marcada = None

	return celda_marcada


# Función para comprobar las bombas restantes
def comprobar_tablero_visible(tvisible, toculto, bombas):
	bombas_reveladas = 0
	print()
	print("Comprobando tablero...")
	for i in range(len(tvisible)):
		for j in range(len(tvisible)):
			if tvisible[i][j] == CFLAG and toculto[i][j] == CBOMBA:
				bombas_reveladas += 1

	print()
	if bombas_reveladas == bombas:
		print("Has revelado todas las bombas")
		return True
	else:
		print("Aún te quedan bombas por revelar")
		return False


# Menú para las opciones del buscaminas
# HE INCLUIDO UNA OPCION SECRETA PARA ACTIVAR EL MODO DEBUG
def menu_buscaminas():
	print("Que quieres hacer?")
	print("1. Destapar casilla")
	print("2. Marcar casilla")
	print("3. Desmarcar casilla")
	print("4. Bombas por detectar")
	print("5. Salir")
	print()
	opcion = int(input('Introduce la opción: '))
	if opcion == 0:
		print("Estas intentando usar el modo debug")
	elif opcion < 1 or opcion > 5:
		print("Introduce una opción válida")
		opcion = int(input('Introduce la opción: '))

	print("Has elegido la opción {0}".format(opcion))
	print()
	return opcion


# Función global para seleccionar la fila y la columna
def seleccionar_fila_columnas(columna, fila, mensaje):
	print(mensaje)
	fila = int(input('Introduce la fila: ')) - 1
	columna = int(input('Introduce la columna: ')) - 1
	return columna, fila


# Bucle principal del programa
def main():
	# Printea las opciones de dificultad
	print("Bienvenido al buscaminas Pythonico")
	print("Que dificultad quieres?")
	print("1. Principiante")
	print("2. Intermedio")
	print("3. Experto")
	print()
	dificultad = int(input("Opción: "))
	print()

	# Inicializa el tablero visible y el tablero oculto según la dificultad
	filas = 0
	columnas = 0
	bombas = 0
	if dificultad == 1:
		filas = 8
		columnas = 8
		bombas = 10
	elif dificultad == 2:
		filas = 16
		columnas = 16
		bombas = 40
	elif dificultad == 3:
		filas = 16
		columnas = 30
		bombas = 99

	# Dificultad secreta muy fácil para debuggear
	elif dificultad == 4:
		print("Has elegido la dificultad secreta, solo hay una bomba")
		filas = 3
		columnas = 3
		bombas = 1

	else:
		print("Introduce una opción válida")
		print()
		main()

	tvisible = crear_tablero_visible(filas, columnas)
	toculto = crear_tablero_oculto(filas, columnas)
	onoff = None

	# Crear las bombas
	poner_bombas_tablero_oculto(toculto, bombas)
	poner_info_tablero_oculto(toculto)
	imprimir_tablero(tvisible)
	print()

	ganar = False
	perder = False

	# Bucle principal del juego
	while ganar == False and perder == False:
		opcion = menu_buscaminas()
		imprimir_tablero(tvisible)
		if opcion == 1:
			if tablero_visible_destapar(tvisible, toculto, filas, columnas):
				perder = True
				print("Has perdido!\n Tus marcas eran:")
				imprimir_tablero(tvisible)
				print("Las bombas estaban en:")
				imprimir_tablero(toculto)
			else:
				imprimir_tablero(tvisible)
				print()

		elif opcion == 2:
			tablero_visible_marcar(tvisible, filas, columnas, True)
			imprimir_tablero(tvisible)
			print()

		elif opcion == 3:
			tablero_visible_marcar(tvisible, filas, columnas, False)
			imprimir_tablero(tvisible)
			print()

		elif opcion == 4:
			if comprobar_tablero_visible(tvisible, toculto, bombas):
				ganar = True
				print("Has ganado!\nTus marcas estaban aqui:")
				imprimir_tablero(tvisible)
				print("Y las bombas estaban aqui:")
				imprimir_tablero(toculto)
			else:
				imprimir_tablero(tvisible)
				print()

		elif opcion == 5:
			print("Hasta luego, gracias por jugar")
			exit()

		# Opcion secreta para activar el modo debug
		elif opcion == 0:
			print("Quieres activar el modo debug? (s/n)")
			debug = input()
			if debug == "s":
				print("JUEGA DE FORMA RESPONSABLE ;)")
				print(
					"Tablero oculto, solo debug: {0} filas, {1} columnas y {2} bombas".format(filas, columnas, bombas))
				imprimir_tablero(toculto)
				print()


if __name__ == "__main__":
	main()
