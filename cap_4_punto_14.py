# Capitulo 4 Ejercicio Propuesto 14

class Empresa:
    def __init__(self,Ventas1,Ventas2,Ventas3,SalarioE):
        self.Ventas1 = Ventas1
        self.Ventas2 = Ventas2
        self.Ventas3 = Ventas3
        self.SalarioE = SalarioE
    def Salario(self):
        totalventas = self.Ventas1 + self.Ventas2 + self.Ventas3
        porcentajeventas = (33/100)*totalventas
        if self.Ventas1 > porcentajeventas:
            salariofinal = (20/100)*self.SalarioE + self.SalarioE
            print(f"El salario de los vendedores del departamento 1 será de {salariofinal}")
        else:
            print(f"El salario de los vendedores del departamento 1 será de {self.SalarioE}")
        if self.Ventas2 > porcentajeventas:
            salariofinal = (20/100)*self.SalarioE + self.SalarioE
            print(f"El salario de los vendedores del departamento 2 será de {salariofinal}")
        else:
            print(f"El salario de los vendedores del departamento 2 será de {self.SalarioE}")
        if self.Ventas3 > porcentajeventas:
            salariofinal = (20/100)*self.SalarioE + self.SalarioE
            print(f"El salario de los vendedores del departamento 3 será de {salariofinal}")
        else:
            print(f"El salario de los vendedores del departamento 3 será de {self.SalarioE}")

Ventas1 = float(input("Ventas del departamento 1: $"))
Ventas2 = float(input("Ventas del departamento 2: $"))
Ventas3 = float(input("Ventas del departamento 3: $"))
SalarioE = float(input("El salario base de los vendedores: $"))
Comerciantes = Empresa(Ventas1,Ventas2,Ventas3,SalarioE)

Comerciantes.Salario()