
#encoding:UTF-8

#Autor:José Javier Rodríguez Mota
#Descripción: Calcula el IMC de una persona

#Inicio
#Definimos nuestra función para obtener el IMC 
def obtenerIMC(masa,estatura):
    imc=masa/(estatura**2)       
    return imc
#Definimos nuestra función para revisar el imc
def analizarIMC(imc):
    if (0<=imc<18.5):
        resultado="Bajo de peso"
    elif(18.5<=imc<=25):
        resultado="Peso normal"
    elif(25<imc):
        resultado="Sobrepeso"        
    return resultado    
#Definimos nuestra función principal
def main():
    masa=float(input("¿Cuál es tu masa en kilogramos?"))
    estatura=float(input("¿Cuál es tu estatura en metros?"))
    if (estatura>0 and masa>0):
        imc=obtenerIMC(masa,estatura)
        analisis=analizarIMC(imc)
        print("""Dada la masa %.2f kg y la estatura %.2f m el IMC es de %.2f, por lo que el análisis es el siguiente:
%s """%(masa,estatura,imc,analisis))
    elif(estatura==0):
        print("ERROR: La estatura no puede ser 0")
    else:
        print("ERROR: Los valores deben ser mayores a 0")    
main()    