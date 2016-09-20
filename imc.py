#encoding: UTF-8
# Autor: Marlon Brandon Velasco Pinello, A01379404
# Descripcion: IMC Tarea 4

#clcular imc
def calcularIMC(masa,estatura):
    imc=masa/(estatura*estatura)
    return imc

    #determinar salud    
def calcularSalud(imc):
    if imc < 18.5:
        salud="bajo de peso"
    elif imc>=18.5 and imc <=25:
        salud="peso normal"
    else:
        salud="Sobre peso"
    return salud

#funcion principal main    
def main():
    masa=float(input("ingresa tu masa en kg"))
    estatura=float(input("ingresa tu estatura en metros"))
    if masa < 0 or estatura < 0:
        print("Error: valores no aceptados")
    elif masa == 0 or estatura == 0:
        print("Error: valores no aceptados")
    else:
        imc=calcularIMC(masa,estatura)
        salud=calcularSalud(imc)
        print("Tus resultados son IMC:",imc)
        print(salud)
        
main()
        