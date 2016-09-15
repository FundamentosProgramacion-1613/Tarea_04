#encoding: UTF-8
#Author: Allan Sánchez Iparrazar
#Descuentos

def calcularTotal(cantidad):
    
    if cantidad>=10 and cantidad<=19:
       
        precio = P*(1500*0.8)
        
    elif cantidad>=20 and cantidad<=49:
       
        precio = cantidad*(1500*0.7)
        
        
    elif cantidad>=50 and cantidad<=99:
      
        precio = cantidad*(1500*0.6)
   
   
    elif cantidad>100:
    
        precio = cantidad*(1500*0.5)
        
    return precio

def main():
    cantidad = int(input("Introduce el numero de paquetes"))
    
    if cantidad <= 0 :
        print("ERROR")
    else :
        cantidadConDescuento = calcularTotal(cantidad)
        print ("El Precio Total es $%.2f"%cantidadConDescuento)
main()