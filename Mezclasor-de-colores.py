#encoding: UTF-8
#Autor: Jess Perea
#Hacer un programa que mezcle colores       

#empieza

def combinarColores(primerColor, segundoColor): #Esta funcion combina los colores dados
        if primerColor == "rojo":
            if segundoColor == "amarillo" :
                combinacion = "naranja"
            elif segundoColor == "azul":
                combinacion = "morado"  
            elif segundoColor == "rojo":
                combinacion = "rojo"      
        elif primerColor == "azul":
            if segundoColor == "amarillo":
                combinacion = "verde"
            elif segundoColor == "rojo":   
                combinacion = "morado"
            elif segundoColor =="azul":
                combinacion = "azul"
        elif primerColor == "amarillo":
            if segundoColor == "rojo":
                combinacion = "naranja"
            elif segundoColor == "azul":
                combinacion = "verde"
            elif segundoColor == "amarillo":
                combinacion = "amarillo"
        elif primerColor != "rojo":
            combinacion = "Error. Teclea color valido"
        elif primerColor != "azul":
            combinacion = "Error. Teclea color valido"
        elif primerColor != "amarillo":
            combinacion = "Error. Teclea color valido"
        elif segundoColor != "rojo" :
            combinacion = "Error. Teclea un color valido"
        elif segundoColor != "azul" :
            combinacion = "Error. Teclea un color valido"
        elif segundoColor != "amarillo" :
            combinacion = "Error. Teclea un color valido"
                
        return combinacion
    
def main ():
    primerColor = str(input("Teclea un color primario (rojo,azul,amarillo)"))
    primerColorMayusc = primerColor.upper()
    primerColorMinusc = primerColor.lower()
    
    segundoColor = str(input("Teclea un color primario (ojo,azul,amarillo)"))
    segundoColorMayusc = segundoColor.upper()
    segundoColorMinusc = segundoColor.lower()
    
    combinacion = combinarColores(primerColorMinusc, segundoColorMinusc)
    COMBINACION = combinarColores(primerColorMayusc, segundoColorMayusc)
    print ("La combinacion es:",combinacion)
    
main()
