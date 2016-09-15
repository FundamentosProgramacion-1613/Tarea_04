#encoding: UTF-8
#Autor: Marina Itzel Haro Hernndez, A01373471
#Este programa pide el  peso de una persona en kilogramos y la estatura en metros para calcular el IMC e indica si la persona tiene bajo peso, peso normal o sobrepeso

#Función que calcula el IMC dependiendo el peso y la estatura
def calcularIMC(peso, estatura):
    if peso>0 and estatura>0:
        IMC = peso/((estatura)**2)
        return IMC
    elif peso<0:
        if estatura<=0:
            return ("Error: Valores negativos no válidos")

#Función que define si tienes bajo peso, peso normal o sobrepeso
def definirEstado(IMC):
    if IMC< 18.5:
        return ("tienes bajo peso")
    elif IMC>=18.5 and IMC<25:
        return ("tienes peso normal")
    elif IMC>=25:
        return ("tienes sobrepeso")

#Pedimos el peso, la altura y mandamos llamar las dos funciones para calcula IMC y definir su estado
def main():
    peso = float(input("Coloca tu peso en kilogramos"))
    altura = float(input("Coloca tu altura en metros"))
    IMC = calcularIMC(peso, altura)
    estado = definirEstado(IMC)
    print ("Tu IMC es: %.2f " % (IMC))
    print ("Y", estado)
    
    
main()
    
