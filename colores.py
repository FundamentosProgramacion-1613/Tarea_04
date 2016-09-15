#encoding: utf-8
#autor: Allan Sánchez Iparrazar
#Combinador de colores

def buscarEmpate(colorA,colorB):
    if colorB == "rojo" and colorA == "rojo" : 
        error = 1
    elif colorB == "azul" and colorA == "azul":
        error = 1
    
    elif colorB == "amarillo" and colorA == "amarillo":
        error = 1
    
    else : 
        error = 0
        
    return error
    
def buscarError (color):
    if color == "azul" or color == "rojo" or color == "amarillo" :
        error = 1
    else :
        error = 0
        
    return error
    
    
def combinarColores(colorA,colorB):
    if colorA == "azul" and colorB == "amarillo" :
        color = "VERDE" 
    elif colorA == "amarillo" and colorB == "azul" :
        color = "VERDE"
        
        
    elif colorA == "rojo" and colorB == "azul" :
        color = "MORADO"
    elif colorA == "azul" and colorB=="rojo" :
        color = "MORADO"
        
    elif colorA == "rojo" and colorB == "amarillo" :
        color = "NARANJA"
    elif colorA == "amarillo" and colorB == "rojo" :
        color = "NARANJA"
        
    return color



def main ():
    color1 = input("Ingresa un color; azul, amarillo o rojo")
    colorA = color1.lower()
    
    color2 = input("Ingresa otro color; azul, amarillo o rojo")
    colorB = color2.lower()
#--------------------------------------------------------------------

        
    empate = buscarEmpate(colorA,colorB)
    
    if empate == 0 : 
        error = buscarError (colorA and colorB)
        
        if error == 1:        
            combinacion = combinarColores (colorA,colorB)
            print("La combinación de los colores da ",combinacion)
        
        
        
        
        
        else : 
            print("Ingresa un color válido")
    else : 
        print("Ingresaste el mismo color")
    
    
    
    
    


main()