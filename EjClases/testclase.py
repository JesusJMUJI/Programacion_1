class Persona:

    def __init__(self,
                 nombre,
                 dni,
                 edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def iniciales(self):
        cadena = ''
        for caracter in self.nombre:
            if caracter >= 'A' and caracter <= 'Z':
                cadena = cadena + caracter + '. '
        return cadena

    def __str__(self):
        cadena = 'Nombre: {0}\n'.format(self.nombre)
        cadena = cadena + 'DNI: {0}\n'.format(self.dni)
        cadena = cadena + 'Edad: {0}\n'.format(self.edad)
        return cadena


toni = Persona('Antion Perez', '382173987123', 23)
pedro = Persona('Perodnsadnas dasdas', '38127381', 23)

print(toni)
