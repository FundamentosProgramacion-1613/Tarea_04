#encoding:UTF-8
#Autor: Lenin Silva Gutirrez, A01373214
#Calcula el índice de masa corporal

def calcularIMC(masa, estatura): #Calcula el IMC
    imc=masa/(estatura**2)
    return imc
    
def indicarEstado(masa, estatura):
    imc=calcularIMC(masa,estatura) #Obtiene el IMC
    #Obtiene el estatus. Regresa el IMC y el estatus
    if imc<18.5:
        return imc, "bajo peso"
    elif imc<=25:
        return imc,"peso normal"
    else: 
        return imc,"sobrepeso" 
        
def main():
    masa=float(input("Masa"))
    estatura=float(input("Estatura"))
    
    if estatura<=0:
        print ("¡Estatura no válida!")
        return
    imc, estado=indicarEstado(masa, estatura)
    
    print ("Su IMC es de %.2f. Su estatus es: %s"%(imc, estado))
    
main()

