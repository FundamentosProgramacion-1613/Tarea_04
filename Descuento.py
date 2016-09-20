#encoding: UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descripción: Programa que calcula el porcentaje de descuento en cierto número de paquetes

#Incio

def calcularDescuento(numpaq): #Función que nos dará el precio con descuento
    if (numpaq <=0):
        res1=str("No compraste ningún paquete")
    elif (numpaq>=10 and numpaq<=19):
        precio = numpaq*(1500*.8)
        res1 = ("El precio total será de $ %.2f, se aplicó el 20%%  de descuento" %precio)
    elif(numpaq<=49 and numpaq>=20):
        precio = numpaq*(1500*.7)
        res1=("El precio total será de $ %.2f, se aplicó el 30%% de descuento" %precio)
    elif (numpaq>=50 and numpaq<=99):
        precio = numpaq*(1500*.6
        res1=("El precio total será de $ %.2f, se aplicó el 40%% de descuento" %precio)
    elif (numpaq>=100):
        precio = numpaq*(1500*.5)
        res1=("El precio total será de $ %.2f, se aplicó el 50%% de descuento" %precio)
    else:
        precio = 1500*numpaq
        res1 = ("El total sería de $ %.2f, no se aplica descuento" %precio)
    return res1

def main(): #Función principal
    paquetes=int(input("Introduce el número de paquetes que adquiriste"))
    res = calcularDescuento(paquetes)
    print (res)
    

main()
