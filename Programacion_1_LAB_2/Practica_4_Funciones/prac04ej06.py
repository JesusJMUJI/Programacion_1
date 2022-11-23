from modulo_test import test
from prac04ej04 import contenido_GC
from prac04ej05 import expansion_triplete_CAG


def menu_ADN():
	# El código de la función debe ir aquí
	opcion = 0
	while opcion != 1 and opcion != 2:
		print('1) Cálculo contenido de GC en ADN')
		print('2) Expansión de CAG en ADN')
		opcion = int(input("Escoge opción: "))
	return opcion


opcion_elegida = menu_ADN()
# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__ == '__main__':
	# El código del programa principal debe ir aquí
	if opcion_elegida == 1:
		test(contenido_GC('GCGC') == 100.0)
		test(contenido_GC('CGCG') == 100.0)
		test(contenido_GC('GACGAC') == 66.67)
		test(contenido_GC('TACGTACGTAT') == 36.36)
		test(contenido_GC('CAGTACTACCTCAGACGT') == 50.0)
		test(contenido_GC('GATCGATCGATGCTAGCTAGCGCATC') == 53.85)
	if opcion_elegida == 2:
		test(expansion_triplete_CAG('GACGAC') == None)
		test(expansion_triplete_CAG('CAGCAG') == 2)
		test(expansion_triplete_CAG('TACGTACGTAT') == None)
		test(expansion_triplete_CAG('CAGCAGTACCTCAGACGT') == 2)
		test(expansion_triplete_CAG('GATCGATCGATGCTAGCTAGCGCATC') == None)
		test(expansion_triplete_CAG('TACTCAGCAGGATGCAGCAGCAGCAGCAG') == 5)
