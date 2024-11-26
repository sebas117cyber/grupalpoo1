# UML

import math

class Figuras:
    def __init__(self, figura):
        self.figura = figura

    def area(self):
        pass

    def perimetro(self):
        pass


class Circulo(Figuras):
    def __init__(self, radio):
        super().__init__("circulo")  
        self.radio = radio

    def area(self):
      area = (self.radio**2) * math.pi
      return area

    def perimetro(self):
      perimetro = (self.radio * 2) * math.pi 
      return perimetro

class Rectangulo(Figuras):
    def __init__(self, base, altura):
        super().__init__("rectangulo")
        self.base = base
        self.altura = altura

    def area(self):
        arearect = self.base * self.altura
        return arearect
    
    def perimetro(self):
        perimetrorect = (2 * self.base) + (2 * self.altura)
        return perimetrorect    

class Cuadrado(Figuras):
    def __init__(self, lado):
        super().__init__("cuadrado")
        self.lado = lado

    def area(self):
        arecuadra = self.lado ** 2
        return arecuadra
    
    def perimetro(self):
        perimecuadra = 4 * self.lado
        return perimecuadra

class Triangulo(Figuras):
    def __init__(self, base, altura):
        super().__init__("triangulo")
        self.base = base
        self.altura = altura

    def area(self):
        areatrian = (self.base * self.altura) / 2
        return areatrian
    
    def hipotenusa(self):
        hipote = math.sqrt((self.base / 2) ** 2 + self.altura ** 2)
        return hipote

    def perimetro(self):
        hipote = math.sqrt((self.base / 2) ** 2 + self.altura ** 2)
        perimetrian = self.base +  self.altura + hipote
        return perimetrian
    
    def tipotriangulo(self):
        hipote = math.sqrt((self.base / 2) ** 2 + self.altura ** 2)
        if self.base == self.altura and self.base == hipote and hipote == self.altura:
            print("El triangulo es equilatero ya que sus lados son iguales")
        elif self.base != self.altura and self.base != hipote and hipote != self.altura:
            print("El triangulo es escaleno ya que sus lados diferentes")
        else:
            print("El triangulo es isoceles dado que por lo menos un lado es diferente")


forma = input("¿Qué figura desea trabajar? ").strip().lower()

objeto = Figuras(forma)

if objeto.figura == "circulo":
    radio = float(input("¿Cuál es el radio del círculo? "))
    objeto = Circulo(radio) 
    print("Área del círculo:", objeto.area()) 
    print("Perímetro del círculo:", objeto.perimetro())

elif objeto.figura == "rectangulo":
  base = float(input("¿Cuál es la base del rectangulo? "))
  altura = float(input("¿Cuál es la altura del rectangulo? "))
  objeto = Rectangulo(base,altura) 
  print("Área del rectangulo:", objeto.area()) 
  print("Perímetro del rectangulo:", objeto.perimetro())

elif objeto.figura == "cuadrado":
  lado = float(input("¿Cuál es el lado del cuadrado? "))
  objeto = Cuadrado(lado) 
  print("Área del cuadrado:", objeto.area()) 
  print("Perímetro del cuadrado:", objeto.perimetro())
elif objeto.figura == "triangulo":
  base = float(input("¿Cuál es la base del triángulo? "))
  altura = float(input("¿Cuál es la altura del triángulo? "))
  objeto = Triangulo(base,altura) 
  objeto.tipotriangulo()
  print("Área del triangulo:", objeto.area()) 
  print("Perímetro del triangulo:", objeto.perimetro())
else:
    print("Figura no reconocida.")
