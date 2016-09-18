#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran
#Problema 3

def calcularColores(a,b):
    if a=="rojo" and b=="azul" or b=="rojo" and a=="azul":
        return "Morado"
    else:
        if a=="rojo" and b=="amarillo" or b=="rojo" and a=="amarillo":
            return "Naranja"
        else:
            if a=="azul" and b=="amarillo" or b=="azul" and a=="amarillo":
                return "Verde"
            else:
                print ("error")
            
def main():
    a= raw_input("¿Que color quieres?")
    a1= a.upper()
    a2= a.lower()
    b= raw_input("¿Que otro color quieres?")
    b1= b.upper()
    b2= b.lower()
    print ("El color entre", a, "y", b," forma el color:",calcularColores(a,b))
    
main()