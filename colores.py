
#encoding:UTF-8

#Autor:José Javier Rodríguez Mota
#Descripción: Imprime la combinación de dos colores primarios

#Inicio
#Definimos nuestra función para obtener la combinación de colores 
def mezclarColores(color1,color2):
    if (not((color1=="azul" or color1=="rojo" or color1=="amarillo")and(color2=="azul" or color2=="rojo" or color2=="amarillo"))):
        resultado ="Error, alguno de los dos colores no es un color primario, intenta de nuevo con rojo, amarillo o azul"
    elif ((color1=="azul" and color2=="rojo")or(color1=="rojo" and color2=="azul")):
        resultado="morado"
    elif ((color1=="azul" and color2=="amarillo")or(color1=="amarillo" and color2=="azul")):
        resultado = "verde"
    elif(color1==color2):
        resultado=color1
    else:
        resultado="naranja"    
    return resultado
#Definimos nuestra función principal
def main():
    color1=str(input("Elige un color primario(amarillo,rojo o azul)"))
    color2=str(input("Elige otro color primario(amarillo, rojo o azul)"))
    color1=color1.lower()
    color2=color2.lower()
    mezcla=mezclarColores(color1,color2)
    print("La combinación de %s y %s da %s"%(color1,color2,mezcla))
#Corremos el programa
main()    
#Fin
