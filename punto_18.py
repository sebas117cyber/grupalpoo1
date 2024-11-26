# Capitulo 3 ejecicio propuesto 18
class empleado:
    def __init__(self, codigo, nombre, horas_trabajas, valor_hora, porcereten):
        self.codigo = codigo
        self.nombre = nombre
        self.horas_trabajadass = horas_trabajas
        self.valor_hora = valor_hora
        self.porcereten = porcereten

    def salarioB(self):
        sabruto = self.horas_trabajadass * self.valor_hora
        return sabruto
    
    def salario_Neto(self):
        sabruto = self.horas_trabajadass * self.valor_hora
        resten = (self.porcereten/100) * sabruto

        return int(sabruto - resten)

perseo = empleado(1000324, "perseo", 56, 4500, 15)
print(perseo.salarioB(), perseo.salario_Neto())