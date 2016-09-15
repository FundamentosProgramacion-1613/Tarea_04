#Encoding UTF-8
#Oswaldo Morales Rodriguez
#Calcula el IMC con la altura y peso

def calcularImc(peso, altura):
    if (peso<0) or (altura<=0):
        calculo=("Error")
    else:
        calculo=(peso/(altura**2))
    return calculo
    
def valorarImc(imc):
    if (imc<18.5):
        mensaje=("Bajo de peso")
    elif (imc>25):
        mensaje=("Sobrepeso")
    elif(imc=="Error"):
        mensaje=("Error")
    else:
        mensaje=("Peso Normal")
    return mensaje
    

def main():
    altura=float(input("Altura en metros"))
    peso=int(input("Peso en Kilogramos"))
    imc=calcularImc(peso, altura)
    resultadoImc=valorarImc(imc)
    print("Tu Indice de Masa Corporal es",imc)
    print("Estas en",resultadoImc)
main()
    

    