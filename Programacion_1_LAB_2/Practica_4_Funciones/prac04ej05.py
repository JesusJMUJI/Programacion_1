from modulo_test import test

def expansion_triplete_CAG (adn):
    # El código de la función debe ir aquí

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(expansion_triplete_CAG('GACGAC') == None)
    test(expansion_triplete_CAG('CAGCAG') == 2)
    test(expansion_triplete_CAG('TACGTACGTAT') == None)
    test(expansion_triplete_CAG('CAGCAGTACCTCAGACGT') == 2)
    test(expansion_triplete_CAG('GATCGATCGATGCTAGCTAGCGCATC') == None)
    test(expansion_triplete_CAG('TACTCAGCAGGATGCAGCAGCAGCAGCAG') == 5)
