#Encoding UTF-8
#Oswaldo Morales Rodriguez
#Conociendo los colores imprimir el resultante

def definirColor(primerColor,segundoColor):
    if(primerColor=="azul") and (segundoColor=="rojo"):
        resultado=("Morado")
    elif(primerColor=="azul") and (segundoColor=="amarillo"):
        resultado=("Verde")
    elif(primerColor=="rojo") and (segundoColor=="amarillo"):
        resultado=("naranja")
    else:
        resultado=("Color inexistente")
    return resultado
        






def main():
    primerColor=str(input("Color elgido entre azul,amrillo o rojo"))
    segundoColor=str(input("Color elgido entre azul,amrillo o rojo"))
    primerColor=primerColor.lower()
    segundoColor=segundoColor.lower()
    colorFinal=definirColor(primerColor,segundoColor)
    print("El resultado de",primerColor, "y",segundoColor, "es",colorFinal)
main()
    