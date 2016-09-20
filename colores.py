#encoding: UTF-8
# Autor: Marlon Brandon Velasco Pinello, A01379404
# Descripcion: colores Tarea 4

#funcion para convertir colores a minusculas
def convertirMinusMayus(color):
    a=color
    b=a.lower()
    return b
   
#funcion para comparar colores 
def compararColores(color1,color2):
    if (color1==color2):
        resultado=color1
    elif (color1=="rojo" and color2=="azul"):
        resultado="morado"
    elif (color2=="rojo" and color1=="azul"):
        resultado="morado"
    elif (color1=="rojo" and color2=="amarillo"):
        resultado="naranja"
    elif (color2=="rojo" and color1=="amarillo"):
        resultado="naranja"
    else:
        resultado="verde"
    return resultado

#funcion principal main  
def main():
    print("Los colores a elegir son Rojo, Azul, Amarillo")
    colorA=input("Ingresa el primer color")
    colorB=input("Ingresa el segundo color")
    color1=convertirMinusMayus(colorA)
    color2=convertirMinusMayus(colorB)
    if (color1=="rojo" or color1=="azul" or color1 == "amarillo"):
        if(color2=="rojo" or color2=="azul" or color2 == "amarillo"):
            resultado=compararColores(color1,color2)
    else:
        resultado="Error: Colores invalidos"
    print(resultado)
    
main()