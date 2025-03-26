
def phoneNumbers():
    number = input("Ingrese su numero con xodigo de pais\n número y prefijo: ")
    print("Su numero de telefono es: {} ".format(number[4:13]))
if __name__ ==  '__main__':
    phoneNumbers()