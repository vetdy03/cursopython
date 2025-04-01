"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es."""
def changeEmail():
    email = input("enter your mail: ")
    print(email[:email.find('@')]+'@umss.edu.bo')
    #email[:email.find('@')]: Esto extrae la porción de la cadena email desde el principio hasta (pero sin incluir) el símbolo "@". Esta es la parte del nombre de usuario de la dirección de correo electrónico original.
    #+ '@ceu.es': Esto agrega la cadena "@ceu.es" al nombre de usuario extraído, creando la nueva dirección de correo electrónico con el dominio deseado.
if __name__ == '__main__':
    changeEmail()