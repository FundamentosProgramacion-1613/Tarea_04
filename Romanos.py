#encoding: UTF-8
#author: Edgar Eduardo Alvarado Durán
#Problema 1

def calcularRango(a):
    if a>=1 and a<=10:
        return a
    else:
        print ("error")
    
def calcularRomanos(a):
    if a==1:
        return ("I")
    else:
        if a==2:
            return (2*"I")
        else:
            if a==3:
                return (3*"I")
            else:
                if a==4:
                    return ("IV")
                else:
                    if a==5:
                        return ("V")
                    else:
                        if a==6:
                            return ("VI")
                        else:
                            if a==7:
                                return ("VII")
                            else: 
                                if a==8:
                                    return ("VI")
                                else:
                                    if a==9:
                                        return ("IX")
                                    else:
                                        if a==10:
                                            return ("X")
                                        else:
                                            print ("error")
                
def main():
    a= int(input("Dame un valor"))
    print ("El numero entero es:",a)
    b= calcularRomanos(a)
    print ("El numero romano es: ",b)

main()