def main():
    number = int(input('Ingrese su numero para convertir a factorial \n'))
    sumador = 1
    numberCopy= number
    while number > 1:
        sumador *= number# * sumador
        number = number - 1

    print('La factorial de {} es {} '.format(numberCopy, sumador))


if __name__ == '__main__':
    main()