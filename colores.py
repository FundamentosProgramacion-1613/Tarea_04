#encoding:UTF-8
#Autor: Lenin Silva Gutirrez, A01373214
#Combina los colores primarios

def combinarColor(color1, color2):
    if color1==color2:
        col_combinado=color1
    #Combinación de rojo    
    elif color1=="rojo":
        if color2=="amarillo":
            col_combinado="naranja"
        else:
            col_combinado="morado"
    #Combinación de azul        
    elif color1=="azul":
        if color2=="amarillo":
            col_combinado="verde"
        else:
            col_combinado="morado"  
    #Combinación de amarillo
    elif color1=="amarillo":
        if color2=="azul":
            col_combinado="verde"
        else:
            col_combinado="naranja"
            
    return col_combinado
    
def revisarValidez(color1,color2):
    primarios=["rojo","azul","amarillo"]
    if (color1 in primarios) and (color2 in primarios):
        return True
    return False
              
def main():
    print ("Escoger entre los siguientes colores: 'rojo', 'azul' o 'amarillo'")
    color1=str(input("Color 1")).lower()
    color2=str(input("Color 2")).lower()
    
    while not(revisarValidez(color1,color2)):
        print ()
        print ("Color no válido")
        print ("Escoger entre los siguientes colores: 'rojo', 'azul' o 'amarillo'")
        color1=str(input("Color 1")).lower()
        color2=str(input("Color 2")).lower()
        
    col_combinado=combinarColor(color1,color2)
    print ("El color resultante del %s y del %s es %s"%(color1,color2,col_combinado))
    
    
main()            