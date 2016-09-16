# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Cálculo de descuentos aplicados en una compañía de software

# Función que devuelve el total a pagar al aplicar un descuento
def calcularTotal(n):
    total = 0
    if n < 10:
        total = n*1500
    elif n >= 10 and n <= 19:
        total = n*1500*0.8
    elif n >= 20 and n <= 49:
        total = n*1500*0.7
    elif n >= 50 and n <= 99:
        total = n*1500*0.6
    else:
        total = n*1500*0.5
    return total

def main():
    paquete = int(input("Introduce el número de paquetes comprados"))
    if paquete<0:
        print("Tienes que teclear un número positivo")
    else:
        print("La cantidad descontada fue de $", format(paquete*1500-calcularTotal(paquete),".2f"), sep="")
        print("El total a pagar es de $", format(calcularTotal(paquete),".2f"), sep="")
main()