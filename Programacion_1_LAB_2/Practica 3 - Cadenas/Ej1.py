print("Práctica 3 - Ejercicio 1")
print("")

word = input("Escribe una palabra en español para convertirla al gerundio en ingles:  ")
cadena = ''

if 'ar' in word or 'er' in word or 'ir' in word:
    palabra = word[:-2]
    cadena = palabra + 'ing'
    print(cadena)
else:
    cadena = word + 'tion'
    print(cadena)