#encoding: UTF-8
#Autor: Aldo Fuentes A01373294
#Encontrar convinacion de colores


#Obtiene una combinacion de los colores primarios introducidos

def combinarColores(color1, color2):
    
    if color1 == "rojo":
        if color2 == "azul":
            combinacion = "Morado"
        elif color2 == "amarillo":
            combinacion = "Naranja"

    elif color1 == "azul":
        if color2 == "rojo":
            combinacion = "Morado"
        elif color2 == "amarillo":
            combinacion = "Verde"
            
    elif color1 == "amarillo":
        if color2 == "rojo":
            combinacion = "Naranja"
        elif color2 == "azul":
            combinarion = "Verde"
    
    if color1 == color2:
        combinacion = color1
    
    if color1 != "amarillo" and color1 != "rojo" and color1 != "azul":
        combinacion = "Error: " + color1 + " no es color primario"
        if color2 != "amarillo" and color2 != "rojo" and color2 != "azul" and color1 != "amarillo" and color1 != "rojo" and color1 != "azul":
            combinacion = "Error: " + color1 + " y " + color2 + " no son colores primarios"
    elif color2 != "amarillo" and color2 != "rojo" and color2 != "azul":
        combinacion = "Error: " + color2 + " no es color primario"
        
            
    
    return combinacion

def main():
    color1 = input("""Teclea un color primario
Ejemplo:
    Azul
    Amarillo
    Rojo""").lower()
    color2 = input("""Teclea otro color primario
Ejemplo:
    Azul
    Amarillo
    Rojo""").lower()
    
    combinacion = combinarColores(color1, color2)
    
    print(color1, "+", color2, "=", combinacion)



main()