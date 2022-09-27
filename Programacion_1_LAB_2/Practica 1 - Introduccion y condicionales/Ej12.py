horasPark = int(input("Horas aparcadas: "))
print(horasPark)
precioH = 0

if horasPark < 24:
    print("Solo se pueden introducir valores superiores a 24h")
else :
    precio = 11
    dias = horasPark / 24
    if dias > 2 and dias < 5:
        precioH = 6 * dias
        print(precioH)
    else:
        if dias > 6 and dias < 14:
          precioH = 5.5 * dias
          print(precioH)
        else:
            if dias > 15:
                precioH = 3.66 * dias
                print(precioH)
    print(dias)        



""" elif hPark > 24 and hPark < 48:
    precioH = hPark * 2.18
    print(precioH)
elif hPark > 48 and hPark < 120:
    precioH = hPark * 0.25
    print(precioH)
elif hPark > 144 and hPark < 336:
    precioH = hPark * 0.22916
    print(precioH)
elif hPark > 337:
    precioH = hPark * 110
    print(precioH) 

    2 y 5
    6 y 14
    15 

    """