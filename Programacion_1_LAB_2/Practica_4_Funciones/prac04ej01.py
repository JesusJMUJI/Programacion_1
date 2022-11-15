from modulo_test import test

def es_narcisista (n):
    # El código de la función debe ir aquí
    
# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(es_narcisista(1) == True)
    test(es_narcisista(153) == True)
    test(es_narcisista(154) == False)
    test(es_narcisista(406) == False)
    test(es_narcisista(407) == True)
    test(es_narcisista(8208) == True)
    test(es_narcisista(92727) == True)
    test(es_narcisista(548834) == True)
    test(es_narcisista(24678051) == True)
