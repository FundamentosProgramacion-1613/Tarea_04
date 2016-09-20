#encoding: UTF-8
#Autor: Jess Perea
#Indicar si la persona tiene bajo pero, sobre peso o normal       

#empieza

def determinarComplexion(IMC):    #Determina si el usuario tiene sobre, bajo o normal peso
    if IMC < 18.5:
        complexion = "Bajopeso"
    elif IMC >= 18.5 and IMC <= 25:
        complexion = "Peso normal"
    elif IMC < 25:
        complexion = "Sobrepeso"
    return complexion
    
def calcularIMC(masa,estatura): #calcula el IMC
    if masa > 0 and estatura > 0:
        IMC = masa / (estatura*estatura)
    else:
        IMC = "Error. Teclea un valor valido (valores positivos)"
    return IMC
    
    
def main():
    masa = float(input("Teclea tu peso en kilogramos"))
    estatura = float(input("Teclea tu estatura en metros"))
    IMC = calcularIMC(masa,estatura)
    complexion = determinarComplexion(IMC)
    print("Tu Indice de Masa Corporal es:",IMC)
    print("Tu complexion es:",complexion)

main()