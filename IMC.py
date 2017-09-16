# Oscar Zuñiga Lara  A01654827

def main():
    masa = float(input("Inserte su masa en kilogramos"))
    altura = float(input("Inserte su altura en metros"))
    iMC = imc(masa, altura)
    salud = eSalud(iMC)
    print("Tu IMC es de : ", iMC)
    print(salud)

def imc(masa, altura):
    imc = masa / (altura ** 2)
    return imc


def eSalud(iMC):
    if iMC < 18.5:
        salud = "Tu peso es bajo"
    elif iMC >= 18.5 and iMC <= 25:
        salud = "Tu peso es normal"
    elif iMC > 25:
        salud = "Tu peso es alto"
    return salud


main()
