class Conjunto:
    def __init__(self, conjunto, elemento):
        self.conjunto = []

    def __str__(self):
        for elemento in self.conjunto:
            print(elemento)
    

    def pertenece(self, elemento):
        elemento = None
        if elemento in self.conjunto:
            print("El elemento {0} esta dentro del conjunto".format(elemento))
            