#encoding: utf-8
#autor: Allan Sánchez Iparrazar
#Imprime un número romano

def escribirNumeroRomano(numeroNat) :
   
        if numeroNat == 1 :
            numeroRomano = "I"
        
        elif numeroNat  == 2 :
            numeroRomano = "II"
        
        elif numeroNat == 3 :
            numeroRomano = "III"
        
        elif numeroNat == 4 :
            numeroRomano = "IV"
        
        elif numeroNat == 5 :
            numeroRomano = "V"
        
        elif numeroNat == 6 : 
            numeroRomano = "VI"
        
        elif numeroNat == 7 :
            numeroRomano = "VII"
                    
        elif numeroNat == 8 :
            numeroRomano = "VIII"
        
        elif numeroNat == 9 :
            numeroRomano = "IX"
        
        elif numeroNat == 10 :
            numeroRomano = "X"
            
        return numeroRomano
        
        



def main():
    numeroNat = float(input("Ingrese un número del 1 al 10")) 
    
    
    if numeroNat<=10 and numeroNat>= 1 :
        numeroRomano = escribirNumeroRomano(numeroNat)
        print("El numero romano es:",numeroRomano)   
    
    else :
        print("No es un valor válido")
        
   

main()