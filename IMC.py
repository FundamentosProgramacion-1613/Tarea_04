# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Cálculo del índice de masa corporal e indicar estado de la persona

# Función que calcula el índice de masa corporal
def calcularIMC(masa, estatura):
    imc = masa/(estatura**2)
    return imc

# Función que determina el estado de peso de una persona a partir de su IMC
def identificarEstado(imc):
    estado = ""
    if imc < 18.5:
        estado = "bajo peso"
    elif (imc >= 18.5 and imc <= 25):
        estado = "peso normal"
    else:
        estado = "sobrepeso"
    return estado
        
def main():
    peso = int(input("Introduce tu peso en kilogramos"))
    altura = float(input("Introduce tu altura en metros"))
    if peso<0 or altura<0:
        print("No se aceptan números negativos")
    elif altura == 0:
        print("No se aceptan estaturas de 0m")
    else:
        imc = calcularIMC(peso, altura)
        print("Tu índice de masa corporal es ", format(imc, ".2f"))
        print("Tu estado de acuerdo a tu IMC es ", identificarEstado(imc))
main()