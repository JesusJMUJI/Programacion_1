n = int(input("Limite inferior del sumatorio: "))
m = int(input("Limite superior del sumatorio: "))
sumatorio = 0

if n > m :
    print("Error, el limite inferior debe ser menor que el superior")
while n <= m:
    sumatorio += n
    n += 1
    print(n)