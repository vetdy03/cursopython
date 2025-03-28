
def phoneNumbers():
    number = input("Ingrese su numero con xodigo de pais\n número y prefijo: ")
    number2 = input("Ingrese su segundo numero de telefono: ")
    print("Su numero de telefono es: {} ".format(number[4:13]))
    print("Su segundo numero purito es: {}".format(number2[4:-3])) 
    #+54-769589387-56
    #0123456789012345
if __name__ ==  '__main__':
    phoneNumbers()