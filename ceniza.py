# -*- coding: utf-8 -*-

def main():
    number1 = int(input('Escriba el primer numero '))
    number2 = int(input('Escriba el segundo numero '))
    number3 = int(input('Escriba el tercer numero '))
    #9 19  9  8
    #2 5  8 10
    #7 10 18 2
    if number1 > number2 :
        if number1 > number3 :
            print('Ceniza es {}'.format(number1))
        else:
            print('Ceniza es {}'.format(number3))
    elif number2 > number3:
        print('Ceniza es {}'.format(number2))
   






if __name__ == '__main__':
    main()



