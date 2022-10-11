""" i = 0
while i < 1000:
    print(i)
    i += 1
print('Hecho') """

sumatorio = 0
i = 1
while i < 1000:
    i += 1
    sumatorio += i
    
    print('sumatorio: ' + str(sumatorio))
    print('i:' + str(i))
print(sumatorio)