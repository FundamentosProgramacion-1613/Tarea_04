#encoding: UTF-8
#Karla Valeria Alcántara Duarte A01373164
#Identificar el color que se forma a partir de dos colores primarios.

def identificarColor(color1,color2):
    if color1=="rojo" and color2=="azul":
        color = "Morado"
        
    elif color1=="rojo" and color2=="amarillo":
        color = "Naranja"
        
    elif color1=="azul" and color2=="rojo":
        color = "Morado"
        
    elif color1=="azul" and color2=="amarillo":
        color = "Verde"
        
    elif color1=="amarillo" and color2=="rojo":
        color = "Naranja"
        
    elif color1=="amarillo" and color2=="azul":
        color = "Verde"
        
    elif color1=="rojo" and color2=="rojo":
        color = "Rojo"
        
    elif color1=="amarillo" and color2=="amarillo":
        color = "Amarillo"
        
    elif color1=="azul" and color2=="azul":
        color ="Azul"
        
    else:
        color = "Ninguno o uno de los colores no es primario."
    
    return color
    
    
def main():
    color1 = input("Dame el primer color")
    color2 = input("Dame ell segundo color")
    colorA = color1.lower()
    colorB = color2.lower()
    colorFinal = identificarColor(colorA,colorB)
    print(colorFinal)

main()

