print("Práctica 3 - Ejercicio 3")
print("")

cadena1 = input("Dime una cadena: ")
cadena2 = input("Dime una posible subcadena de cadena: ")
coincidencias = 0
encontrado = False

for caracter in cadena1:
    if caracter == cadena2[coincidencias]:
        coincidencias += 1
    else:
        coincidencias = 0
    
    if len(cadena2) == coincidencias:
        encontrado = True
        print("")
        print(cadena2 + " es subcadena de " + cadena1)
        coincidencias = 0

if encontrado == False:
    print("")
    print(cadena2 + " NO es subcadena de " + cadena1)