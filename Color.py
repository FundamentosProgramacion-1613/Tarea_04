#encoding: UTF-8
#Adrian E. Tellez Lopez
#Tomar 2 colores primarios y sacar la mezcla

def main():
    color1 = raw_input("Pon el primer color primario")
    color2 = raw_input("Pon el segundo color primario")
    combina = mezclarColor (color1, color2)
    print ("La combinacion de", color1, "y", color2, "es", combina)


def mezclarColor (color1, color2):
    Color1 = color1.upper()
    Color2 = color2.upper()
    if Color1 == "AZUL":
        if Color2 == "AMARILLO":
            mezcla = "verde"
        elif Color2 == "ROJO":
            mezcla = "morado"
    
    elif Color1 == Color2:
        return color1
    
    
    elif Color1 == "ROJO":
        if Color2 == "AMARILLO":
            mezcla = "naranja"
        elif Color2 == "AZUL":
            return "morado"
            
    elif Color1 == "AMARILLO":
        if Color2 == "ROJO":
            mezcla = "naranja"
        elif Color2 == "AZUL":
            mezcla = "verde"
    else:
        return "Error: pon un color primario"
      
    return mezcla 


main()