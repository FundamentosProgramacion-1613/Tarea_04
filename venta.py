
#encoding:UTF-8

#Autor:José Javier Rodríguez Mota
#Descripción: Imprime el precio de una venta

#Inicio
#Definimos nuestra función para obtener el descuento 
def calcularDescuento(cantidad):
    if(cantidad<10):
        resultado=0
    elif(10<=cantidad<20):
        resultado=20
    elif(20<=cantidad<50):
        resultado=30
    elif(50<=cantidad<100):
        resultado=40
    else:
        resultado=50                        
    return resultado
#Definimos nuestra función para obtener el precio
def calcularPrecio(cantidad):
    precio=1500*cantidad
    return precio
def calcularTotal(descuento,precio):
    total=precio*((100-descuento)/100)
    return total        
#Definimos nuestra función principal
def main():
    cantidad=int(input("¿Cuántas piezas comprarás?"))
    if (cantidad<0):
        print("ERROR LA CANTIDAD NO ES VÁLIDA")
    else:  
        descuento=calcularDescuento(cantidad)
        precio=calcularPrecio(cantidad)
        total=calcularTotal(descuento,precio)
        print("""Cotización de %d piezas:
        Precio:$%.2f
        Descuento: -%d porciento
        Total:$%.2f
        """%(cantidad,precio,descuento,total))  
#Corremos el programa
main()    
#Fin   
