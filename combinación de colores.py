# encoding: UTF-8
#Blanca Flor Cldern Vzquez
#Mezclador  de  color


def combinarColores(color1,color2):
    if color1== "azul" or color1== "rojo" or color1== "amarillo":
        if color2== "azul" or color2== "rojo" or color2== "amarillo":
            if color1== "azul"   and color2== "azul" :
                color= "azul"
            elif color2== "azul" and color1== "azul":
                color ="azul"
            elif color2== "rojo" and color1== "rojo":
                color ="rojo"
            elif color1== "amarillo" and  color2== "amarillo":
                color ="amarillo"
            elif color1== "azul" and color2== "rojo":
                color ="violeta"
            elif color1== "azul" and color2== "amarillo":
                color ="verde"
            elif color1== "rojo" and   or color2== "rojo":
                color="rojo"
            elif  color2== "amarillo" and color1== "amarillo"  :
                color ="amarillo"
            elif  color2== "azul" and  color1== "rojo":
                color="violeta"
            elif color2== "azul"  and  color1== "amarillo":
                color="verde"
            elif  color2== "rojo" and color1== "amarillo":
                color="naranja"
        
        else:
            color= "error, ingresa bien tus datos"
    else:
        color= "error, ingresa bien tus datos"
        
    return color
    


def main():
    
    color1=int(input("ingresa el primer número de color que desees combinar(rojo, amarillo o azul)"))
    color2=int(input("ingresa el segundo numero de color que desees combinar(rojo, amarillo o azul)")) 
    colorResultante=combinarColores(color1,color2)
    print (colorResultante)

main()
