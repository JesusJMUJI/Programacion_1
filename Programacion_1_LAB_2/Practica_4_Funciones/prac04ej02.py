from modulo_test import test

def divisores (n):
    # El código de la función debe ir aquí
    lista_div = []
    for i in range(1,n+1):
        if n % i == 0:
            lista_div.append(i)
    return lista_div
# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(divisores(1) == [1])
    test(divisores(10) == [1, 2, 5, 10])
    test(divisores(9) == [1, 3, 9])
    test(divisores(10) == [1, 2, 5, 10])
    test(divisores(30) == [1, 2, 3, 5, 6, 10, 15, 30])
    test(divisores(35) == [1, 5, 7, 35])
    test(divisores(49) == [1, 7, 49])
