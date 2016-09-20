#encoding:UTF-8
#Autor:Carlos E. Carbajal Nogués
#Descripción: Programa que suma colores

#Inicio
def sumarColores(color1,color2):#Función que sumará los colores
    c1 = color1.lower()
    c2 = color2.lower()
     
    if ((c1==("rojo") or c1==("azul")) and (c2==("rojo") or c2==("azul"))):
        res1 = ("El color que resulta es morado")
    elif ((c1==("rojo") or c1==("amarillo")) and (c2==("rojo") or c2==("amarillo"))):
        res1 = ("El color que resulta es naranja")
    elif ((c1==("azul") or c1==("amarillo")) and (c2==("azul") or c2==("amarillo"))):
        res1 = ("El color que resulta es verde")
    else: 
        res1=("Datos invalidos")
        
    return res1

def main(): #Función principal
    color1 = input("Introduce el color 1")
    color2 = input("Introduce el color 2")
    res=sumarColores(color1,color2)
    print (res)

main()