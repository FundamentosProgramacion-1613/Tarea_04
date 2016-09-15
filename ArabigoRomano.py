#Encoding UTF-8
#Oswaldo Morales Rodriguez
#Conociendo un numero imprimir su arabigo



def remplazarSistema(numero):
    if (numero<=3) and (numero>0):
        romano=(numero*"I")
    elif(numero==4):
        romano=("IV")
    elif(numero==5):
        romano=("V")
    elif(numero>5) and (numero<9):
        numeroTrabajo=numero-5
        romano=("V",numeroTrabajo*"I")
    elif(numero==9):
        romano=("XIX")
    elif(numero==10):
        romano=("X")
    else:
        romano=("un error con este programa")
    return romano
    
def main():
    numero=int(input("Numero")) 
    numeroRomano=remplazarSistema(numero)
    print("El numero romano de",numero,"es",numeroRomano)
main()