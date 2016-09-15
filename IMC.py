#encoding: utf-8
#autor: Allan Sánchez Iparrazar
#Indice de Masa Corporal

def calcularIMC(peso,estatura):
    IMC = peso/(estatura*estatura)
    return IMC



def determinarIMC(IMC):
    if IMC < 18.5 :
        tipoDePeso = "bajo peso"
        
    elif IMC > 18.5 and IMC < 25 :
        tipoDePeso = "peso normal"
        
    elif IMC > 25 :
        tipoDePeso = "sobrepeso"
        
    return tipoDePeso
    


def main():
    
    peso = float(input("Ingrese su peso en Kg"))
    estatura = float(input("Ingrese su estatura en metros"))
            
    if peso > 0 and estatura > 0 :
        IMC = calcularIMC(peso,estatura)
        tipoDePeso = determinarIMC(IMC)
        print("Usted tiene",tipoDePeso)
        print("Su peso es de %.2f"%IMC)
        
    
    else :
        print("### Error ###")
        
    
main()