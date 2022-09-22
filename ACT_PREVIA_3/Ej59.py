edad1 = int(input("Edad persona 1: "))
edad2 = int(input("Edad persona 2: "))

if edad1 < edad2:
    print("La persona 1 es más joven que la persona 2")
elif edad1 > edad2:
    print("La persona 2 es más joven que la persona 1")
elif edad1 == edad2:
    print("Ambas personas tienen la misma edad")