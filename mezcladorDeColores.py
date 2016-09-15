#encoding: UTF-8
#Autor: Marina Itzel Haro Hernández, A01373471
#Este programa lee dos colores primarios (rojo, azul, amarillo) e imprime el color resultante al mezclarlos

#Función que te da el color resultante dependiendo de los colores que indique el usuario
def mezclarColores(color1, color2, color3):
    if (color1 == color2):
        return color3
    elif (color1 or color2 == "rojo") and (color2 or color1 == "azul"):
        return ("Morado")
    elif (color1 or color2 == "rojo") and (color2 or color1 == "amarillo"):
        return ("Naranja")
    elif (color1 or color2 == "azul") and (color2 or color1 == "amarillo"):
        return ("Verde")
    else:
        return("Error")
        
#Le pedimos al usuario dos colores entre azul, rojo y amarillo y llamamos a la función anterior para que nos de el color resultante        
def main():
    color3 = input("Coloca un color ya sea rojo, azul o amarillo")
    color4 = input("Coloca otro color ya sea rojo, azul o amarillo")
    color1 = color3.lower()
    color2 = color4.lower()
    mezclaColores = mezclarColores(color1, color2, color3)
    print ("El color resultante de", color3, "y", color4, "es", mezclaColores)
    
main()