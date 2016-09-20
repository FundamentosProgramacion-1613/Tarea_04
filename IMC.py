# encoding: UTF-8
#Blanca Flor Cldern Vzquez
#IMC 

def calcularIMC(estatura,peso):
    if estatura >0 and peso>0:
        IMC=estatura/peso**2
    else :
        IMC="ingresa numeros positivos y diferentes de cero"    
    return IMC

def main():
    estatura=float(input("Ingresa la estatura en metros"))
    peso=float(input("ingresa la estatura en Kg"))
    
    IMC=calcularIMC(estatura,peso)
    if IMC>0 and IMC<800:   
        if IMC<18.6:
            tuIMC="Estas con desnutrición"
        elif IMC>18.6 and IMC<=25:
            tuIMC="Estas chido"
        elif IMC>25:
            tuIMC="Ya bajale a los tacos"
    else :
        tuIMC="porfavor"  
   #Es más divertido cuando pones resultados sarcasticos o tontos
    print (IMC, tuIMC)

main()




