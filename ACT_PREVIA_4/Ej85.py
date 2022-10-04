nota = float(input('¿Cual es la nota del alumno: ? '))

if nota < 5:
    print (str(nota) + ' no es suficiente nota para aprobar')
    print ("El alumno esta suspenso")
else:
    if nota >= 5 and nota < 7:
        print(str(nota) + ' el alumno tiene un aprobado')
        print(' El alumno esta aprobado ')
    else:
        if nota <= 7 and nota > 9:
            print (str(nota) + ' el alumno tiene un notable')
            print ('El alumno esta aprobado')
        else:
            if nota <= 9 and nota > 10:
                print (str(nota) + 'el alumno tiene un sobresaliente')
                print ('El alumno esta aprobado')
            else:
                if nota == 10:
                    print(str(nota) + ' el alumno tiene una matrícula de honor')
                    print ('El alumno esta aprobado')