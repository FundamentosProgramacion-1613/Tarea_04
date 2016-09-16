#encoding:UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descripción: Programa que convierte los decimales a romanos

#Incio

def calcularRomano(num): #Declaramos la función que nos dirá el número romano
    if (num<0 or num>10):
        res1 = ("Dato incorrecto")
    elif (num>=1 and num<=3):
        res1 = ("I" * num)
    elif (num==4):
        res1 = ("IV")
    elif (num>=5 and num<=8):
        res1 = ("V" + ("I" * (num-5)))
    elif (num==9):
        res1 = ("IX")
    elif (num==10):
        res1 = ("X")
    return res1
        

def main(): #Declaramos nuestra función principal
    numero= int(input("Introduce tu número"))
    res=calcularRomano(numero)
    print (res)
main()
#Fin