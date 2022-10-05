for numero in range (1,111):
    if numero % 3 != 0 or numero % 5 != 0 or numero % 7 != 0:  
        print(numero, end='')
        if numero % 3 == 0:
            print('Cosa', end ='')
        if numero % 5 == 0:
            print('Losa', end ='')
        if numero % 7 == 0:
            print('Wosa' , end ='')
    else:
        print (numero, end='')
    if numero % 11 == 0:
        print()
    else:
        print(' ', end='')