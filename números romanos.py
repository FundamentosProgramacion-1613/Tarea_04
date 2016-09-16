#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza
#Matricula del autor: A01378897
#Ejercicio n°1 de la tarea 4

def conversorDeNumeroARomano(numeroParaFuncion):
    if numeroParaFuncion < 4:
        numeroRomano = ( numeroParaFuncion * "I" )
    elif numeroParaFuncion == 4:
        numeroRomano = ( "IV")
    elif numeroParaFuncion == 5:
        numeroRomano = ("V")
    elif numeroParaFuncion > 5 and numeroParaFuncion < 9:
        numeroRomano = ("V" + (numeroParaFuncion - 5) * "I")
    elif numeroParaFuncion == 9:
        numeroRomano = "IX"
    else:
        numeroRomano = "X"
    return numeroRomano
    
    

def main():
    numeroSinConvertir = int(input("Teclee un numero, este será convertido a Romano"))
    
    if numeroSinConvertir >= 1 and numeroSinConvertir <= 10:
       print (conversorDeNumeroARomano(numeroSinConvertir))
    else:
       print ("Este programa soporta solo números del uno al diez positivos")       
       
       
       
main()