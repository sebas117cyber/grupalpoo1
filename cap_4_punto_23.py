# Capitulo 4 Ejercicio Propuesto 23
import math

n = int(input("Cuantos cálculos desea realizar con la ecuación de segundo grado? "))

for i in range(n):
    A = float(input("Ingrese el valor de A: "))
    B = float(input("Ingrese el valor de B: "))
    C = float(input("Ingrese el valor de C: "))
    det = (math.pow(B,2)-(4*A*C))
    if det > 0:
        X = math.sqrt(det)
        S1 = ((-1)*B + X)/2*A
        S2 = ((-1)*B - X)/2*A
        print(f"Las soluciones de la ecuación ({int(A)})X^2+({int(B)})X+({int(C)}) son {S1} y {S2}")
    else:
        print("La ecuación no tiene soluciones reales")