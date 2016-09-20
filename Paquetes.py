#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran
#Problema 4

def calcularPrecio(a):
    if a>=1 and a<9:
        z= a*1500
        return z
    else:
        if a>=10 and a<=19:
            z= float(a*1500)*.80
            return z
        else:
            if a>=20 and a<=49:
                z= float(a*1500)*.70
                return z
            else:
                if a>=50 and a<=99:
                    z= float(a*1500)*.60
                    return z
                else:
                    if a>=100:
                        z= float(a*1500)*.50
                        return z
                    else:
                        print ("error")
                        
def main():
    a= int(input("¿Cuantos paquetes vas a querer?"))
    b= calcularPrecio(a)
    print ("El total a pagar de",a,"paquetes es de:$",b,"pesos")
                        
main()