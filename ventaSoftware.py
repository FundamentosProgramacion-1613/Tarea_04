#Oscar Zuñiga Lara  A01654827

def main():
    paquetes = int(input("Inserte paquetes"))
    descuento = descuentos(paquetes)
    total = paquetes * 1500 - paquetes * descuento
    print("Usted comprará : ", paquetes)
    print("Usted tendrá un descuento de : " , descuento)
    print("Y pagará :",  total)

def descuentos(paquetes):
    if paquetes < 0:
        descuent = "Error"
    elif paquetes >= 0 and paquetes < 10:
        descuento = 0
    elif paquetes > 10 and paquetes < 20:
        descuent = 20
    elif paquetes > 20 and paquetes < 50:
        descuent = 30
    elif paquetes >= 50 and paquetes < 100:
        descuent = 40
    elif paquetes > 100:
        descuent = 50
    return descuent

main()