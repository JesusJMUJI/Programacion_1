from modulo_test import test
from prac04ej02 import divisores

def son_amigos (n1,n2):
    lista_1 = divisores(n1)
    suma_lista_1 = 0
    lista_2 = divisores(n2)
    suma_lista_2 = 0
    # El código de la función debe ir aquí
    for elem1 in lista_1:
        suma_lista_1 += elem1
    for elem2 in lista_2:
        suma_lista_2 += elem2


    
    if suma_lista_1 - n1 == n2 and suma_lista_2 - n2 == n1:
        return True
    else:
        return False
            
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
