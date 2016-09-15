#encoding: UTF-8
#Autor: Jesús Perea
#Números Romanos        

#empieza

def convertirARomano(numero):   #Convierte el número dado en número romano
    if  numero >= 1 and numero <= 10:
        if numero >= 1 and numero <=2:
            if numero == 1:
                romano = "I" 
            else:
                romano = "II"
        if numero >= 3 and numero <= 4:
            if numero == 3:
                romano = "III"
            else:
                romano = "IV"
        if numero >= 5 and numero <=8:
            if numero == 5:
                romano = "V"
            else:
                romano = "VI" 
        if numero >= 7 and numero <= 8:
            if numero == 7:
                romano = "VII" 
            else:
                romano = "VII"
        if numero >= 9 and numero <=10:
            if numero == 9:
                romano = "IX"
            else:
                romano = "X"
        return romano
    else: 
        error = "Error. Teclea un número válido"
        return error
            
def main(): 
    numeroEntero = int(input("Teclea el número ente el 1 y 10 que quieras convertir en romano"))
    numeroRomano = convertirARomano(numeroEntero)
    print (numeroRomano)   


main()