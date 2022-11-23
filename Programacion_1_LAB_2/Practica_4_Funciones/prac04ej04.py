from modulo_test import test

def contenido_GC (adn):
    # El código de la función debe ir aquí
    contador = 0
    for elem in adn:
        if elem == 'G':
            contador += 1
        elif elem == 'C':
            contador += 1
    porcentaje = (contador / len(adn)) * 100
    print("Procentaje: {:.2f}".format(porcentaje))
    return round(porcentaje, 2)

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!
    test(contenido_GC('GCGC') == 100.0)
    test(contenido_GC('CGCG') == 100.0)
    test(contenido_GC('GACGAC') == 66.67)
    test(contenido_GC('TACGTACGTAT') == 36.36)
    test(contenido_GC('CAGTACTACCTCAGACGT') == 50.0)
    test(contenido_GC('GATCGATCGATGCTAGCTAGCGCATC') == 53.85)
