# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripción: Programa que devuelve el color resultante de la mezcla de dos colores primarios

# Función que calcula el color resultante a partir de otros dos colores
def calcularMezcla(a,b):
    mezcla = ""
    if a==b:
        mezcla = a
    elif ((a == "rojo" and b == "azul") or (a == "azul" and b == "rojo")):
        mezcla = "morado"
    elif ((a == "rojo" and b == "amarillo") or (a == "amarillo" and b == "rojo")):
        mezcla = "naranja"
    else:
        mezcla = "verde"
    return mezcla
    
def main():
    color1 = input("Introduce le primer color primario")
    color2 = input("Introduce el segundo color primario")
    color1 = color1.lower()
    color2 = color2.lower()
    if ((color1 != "amarillo" and color1 != "rojo" and color1 != "azul") or (color2 != "amarillo" and color2 != "rojo" and color2 != "azul")):
        print("Has tecleado incorrectamente algún color o no introduciste un color primario")
    else:
        print("Tu mezcla es de color", calcularMezcla(color1, color2))
main()