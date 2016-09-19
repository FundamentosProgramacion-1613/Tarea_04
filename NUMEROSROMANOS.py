# encoding: UTF-8
#Blanca Flor Cálderón Vázquez
# Lee el número del 1-10 e imprime su equvalente en romano.
#ahora entre 1-20

def transformarNumero(n):
    if n<4:
        romano= "I"*n
    elif n<6:
        romano=(5-n)*"I"+"V"
    elif n<9:
        romano= "V"+("I"*(n-5))
    else:
        romano=(10-n)*"I"+"X"
    return romano    

def main():
    numero=int(input("ingresa un número del 1-10 en letra"))
    if numero>0 and numero<11:
        numeroRomano=transformarNumero(numero)
        print(numeroRomano)
    

main()