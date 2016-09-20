#encoding: UTF-8
#Autor: Jess Perea
#Calcular descuento respecto al numero de productos comprados    

#empieza

def calcularDescuento(paquetesComprados):   #calcula el numero de descuentos
    if paquetesComprados >= 10 and paquetesComprados <=19:
        pagoTotal = ((paquetesComprados*1500) * 0.80)
    elif paquetesComprados >= 20 and paquetesComprados <=49:
        pagoTotal = ((paquetesComprados*1500) * 0.70) 
    elif paquetesComprados >= 50 and paquetesComprados <=99:
        pagoTotal = ((paquetesComprados*1500) * 0.60)
    elif paquetesComprados >= 100:
        pagoTotal = ((paquetesComprados*1500) * 0.50)
    elif paquetesComprados <0:
        pagoTotal = "Error. Teclea valor válido"
    return pagoTotal
    
    
    
def main():
    paquetesComprados = int(input("Teclea el numero de paquetes comprados"))
    pagoTotal = calcularDescuento(paquetesComprados)
    print(pagoTotal)

main()