def ejerc9():
    cantInvertir= float(input("Ingrese la cantidad a invertir: "))
    interes= float(input("Ingrese el interes anual: "))
    anios= int(input("Ingrese la cantidad de años que quiere invertir: "))
    res= round( cantInvertir*((interes/100)+1)**anios,2)
    print("La ganancia total es: {}".format(res))

if __name__ == '__main__':
    ejerc9()