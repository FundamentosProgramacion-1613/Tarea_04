#encoding: UTF-8
#Karla Valeria Alcntara Duarte A01373164
#Calcular descuento de compra

def calcularDescuento(numeroPaquetes):

    if numeroPaquetes<10:
        descuento = "No hay descuento"
        pago = (1500*numeroPaquetes)
        
    elif numeroPaquetes>=10 and numeroPaquetes<=19:
        descuento = (1500*numeroPaquetes)*(0.20)
        pago = (1500*numeroPaquetes)-descuento
        
    elif numeroPaquetes>=20 and numeroPaquetes<=49:
        descuento = (1500*numeroPaquetes)*(0.30)
        pago = (1500*numeroPaquetes)-descuento
          
    elif numeroPaquetes>=50 and numeroPaquetes<=99:
        descuento = (1500*numeroPaquetes)*(0.40)
        pago = (1500*numeroPaquetes)-descuento
        
    elif numeroPaquetes>=100:
        descuento = (1500*numeroPaquetes)*(0.50)
        pago = (1500*numeroPaquetes)-descuento
        
    return pago 
    
    
def main():

    numeroPaquetes = int(input("¿Cuantos paquetes son?"))
    
    if numeroPaquetes>=0:
        precio = calcularDescuento(numeroPaquetes)
        print("El precio es",precio)
    
    else:
        print("Valor invalido")
        

main()
