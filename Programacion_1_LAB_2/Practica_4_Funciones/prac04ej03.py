from modulo_test import test
from ... import divisores

def son_amigos (n1,n2):
    # El código de la función debe ir aquí

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(son_amigos(30, 42) == False)
    test(son_amigos(42, 30) == False)
    test(son_amigos(220, 284) == True)
    test(son_amigos(284, 220) == True)
    test(son_amigos(2620, 2924) == True)
    test(son_amigos(6368, 6232) == True)
