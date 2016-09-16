#encoding: UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descripción: Programa que calcula el IMC

#Inicio

def calcularIMC(masa,altura): #Función que calculará el IMC
    if (masa==0 or altura==0):
        IMC=("Los datos no pueden valer 0")
    elif (masa>0 and altura>0):
         IMC=masa/(altura**2)
    else:
        IMC=("Datos Invalidos")
    return IMC
    

def compararIMC(IMC): #Función que te dirá en que rango estás
    if (IMC==("Los datos no pueden valer 0")):
        res2=("No se puede calcular el IMC")
    elif (IMC>0 and IMC<18.5):
        res2= ("Tu peso es bajo")
    elif (IMC>= 18.5 and IMC<25):
        res2= ("Tu peso en normal")
    elif (IMC>=25):
        res2=("Tienes sobrepeso")
    else:
        res2=("No se puede calcular el IMC")
    return res2

def main(): #Función principal
    peso=float(input("Introduce tu peso en kilogramos"))
    altura=float(input("Introduce tu altura en metros"))
    res= calcularIMC(peso,altura)
    print ("IMC=" , str(res))
    restotal=compararIMC(res)
    print (restotal)

main()
#Fin