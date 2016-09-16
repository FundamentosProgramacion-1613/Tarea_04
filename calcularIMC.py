#Nombre Ian Gonzlez Pmanes
#Matricula A0373302
#Descripcin Programa que calcula el IMC y anuncia el estado.

def calcularIMC(altura, peso): 
    IMC = peso/altura**2
    return IMC
    
def main():
    altura = float( input("Cuanto mides? en metros"))
    peso = float( input("Cuanto pesas? en kilogramos"))
    
    if altura > 0 and peso > 0:
        if calcularIMC(altura, peso) < 18.5:
            print ("Tu IMC es:", calcularIMC(altura, peso), "Tienes bajo peso")
        elif calcularIMC(altura, peso) >= 18.5 and calcularIMC(altura, peso) <= 25:
            print ("Tu IMC es:", calcularIMC(altura, peso), "Tienes peso normal")
        elif calcularIMC(altura, peso) > 25:
             print ("Tu IMC es:", calcularIMC(altura, peso), "Tienes sobrepeso")
             
    else:
        print ("Esos no son valores validos")
        
main()