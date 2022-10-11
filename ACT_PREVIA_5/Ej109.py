numInput = float(input("Introduce un número entre 0 y 10: "))

while numInput < 0 or numInput > 10:
    print("Número incorrecto")
    numInput = float(input("Introduce un número entre 0 y 10: "))
print("Número correcto")