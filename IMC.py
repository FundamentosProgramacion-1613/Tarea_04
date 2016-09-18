#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran
#Problema 5

def calcularIMC(masa,estatura):
    IMC= float(masa/(estatura**2))
    return IMC
    
def calcularEstado(a):
    if a>=0 and a<18.5:
        print ("Tienes bajo peso")
    else:
        if a>=18.5 and a<25:
            print ("Tu peso es normal")
        else:
            if a>25:
                print ("Tienes sobrepeso")
            else:
                print ("error")
                
def main():
    masa= int(input("¿Cuanto pesas en kilogramos?"))
    estatura= float(input("¿Cuanto mides en metros?"))
    print ("Peso:",masa,"kg")
    print ("Estatura:",estatura,"m")
    a= calcularIMC(masa,estatura)
    print ("IMC:",a)
    calcularEstado(a)
    
main()