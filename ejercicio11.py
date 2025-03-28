
def ejer11Interescompuesto():
    cantAahorrar= float(input("Ingrese la cant. total a ahorrar: "))
    interes= 0.04
    ahorrosPA= cantAahorrar*(1+interes)
    print("Balance tras el primer año es:{} ".format(round(ahorrosPA,2)))
    ahorrosSA= ahorrosPA*(1+interes)
    print("Balance de ahorroa segundo año: {}".format(round(ahorrosSA,3)))
    ahorrosTA= ahorrosSA*(1+interes)
    print("Balance de ahorroa tercer año: {}".format(round(ahorrosTA,1)))
    print("Gracias por ahorrar en nuestro banco, Tenga Feliz día")
    print("Thanks for saving at our bank, have a nice day")

if __name__ == '__main__':
    ejer11Interescompuesto()