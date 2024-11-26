# Capitulo 4 Ejercicio propuesto 22

NOMBRE = str(input("Ingrese el nombre del empleado: "))
SAL_HR = int(input("Digite el salario básico por hora: "))
HR = int(input("Ingrese las horas trabajadas en el mes: "))
SAL_MES = SAL_HR * HR
if SAL_MES > 450000:
    print(f"{NOMBRE}: {SAL_MES}")
else:
    print(NOMBRE)