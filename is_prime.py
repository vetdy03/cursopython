# -*- coding: utf-8 -*-


def main():
    number = int(input('Escribe tu numero '))
    res = is_prime(number)
    if res == True:
        print( 'Si es primo')
    else:
        print( 'no es primo')
    

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
    return True

if __name__ == '__main__':
    main()   

