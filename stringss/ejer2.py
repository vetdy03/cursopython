
def pedirNameYconvertir():
    tellMeName= input("Cual es su nombre: ")
    nameMayus= tellMeName.upper()
    nameMinus= tellMeName.lower()
    nameMix=  tellMeName.title()
    print("Holi:\n{}\n{}\n{}".format(nameMayus, nameMinus, nameMix))
if __name__ == '__main__':
    pedirNameYconvertir()