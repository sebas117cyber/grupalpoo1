# Capitulo 4 ejercicio resuelto 10
NI = int(input("Digite el número de inscripción: "))
NOM = str(input("Ingrese el nombre: "))
PAT = int(input("Ingrese el patrimonio: "))
EST = int(input("Ingrese el estrato social: "))
CONST = 50000
PATLIM = 2000000
ESTLIM = 3
if PAT >= PATLIM and EST >= ESTLIM:
    EXTR = PAT*0.03
    CONST += int(EXTR)
print(f"El estudiante con número de inscripción {NI} y nombre {NOM} debe pagar ${CONST}")