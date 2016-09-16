#encoding = UTF-8
#Adrian Tellez
# Sacar el IMC y el estado

def main():
    peso = float(input("Tu peso en kg"))
    altura = float(input("Tu altura en m"))
    IMC = calcularIMC(peso, altura)
    Peso = checarIMC(IMC)
    print ("IMC:", IMC)
    print (Peso)

def calcularIMC (peso, altura):
    if altura <= 0:
        return ("Error: pon una altura adecuada")
    if peso < 0:
        return ("Error: pon un peso adecuado")
    else:
        IMC = peso/(altura*altura)
        return IMC
        
def checarIMC(IMC):
    if IMC < 18.5:
        return ("Tienes bajo peso")
    if IMC >= 18.5 and IMC <= 25:
        return ("Tienes peso normal")
    else:
        return ("Tienes sobrepeso")   
        
    
main()