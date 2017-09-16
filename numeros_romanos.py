#Oscar Zuñiga Lara A01654827

def main():
    numeroU = int(input("Inserte Numero"))
    numeroR = romanoN(numeroU)
    print("Su numero romano es : " , numeroR)

def romanoN(numeroU):
    user = numeroU
    if user > 10 or user < 1:
        romano = "No puedo calcular numeros romanos menores a 1 o mayores a 10"
    elif user >= 5 and user < 9:
        romano = "V" + (user % 5 * "I")
    elif user < 4 and user >=1:
        romano = user % 5 * "I"
    elif user == 4:
        romano = "IV"
    elif user == 9:
        romano = "IX"
    elif user == 10:
        romano = "X"
    return romano

main()