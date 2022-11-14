n = 28
def es_perfecto(n):
	sumatorio = 0
	for i in range(1, n):
		if n % i == 0:
			sumatorio += i
	return sumatorio == n

print(es_perfecto(n))