# Capitulo 4 Ejercicio resuelto 15

A = int(input("Indique el peso de la esfera A: "))
B = int(input("Indique el peso de la esfera B: "))
C = int(input("Indique el peso de la esfera C: "))
D = int(input("Indique el peso de la esfera D: "))
 
ESFERA_X = ""
PESO_X = ""

if (A == B) and (A == C):
    ESFERA_X += "D"
    if A < D:
        PESO_X += "mayor peso"
    else:  
        PESO_X += "menor peso"
elif (A == B) and (A == D):
    ESFERA_X += "C"
    if A < C:
        PESO_X += "mayor peso"
    else:  
        PESO_X += "menor peso"
elif (A == C) and (A == D):
    ESFERA_X += "B"
    if A < B:
        PESO_X += "mayor peso"
    else:  
        PESO_X += "menor peso"
elif (B == C) and (B == D):
    ESFERA_X += "A"
    if B < A:
        PESO_X += "mayor peso"
    else:  
        PESO_X += "menor peso"
         
print(f"la esfera {ESFERA_X} es la diferente y es de {PESO_X}")