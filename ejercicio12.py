
def     ejercicio12Marraqueta():
    barras = int(input("Introducir el numero de barras vendidas no frescas: "))
    precio= 3.49
    descuento= 0.6
    coste= barras*precio*(1-descuento)
    print("El coste de una barra es {} €".format(round(precio)) )
    print("El precio con descuento es {} %".format(descuento*100))
    print("El precio final a pagar es: {} € ".format(round(coste, 2)))
if __name__ == '__main__':
    ejercicio12Marraqueta()
    