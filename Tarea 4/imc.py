#encoding: UTF-8
#Autor: Aldo Fuentes A01373294
#Calcular y evaluar IMC


#Calcula el IMC con la formula peso/estatura**2
def calcularIMC(estatura, peso):
    imc = peso / estatura**2
    return imc
    
#Evalua el estado de acuerdo al imc
def evaluarIMC(imc):
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc <= 25:
        estado = "Peso normal"
    else:
        estado = "Sobrepeso"
    return estado



def main():

    estatura = float(input("Teclea tu estatura en metros"))
    peso = float(input("Teclea tu peso en kilogramos"))
    
    if estatura <= 0 or peso <= 0:
        print("Error")
    else:
        imc = calcularIMC(estatura, peso)
        estado = evaluarIMC(imc)
    
        print("IMC: ", "%.2f" % imc)
        print("Estado: ", estado)




main()