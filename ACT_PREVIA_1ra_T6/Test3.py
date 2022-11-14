def menú():
	opción = ''
	while not (opción >= 'a' and opción <= 'c'):
		print('Cajero automático.')
		print('a) Ingresar dinero.')
		print('b) Retirar dinero.')
		print('c) Consultar saldo.')
		opción = input('Seleccione una opción: ')
		if not (opción >= 'a' and opción <= 'c'):
			print('Solo puede escoger a, b o c. Intentelo de nuevo,')
	return opción


accion = menú()
