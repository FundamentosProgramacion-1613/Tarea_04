#Encoding UTF-8
#Oswaldo Morales Rodriguez
#Conociendo la cantida comprada dar el total

def calcularDescuento(cantidadPaquetes):
    if (cantidadPaquetes>=10) and (cantidadPaquetes<=19):
        descuento=(cantidadPaquetes*1500)*0.20
    elif (cantidadPaquetes>=20) and (cantidadPaquetes<=49):
        descuento=(cantidadPaquetes*1500)*0.30
    elif (cantidadPaquetes>=50) and (cantidadPaquetes<=99):
        descuento=(cantidadPaquetes*1500)*0.40
    elif (cantidadPaquetes>=100):
        descuento=(cantidadPaquetes*1500)*0.50
    elif(cantidadPaquetes<0):
        descuento=("Error")
    else:
        descuento=0
    return descuento

def main():
    cantidadPaquetes=int(input("Paquetes comprados"))
    descontado=calcularDescuento(cantidadPaquetes)
    subtotal=cantidadPaquetes*1500
    total=subtotal-descontado
    print("El subtotal es",subtotal)
    print("El descuento es", descontado)
    print("El total es",total)
main()
    