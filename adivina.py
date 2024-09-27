# -*- coding: utf-8 -*-
import random
def main():
    secret = random.randint(1, 100)
    print('A D I V I N A   E L   N U M E R O   S E C R E T O ')
    number = int(input('Ingrese su numero: '))
    attempt = 10



    while number != secret and attempt > 0:
        if number > secret:
            print('Por encima del numero secreto todavia tienes {} intentos'.format(attempt))
            number = int(input('Intenta otra vez: '))
            attempt -= 1
        elif number < secret:
            print('Por debajo del numero secreto todavia tienes {} intentos'.format(attempt)) 
            number = int(input('Intenta otra vez: '))
            attempt -= 1
    
    if number == secret:
        print('Felicidades adivinaste el numero secreto')
    else:
        print('Perdiste eres manco como yahir 17, el numero fue: ')
    print(secret)

if __name__ == '__main__':
    main()