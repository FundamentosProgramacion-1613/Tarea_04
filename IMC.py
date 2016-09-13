#encoding: UTF-8
#Autor: Diego Perez aka DiegoCodes
#IMC

def calculadorIMC(masa,altura): #CALCULA IMC
    if (masa > 0 and altura >0):
        imc = masa/(altura*altura)
    else:
        imc = "ERROR"     
    return imc
    
def conclusionIMC(IMC): #EVALUA EL IMC, DA CONCLUSION
    if IMC < 18.5:
        conclusion = "UD. ESTA BAJO DE PESO"
    if IMC >= 18.5 and IMC <=25:
        conclusion = "UD. TIENE PESO NORMAL"
    if IMC > 25:
        conclusion = "UD. TIENE SOBREPESO"  
    return conclusion             
       
def main():
    masa = float(input("Ingrese masa en kg"))
    altura = float(input("Ingrese altura en m"))
    IMC = calculadorIMC(masa,altura)
    print("Su IMC es: %.2f" % IMC)  
    if (IMC != "ERROR"):     #COMPRUEBA QUE EL IMC ES VALIDO
        conclusion = conclusionIMC(IMC)
        print(conclusion)
main()    