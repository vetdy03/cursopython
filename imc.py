
def imc():
    print("Use el punto para ingresar decimales: Ej. 1.52[m] ")
    masa= float(input("Ingrese su masa: "))
    estatura= float(input("Ingrese su estatura en metros: "))
    imc= round((masa)/estatura**2,2)
    print("Su 'ICM' es:{} ".format(imc))
if __name__ == "__main__":
    imc()