# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Números romanos del 1 al 10

#Función que convierte un número arábigo(a) a romano(b)
def convertir(a):
    b = ""
    if a <= 3:
        b = (a*"I")
    elif a==4:
        b = ("IV")
    elif a>4 and a<9:
        b = ("V"+((a-5)*"I"))
    else:
        b = (((10-a)*"I")+"X")
    return b
    
def main():
    numeroArabigo = int(input("Teclea un número del 1 al 10"))
    if numeroArabigo >= 1 and numeroArabigo<=10:
        numeroRomano = convertir(numeroArabigo)
        print(numeroRomano)
    else:
        print("El numero ingresado no está en el rango indicado")
main()