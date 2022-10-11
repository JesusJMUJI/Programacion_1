n = int(input("Limite inferior del sumatorio: "))
m = int(input("Limite superior del sumatorio: "))
sumatorio = 0

while n <= m:
    sumatorio += n
    n += 1
    print(n)

print(m)