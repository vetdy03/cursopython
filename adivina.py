# -*- coding: utf-8 -*-
import random
def main():
    secret = random.randint(1, 100)
    print('A D I V I N A   E L   N U M E R O   S E C R E T O ')
    number = int(input('Ingrese su numero: '))
    attempt = 50
    
    
    
    
    

    while number != secret and attempt > 0:
        if number > secret:
            print('Tu numero secreto es menor, todavia tienes {} intentos'.format(attempt))
            number = int(input('Intenta otra vez: '))
            attempt -= 1
        elif number < secret:
            print('Tu numero secreto es mayor, todavia tienes {} intentos'.format(attempt)) 
            number = int(input('Intenta otra vez: '))
            attempt -= 1
    
    if number == secret:
        print('Felicidades abet adivinaste el numero secreto')
    else:
        print('Perdiste eres manco como yahir 17, el numero fue: ')
    print(secret)

if __name__ == '__main__':
    main()