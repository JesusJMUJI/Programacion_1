from random import *

codigo = ''
while len(codigo) < 4:
    n = str(randint (0,9))
    if not n in codigo:
        codigo += n
print(n)
print(codigo)

"""
from random import *

input = input("Introduce una cadena de 4 digitos: ")
cadenaRandom = str(randint(1,9))

if

codigo = ''
while len(codigo) < 4:
    n = randint (0,9)
        codigo += n
"""