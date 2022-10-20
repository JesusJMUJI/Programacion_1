elemento = 5
lista = [1,4,5,1,3,8]

for i in lista:
    #if elemento == i: 
        # Línea erronea: ahora mismo esta comparando el elemento con la i del for, 
        # por lo tanto, esta comaprandolo con la variable temporal en vez de la lista. 
        # se resolvería cambiando elemento == i por elemento in lista:
    if elemento in lista:
        pertenece = True
    else: 
        pertenece = False
if pertenece:
    print('Pertenece')
else:
    print('No pertenece')