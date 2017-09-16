# Oscar Zuñiga Lara, A01654827
import math


def main():
    a = (input("Introduce color 1"))
    b = (input("Introduce color 2"))
    color1 = a.lower()
    color2 = b.lower()
    print(color2)
    print( color1)
    r = colorResultante(color1, color2)
    print(r)


def colorResultante(color1, color2):

    if color1 != "rojo" and color1 != "azul" and color1 != "amarillo":
        colorR = "Color 1 invalido"
    elif color2 != "rojo" and color2 != "azul" and color2 != "amarillo":
        colorR = "Color 2 invalido"
    elif color1 == color2:
        colorR = color1
    elif color1 == "azul" and color2 == "rojo":
        colorR = "Morado"
    elif color2 == "azul" and color1 == "rojo":
        colorR = "Morado"
    elif color1 == "rojo" and color2 == "amarillo":
        colorR = "Naranja"
    elif color2 == "rojo" and color1 == "amarillo":
        colorR = "Naranja"
    elif color1 == "azul" and color2 == "amarillo":
        colorR = "Verde"
    elif color2 == "azul" and color1 == "amarillo":
        colorR = "Verde"
    return colorR


main()
