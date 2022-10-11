n = int(input("Dime un numero: "))
m = int(input("Dime otro numero: "))
nm = n * m
i = 0

while n < nm:
    i += 1
    n *= i
    print(str(n) + ' * ' + str(i))
print('Done')