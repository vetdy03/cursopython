#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
def pedirproductoscesta():
  cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print('\n'.join(cesta.split(',')))
if __name__ == '__main__':
  pedirproductoscesta()
