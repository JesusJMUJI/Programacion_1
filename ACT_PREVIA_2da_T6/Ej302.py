from math import sqrt

def área_triangulo(a,b,c):
	s = (a+b+c)/2
	return sqrt(s*(s-a)*(s-b)*(s-c))

s = 4
print(área_triangulo(s-1, s, s+1))
print(s)
print(a)

# El valor de área_triangulo se imprime correctamente y da 6.0
# El valor de s se imprime correctamente y da 4
# El valor de a no está definido, por lo que no se puede imprimir
