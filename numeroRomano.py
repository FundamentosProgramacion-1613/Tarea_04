#encoding: UTF-8
# Autor: Marlon Brandon Velasco Pinello, A01379404
# Descripcion: Números romanos Tarea 4

#Funcion para convertir de numero normal a romano
def convertirNNormalNRomano(numeroNormal):
    if(numeroNormal<=3):
        numeroRomano=(numeroNormal*"I")
    elif(numeroNormal>= 4 and numeroNormal<=8):
        numeroRomano=(((4-numeroNormal)+1)*"I"+1*"V"+(numeroNormal-5)*"I")
    else:
        numeroRomano=(((9-numeroNormal)+1)*"I"+1*"X")
    return numeroRomano

#funcion principal main
def main():
    numeroNormal=int(input("Ingresa un numero del 1 al 10"))
    if (numeroNormal >=1 and numeroNormal<=10):
        numeroRomano=convertirNNormalNRomano(numeroNormal)
        print("El numero que ingresaste es %d traducido a romano es: %s"%(numeroNormal,numeroRomano))
    else:
        print("Error:numero invalido")
        
main()