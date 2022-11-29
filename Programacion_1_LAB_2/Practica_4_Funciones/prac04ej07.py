from modulo_test import test
from prac04ej03 import divisores

def son_sociables (lista):
    # El código de la función debe ir aquí
    i = -1
    es_social = True
    # for i in range(0, len(lista)):
    while es_social and i < len(lista) - 1:
        lista_div = divisores(lista[i])
        suma_lista = 0
        for j in range(0, len(lista_div) - 1):
            suma_lista += lista_div[j]

        if lista[i + 1] != suma_lista:
            es_social = False
        i += 1
    return es_social

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(son_sociables([220, 284]) == True)
    test(son_sociables([14288, 15472, 14536, 14264, 12496]) == True)
    test(son_sociables([14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, \
                        589786, 294896, 358336, 418904, 366556, 274924, 275444, \
                        243760, 376736, 381028, 285778, 152990, 122410, 97946, \
                        48976, 45946, 22976, 22744, 19916, 17716]) == True)
    test(son_sociables([28158165, 29902635, 30853845, 29971755]) == True)
