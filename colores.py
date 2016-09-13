#encoding: UTF-8
#Autor: Diego Perez aka DiegoCodes
#MEZCLADOR_DE_COLORES

def mezclador(c1,c2):   # COMBINA LOS COLORES PREVIAMENTE EVALUADOS COMO VALIDOS     
    if (c1.lower() == "rojo"):
        if (c2.lower()  == "azul"):
            col = "morado"
        if (c2.lower()  == "amarillo"):
            col = "naranja"  
        if (c2.lower()  == "rojo"):
            col = "rojo"
            
    if (c1.lower()  == "azul"):
        if (c2.lower()  == "rojo"):
            col = "Morado"
        if (c2.lower()  == "amarillo"):
            col = "verde"  
        if (c2.lower()  == "azul"):
            col = "azul"
            
    if (c1.lower()  == "amarillo"):
        if (c2.lower()  == "azul"):
            col = "verde"
        if (c2.lower()  == "amarillo"):
            col = "amarillo"  
        if (c2.lower()  == "rojo"):
            col = "naranja" 
    return col
                                                                                                                                                  
def main():
    c1 = input("Escriba un color primario")
    c2 = input("Escriba otro color primario")
    #EVALUADOR DE QUE SEAN VALIDOS PREVIO A LA FUNCION
    if (c1.lower() == "rojo" or c1.lower() == "azul" or c1.lower() == "amarillo") and (c2.lower() == "rojo" or c2.lower() == "azul" or c2.lower() == "amarillo"):
        col = mezclador(c1,c2)
    else:
        col = "ERROR!"     
        
    print(col)
main()                                                                                                                                                                                                                                                                                                           