# Capitulo 3 ejecicio propuesto 19

def perimetro(lado):
    peri = lado * 3
    print(f"El perimetro del triangulo es {peri}")

def altura(lado):
    base = lado / 2
    h = (lado ** 2) - (base ** 2)
    H = h ** 0.5
    print("La altura del triangulo equilatero es {}".format(round(H,2)))

def area(lado):
    base = lado / 2
    h = (lado ** 2) - (base ** 2)
    H = h ** 0.5
    are = (lado * H) / 2
    print(f"El area del triangulo equilatero es {round(are, 2)}")


lado = int(input("ingrese el lado del triangulo equilatero  "))
perimetro(lado)
altura(lado)
area(lado)
