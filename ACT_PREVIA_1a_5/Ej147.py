numeroDNI = int(input("Introduce el numero completo de tu DNI: "))
letraDNI = numeroDNI % 23
indexLetras = "TRWAGMYFPDXBNJZSQVHLCKE"
letraDNI = indexLetras[letraDNI]
print("Tu letra de DNI es: ", letraDNI)