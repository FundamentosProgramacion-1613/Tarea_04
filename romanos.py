
#encoding:UTF-8

#Autor:José Javier Rodríguez Mota
#Descripción: Imprime los números romanos del 1 al 10

#Inicio
#Definimos nuestra función para obtener un número romano 
def convertirRomano(numero):
    if (not(1<=numero<=10)):
        resultado ="Error el número no está dentro del parámetro"
    elif (9>numero > 5):
        variable=numero%5
        resultado="V"+"I"*variable
    elif (numero>=9):
        variable= 10-numero
        resultado = "I"*(variable)+"X"
    elif(numero==4):
        resultado="IV"    
    else:
        resultado="I"*numero    
    return resultado
#Definimos nuestra función principal
def main():
    numero=int(input("Dame un número entre 1 y 10"))
    resultado=convertirRomano(numero)
    print("El número que elegiste es %d y en romano se vuelve %s"%(numero,resultado))
main()    