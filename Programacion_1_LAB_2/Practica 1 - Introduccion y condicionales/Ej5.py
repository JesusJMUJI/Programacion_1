T = float(input("temperatura Cº: "))
V = float(input("velocidad del viento: "))

Ts = round(13.12 + 0.6215 * T - 11.37 * V ** 0.16 + 0.3965 * T * V ** 0.16 , 2)

print(Ts)
