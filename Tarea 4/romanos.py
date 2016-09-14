#encoding: UTF-8
#Autor: Aldo Fuentes
#Convertir a numeros romanos



#Convierte el valor de num a romano

def convertirRomano(num):
    
    if num > 0 and num < 4:
        romano = ("I"*num)
    elif num < 9:
        romano = ("V"+(num-5)*"I")
        if num == 4:
            romano = "IV"
    elif num < 11:
        romano = (abs(num-10)*"I"+"X")
    else:
        romano = "Error: No es un numero dentro del rango 1-10"
            
    return romano


def main():
    
    num = int(input("Teclea un numero del 1 al 10"))
    
    romano = convertirRomano(num)
    
    print(romano)





main()