#Nombre Ian Gonzlez Pmanes
#Matricula A0373302
#Descripcin Programa que lee dos colores y da el producto de su mezcla

def mezclarColor(a,b):
    if (a == "ROJO" and b == "ROJO"):
        r = "ROJO"
    elif (a == "ROJO" and b == "AMARILLO") or (a == "AMARILLO" and b == "ROJO"):
        r = "NARANJA"
    elif (a == "ROJO" and b == "AZUL") or (a == "AZUL" and b == "ROJO"):
        r = "MORADO"
    elif( a == "AMARILLO" and b == "AMARILLO"):
        r = "AMARILLO"
    elif (a == "AMARILLO" and "b == AZUL") or (a == "AZUL" and b == "AMARILLO"):
        r = "VERDE"
    elif (a == "AZUL" and b == "AZUL"):
        r = "AZUL"
    
    return r
    
def main():
    color1 = str( input("Escribe un color (Rojo, Amarillo, Azul)"))
    color1 = color1.upper()
    color2 = str( input("Escribe un color (Rojo, Amarillo, Azul)"))
    color2 = color2.upper()
    
    if (color1 == "ROJO" or color1 == "AMARILLO" or color1 == "AZUL") and (color2 == "ROJO" or color2 == "AMARILLO" or color2 == "AZUL"):
        print ("El color resultante es:", mezclarColor(color1, color2))
    else:
        print ("Esa no es una entrada valida")
        
main()