# encoding: UTF-8
#Blanca Flor Cldern Vzquez
#Venta  de  software

    
def descontar(numerodecompras,preciounitario):
    precio=(numerodecompras*preciounitario)
    if numerodecompras<=0:
        pagas="ingresa un numero positivo diferente de cero"
    elif numerodecompras>0 and numerodecompras<10:
        pagas= precio
    elif numerodecompras>9 and numerodecompras<20:
        pagas=precio-((20*precio)/100)
    elif numerodecompras>19 and numerodecompras<50:
        pagas=precio-((30*precio)/100)
    elif numerodecompras>49 and numerodecompras<100:
        pagas=precio-((40*precio)/100)
    elif numerodecompras>99:
        pagas=precio-((50*precio)/100)
    return pagas
  
def main():
    precio=1500.00
    numeroDePiezasCompradas=int(input("introduce el número de piezas que compraste"))
    pagar=descontar(numeroDePiezasCompradas,precio)
    print(pagar)

  
    
main()  