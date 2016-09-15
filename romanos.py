#encoding:UTF-8
#Autor: Lenin Silva Gutiérrez, A01373214
#Escribe en números romanos

from math import fabs #Para poder obtener el valor absoluto de números

def ponerTres(a): #Pone 'I' el número que veces que se le indique
    num=a*"I"
    return num #Regresa un string
    
def ponerCinco(b): 
    if (b-5)<0: #Condición para 4
        num=ponerTres(int(fabs(b-5)))+"V"
        return num
    num="V"+ponerTres(b-5)#Condición a partir del cinco. Pone 'V' y el número de 'I' restantes con la función anterior
    return num #Regresa un string
    
def ponerDiez(c):
    if (c-10)<0: #Condición para 9
        num=ponerTres(int(fabs(c-10)))+"X"
        return num
    num="X"+ponerTres(c-10)#Condición a partir del cinco. Pone 'X' y el número de 'I' restantes con ponerTres()
    return num #Regresa un string

def main():
    numero=int(input("Valor entre 1 y 13"))
    while numero<1 or numero>13: #Loop para que sólo sea posible poner valores dentro del rango
        print ("Escoja un valor entre 1 y 13")
        numero=int(input("Valor entre 1 y 13"))
    
    #Determina qué función se debe aplicar según el valor del número        
    if numero>=9: 
        numero_romano=ponerDiez(numero)
    elif numero>=4:
        numero_romano=ponerCinco(numero)
    else:
        numero_romano=ponerTres(numero)
    
    print ("El numero %d en romano es '%s'"%(numero, numero_romano)) #Imprime el número en romano
    
main()
        