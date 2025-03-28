
def contarLetrasDelNombre():
    name= input("Escriba su nombre: ")
    contarLetras= len(name)
    print("Su nombre: {} tiene {} letras".format(name.upper(), contarLetras))

if __name__ == '__main__':
    contarLetrasDelNombre()