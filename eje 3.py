no1 = float(input("nota 1: "))
no2 = float(input("nota 2: "))
no3 = float(input("nota 3: "))

promedio = (no1 + no2 + no3) /3

if promedio >= 7:
    print("promocionado")
if promedio >=4 and promedio < 7:
    print("regular")
if promedio < 4:
    print("no habilita")