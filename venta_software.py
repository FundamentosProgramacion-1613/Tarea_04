#encoding:UTF-8
#Autor: Lenin Silva Gutirrez, A01373214
#Calcula el total a pagar por un software

def calcularPago(paquetes,precio):

    if paquetes<=9:
        total=paquetes*precio
    elif paquetes>=10 and paquetes<=19:
        total=(paquetes*precio)*.8 #Aplica descuento de 20%
    elif paquetes>=20 and paquetes<=49:
        total=(paquetes*precio)*.7 #Aplica descuento de 30%
    elif paquetes>=50 and paquetes<=99:
        total=(paquetes*precio)*.6 #Aplica descuento de 40%
    else:
        total=(paquetes*precio)*.5 #Aplica desceutno de 50%
    return total #Regresa el costo con descuento como flotante
    
def main():
    paquetes=int(input("¿Cuántos paquetes serán comprados?"))
    if paquetes<0:
        print ("¡Valor negativo no aceptado!")
        return
    precio=1500.00
    total=calcularPago(paquetes, precio)
    
    print ("Por %d paquetes, son $%.2f"%(paquetes,total))
     
main()    