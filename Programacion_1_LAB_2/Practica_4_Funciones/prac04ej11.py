from modulo_test import test

def es_cuadrado_latino (matriz):
    # El código de la función debe ir aquí

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!
    matriz2=[[1,2,3], \
             [2,3,1], \
             [3,1,2]]
    matriz3=[[1,2,3,4], \
             [2,1,4,3], \
             [3,4,1,2], \
             [4,3,2,1]]
    matriz4=[[1,2,3,4], \
             [3,4,1,2], \
             [4,3,2,1], \
             [2,1,4,3]]
    matriz5=[[1,2,3], \
             [0,3,1], \
             [3,1,2]]
    matriz6=[[1,2,3], \
             [2,3,4], \
             [3,1,2]]
    matriz7=[[1,2,3], \
             [2,3,1], \
             [1,2,3]]
    matriz8=[[1,2,3,4], \
             [2,1,4,3], \
             [3,4,1,2], \
             [1,3,2,4]]

    test(es_cuadrado_latino(matriz2) == True)
    test(es_cuadrado_latino(matriz3) == True)
    test(es_cuadrado_latino(matriz4) == True)
    test(es_cuadrado_latino(matriz5) == False)
    test(es_cuadrado_latino(matriz6) == False)
    test(es_cuadrado_latino(matriz7) == False)
    test(es_cuadrado_latino(matriz8) == False)
