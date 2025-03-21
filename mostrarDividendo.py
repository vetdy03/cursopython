def mostrarDIvidendo():
    n= input("Ingrese su Numerador: ")
    m=  input("Ingrese su Denominador: ")
    print(n+" Entre "+m+" da un cociente de "+str(int(n)/int(m))+" y un residuo de "+str(int(n)%int(m)))
    #l doble / da un cociente entero saca lo entero mientras que / da con los decimales, pueden ser muchos decmales
if __name__ == '__main__':
    mostrarDIvidendo()