"""Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""
def priceOfProduct():
    precio = input("enter your price: ")
    print(precio[:precio.find('.')], 'euros y ', precio[precio.find('.')+1:], 'centimos. ')
    #selecciona una porción de la cadena precio desde la posición después del punto decimal hasta el final, obteniendo así los céntimos.
if __name__ == '__main__':
        priceOfProduct()