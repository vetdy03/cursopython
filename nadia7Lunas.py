def main():
    numero = int(input('Ingrese su numero: '))
    ultimo = numero % 100
    ultimoPrimero = ultimo // 10
    print('Nadia su penultimo número es: {}'.format(ultimoPrimero))

if __name__ == '__main__':
    main() 