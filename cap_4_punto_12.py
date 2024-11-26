# Capitulo 4 Ejercicio Resuelto 12

class Empleado:
    def __init__(self,Nombre, HorasTrabajo,ValorHoras):
        self.Nombre = Nombre
        self.HorasTrabajo = HorasTrabajo
        self.ValorHoras = ValorHoras
    def PagoSemanal(self):
        if self.HorasTrabajo <= 40:
            PagoSemanal = self.HorasTrabajo*self.ValorHoras
            return PagoSemanal
        elif 48 >= self.HorasTrabajo > 40:
            ExcedenteHoras1 = (self.HorasTrabajo-40)
            HorasExtras1 = ExcedenteHoras1*(2*(self.ValorHoras))
            PagoSemanal = (40*self.ValorHoras)+HorasExtras1
            return PagoSemanal
        else:
            if self.HorasTrabajo > 48:
                ExcedenteHoras2 = (self.HorasTrabajo-48)
                HorasExtras2 = ExcedenteHoras2*(3*(self.ValorHoras))
                ExcedenteHoras1 = (self.HorasTrabajo-40)-ExcedenteHoras2
                HorasExtras1 = ExcedenteHoras1*(2*(self.ValorHoras))
                PagoSemanal = (40*self.ValorHoras)+HorasExtras1+HorasExtras2
                return PagoSemanal

n = int(input("¿Cuantos salarios semanales desea calcular?: "))

for i in range(n):
    Nombre = (input("Ingrese su nombre: "))
    HorasTrabajo = (int(input("Ingrese la cantidad de horas que trabajó en semana: ")))
    ValorHoras = (float(input("Ingrese el valor de cada hora de trabajo: ")))
    Nombre = Empleado(Nombre,HorasTrabajo,ValorHoras)
    print(f"{Nombre.Nombre} tiene un salario semanal de: ${Nombre.PagoSemanal()}")