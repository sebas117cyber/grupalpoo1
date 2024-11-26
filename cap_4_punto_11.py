# Capitulo 4 Ejercicio Resuelto 11
n = int(input("Cuantas comparaciones de 3 numeros (distintos) desea hacer?"))

for i in range(n):
    A = float(input("Ingrese el primer numero a comparar: "))
    B = float(input("Ingrese el segundo numero a comparar: "))
    C = float(input("Ingrese el tercer numero a comparar: "))
    while A == B or A == C or B == C:
        print("Ingresaste numeros iguales, por favor ingresa numeros diferentes entre sí.")
        A = float(input("Ingrese el primer numero a comparar: "))
        B = float(input("Ingrese el segundo numero a comparar: "))
        C = float(input("Ingrese el tercer numero a comparar: "))
    if (A > B) and (A > C) :
        print(f"El numero más grande fue el primero, que es {A}")
    elif (B > A) and (B > C):
        print(f"El numero más grande fue el segundo, que es {B}")
    elif (C > A) and (C > B):
        print(f"El numero más grande fue el tercero, que es {C}")