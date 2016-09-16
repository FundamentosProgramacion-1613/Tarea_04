#encoding = UTF-8
#Adrian E. Tellez Lopez
# Sacar el total a pagar

def main():
    paquetes = int(input("Paquetes comprados"))
    precios = calcularPrecio(paquetes)
    print("Si compras", paquetes,"paquetes, tienes un descuento del", descuentos,"%")
    print("Total a pagar:", precios)
    

def calcularPrecio (paquetes):
    global descuentos
    if paquetes < 0:
        return ("Pon un numero positivo")
    else:
        if paquetes < 10:
            descuentos = 0
            precio = paquetes * 1500
            return precio
        if paquetes >= 10 and paquetes <= 19:
            descuentos = 20
            precio = paquetes * 1500
            descuento = precio * .20
            precio = precio - descuento
            return precio 
        if paquetes >= 20 and paquetes <= 49:
            descuentos = 30
            precio = paquetes * 1500
            descuento = precio * .30
            precio = precio - descuento
            return precio 
        if paquetes >= 50 and paquetes <= 99:
            descuentos = 40
            precio = paquetes * 1500
            descuento = precio * .40
            precio = precio - descuento
            return precio 
        else:
            descuentos = 50
            precio = paquetes * 1500
            descuento = precio * .50
            precio = precio - descuento
            return precio 

main()