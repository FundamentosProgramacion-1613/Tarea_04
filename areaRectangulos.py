# Oscar Zuñiga Lara, A01654827

import turtle


def main():
    ancho1 = float(input("Inserte ancho del rectangulo 1"))
    largo1 = float(input("Inserte largo del rectangulo 1"))
    ancho2 = float(input("Inserte ancho del rectangulo 2"))
    largo2 = float(input("Inserte largo del rectangulo 2"))
    area1 = areaRectangulo(ancho1, largo1)
    area2 = areaRectangulo(ancho2, largo2)
    areaM = areaMayor(area1, area2)
    print("El area mayor es : ", areaM)
    dibujartriangulo(ancho1,largo1,ancho2,largo2)

def areaRectangulo(ancho, largo):
    area = ancho * largo
    return area


def perimetroRectangulo(ancho, largo):
    perimetro = (ancho + largo) * 2
    return perimetro


def areaMayor(area1, area2):
    if area1 - area2 > 0:
        areaM = "Rectangulo 1"
    else:
        areaM = "Rectangulo 2"
    return areaM
def dibujartriangulo(largo1,ancho1,largo2,ancho2):
    turtle.pencolor("Red")
    turtle.fd(largo1)
    turtle.lt(90)
    turtle.fd(ancho1)
    turtle.lt(90)
    turtle.fd(largo1)
    turtle.lt(90)
    turtle.fd(ancho1)
    turtle.lt(90)
    turtle.pencolor("blue")
    turtle.fd(largo2)
    turtle.lt(90)
    turtle.fd(ancho2)
    turtle.lt(90)
    turtle.fd(largo2)
    turtle.lt(90)
    turtle.fd(ancho2)
    turtle.exitonclick()

main()
