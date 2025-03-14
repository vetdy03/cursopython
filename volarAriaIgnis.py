def main():
    numero = int(input('Ingrese su numero a volar: '))
    if (numero//10 == numero%10):
        print('Su numero {} puede volar'.format(numero))
    else:
        print('Su numero {} no puede volar'.format(numero)) 
   
"""def main():
    numero = 23
    div = 23/10
    print('la div es {}'.format(div))"""

if __name__ == '__main__':
    main()