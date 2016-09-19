#encoding: UTF-8
#Autor: Diego Perez aka DiegoCodes
#Convertidor a Romanos
def convertidorRomanos(numero): #CONVIERTE EL VALOR A NUMEROS ROMANOS
    if (numero >=1 and numero <4):
        numRomano = ("I"*numero)
    if (numero ==4):
        numRomano = ("IV")
    if (numero >=5 and numero <9):
        numRomano = ("V"+"I"*(numero-5))
    if (numero ==9):
        numRomano = ("IX")
    if (numero ==10):
        numRomano = ("X")
    if (numero <=0 or numero > 10):
        numRomano = "HOLA, SOY UN MENSAJE DE ERROR"                        
    return numRomano
    
def main():
    numero = int(input("Escribe un numero 1-10:"))
    numRomano = convertidorRomanos(numero)
    print(numRomano)
main()    