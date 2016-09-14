#encoding: UTF-8
#Autor: Aldo Fuentes A01373294
#Calcular descuento de paquetes



#Calcula el precio, el descuento y el total
def calcularPrecio(num):

    precio = num * 1500
    
    if num < 10:
        porcentaje = 0
    elif num < 20:
        porcentaje = 20
    elif num < 50:
        porcentaje = 30
    elif num < 100:
        porcentaje = 40
    else:
        porcentaje = 50
        
    descuento = precio * porcentaje / 100
    
    total = precio - descuento
    
    return precio, descuento, total




def main():

    num = int(input("Teclea el numero de paquetes"))
    if num < 0:
        print("Error: numeros negativos no validos")
    else: 
        precio, descuento, total = calcularPrecio(num)
        print("Precio: $", "%.2f" % precio)
        print("Descuento: $", "%.2f" % descuento)
        print("Total: $", "%.2f" % total)

        

        




main()