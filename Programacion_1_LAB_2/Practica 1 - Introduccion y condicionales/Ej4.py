mi_nombre = "Jesus"
mi_edad = "20"
mi_ciudad = "Valencia"
mi_provincia = "Valencia"

nombre_compañero = "Alex"
ciudad_compañero = "Murcia"
edad_compañero = "17"
provincia_compañero = "Alicante"

print("Ej4 - a")
print(mi_edad == edad_compañero or mi_ciudad == ciudad_compañero)
print(" ")

print("Ej4 - b")
print(mi_ciudad and ciudad_compañero == "Castellón")
print(" ")

print("Ej4 - c")
print(mi_ciudad and ciudad_compañero != "Castellón")
print(" ")

print("Ej4 - d")
print(provincia_compañero == "Castellon" or provincia_compañero == "Valencia" or provincia_compañero == "Alicante")
print(" ")

print("Ej4 - e")
print(ciudad_compañero != "Castellon" or ciudad_compañero != "Valencia" or ciudad_compañero != "Alicante")
print(ciudad_compañero == "Castellon" or ciudad_compañero == "Valencia" or ciudad_compañero == "Alicante")
print(" ")

print("Ej4 - f")
print(mi_edad < edad_compañero or mi_edad > edad_compañero)
print(" ")

print("Fin ejercicio")
