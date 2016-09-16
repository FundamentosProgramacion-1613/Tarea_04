#encoding: UTF-8
#Karla Valeria Alcntara Duarte A01373164
#Calcular Indice de Masa Corporal

def calcularIMC(peso,estatura):
    imc = peso/(estatura**2)
    return imc      
        
def identificarEstado(imc):       
    if imc<18.5:
        estado = "bajo de peso"
    elif imc>=18.5 and imc<25:
        estado = "en peso normal"
    else:
        estado = "con sobrepeso"
    return estado
    
def main():
    peso = int(input("Introduce el peso en kilogramos"))
    altura = float(input("Introduce la altura en metros"))
    if peso<0 or altura<0:
       print("Valores invalidos")
    elif altura==0:
       print("Valor invalido")
    else:
       imc = calcularIMC(peso,altura)
       estado = identificarEstado(imc)
       print("El IMC es %.02f"%imc,"por lo tanto se encuentra",estado)
     

main()