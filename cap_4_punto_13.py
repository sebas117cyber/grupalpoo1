# Capitulo 4 Ejercicio resuelto 13
COMPRA = int(input("Digite el valor de la compra: "))
COLORBOL = str(input("Ingrese en MAYÚSCULA el color de la bolita: "))
PERCEN = 0
if COLORBOL == "BLANCO":
    PERCEN += 0
elif COLORBOL == "VERDE":
    PERCEN += 10
elif COLORBOL == "AMARILLO":
    PERCEN += 25
elif COLORBOL == "AZUL":
    PERCEN += 50
elif COLORBOL == "ROJO":
    PERCEN += 100

PAGO = int(COMPRA - (PERCEN*COMPRA/100))
print(f"El cliente debe pagar: ${PAGO}")