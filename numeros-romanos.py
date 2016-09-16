#encoding: UTF-8
#Karla Valeria Alcántara Duarte A01373164
#Convertir numeros decimales a romanos.

def convertirNumero(numeroUsuario):
    if numeroUsuario>=1 and numeroUsuario<4:
        romano = ("I"*numeroUsuario)
    elif numeroUsuario==4:
        romano = "IV"
    elif numeroUsuario==5:
        romano = "V"
    elif numeroUsuario>=6 and numeroUsuario<9:
        romano = ("V"+(numeroUsuario-5)*("I"))
    elif numeroUsuario==9:
        romano = "IX"
    elif numeroUsuario==10:
        romano = "X"
    else:
        romano = "numero fuera de rango"
    return romano
    
def main():
    numeroUsuario = int(input("¿Que numero quieres convertir?"))
    numeroRomano = convertirNumero(numeroUsuario)
    print("El numero",numeroUsuario,"es",numeroRomano)


main()