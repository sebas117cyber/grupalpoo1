# Capitulo 3 Ejercicio Propuesto 21
class Triangulo:
    def __init__(self,LadoA,LadoB,LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB 
        self.LadoC = LadoC
    def Perimetro(self):
        Perimetro = self.LadoA + self.LadoB + self.LadoC
        return Perimetro
    def Semiperimetro(self):
        Semiperimetro = round((self.LadoA+self.LadoB+self.LadoC)/2,1)
        return Semiperimetro

LadoA = float(input("Ingrese lado A del triangulo: "))
LadoB = float(input("Ingrese lado B del triangulo: "))
LadoC = float(input("Ingrese lado C del triangulo: "))

T = Triangulo(LadoA,LadoB,LadoC)

print(f"El perimetro del triángulo es: {T.Perimetro()} y su semiperimetro es: {T.Semiperimetro()}")