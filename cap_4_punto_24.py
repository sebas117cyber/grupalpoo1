# Capitulo 4 Ejercicio Propuesto 24
n = int(input("Cuantas comparaciones de peso (en kg) desea hacer? "))

for i in range(n):
    A = float(input("Ingrese el peso de la primera esfera (solo el numero): "))
    B = float(input("Ingrese el peso de la segunda esfera (solo el numero): "))
    C = float(input("Ingrese el peso de la tercera esfera (solo el numero): "))
    while A == B or A == C or B == C:
        print("Ingresaste pesos iguales, por favor ingresa pesos diferentes entre sí.")
        A = float(input("Ingrese el peso de la primera esfera (solo el numero): "))
        B = float(input("Ingrese el peso de la segunda esfera (solo el numero): "))
        C = float(input("Ingrese el peso de la tercera esfera (solo el numero): "))
    if (A > B) and (A > C) :
        print(f"La esfera más pesada fue la primera, que pesa {A}kg")
    elif (B > A) and (B > C):
        print(f"La esfera más pesada fue la segunda, que pesa {B}kg")
    elif (C > A) and (C > B):
        print(f"La esfera más pesada fue la tercera, que pesa {C}kg")
    else:
        print("Las 3 esferas pesan lo mismo")