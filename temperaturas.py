# -*- coding: utf-8 -*-

def tempe(temps):
    suma = 0
    for tempes in temps:
        suma += tempes
    
    return suma / len(temps)
   

if __name__ == '__main__':
    temps = [21,22,24,25,26,23,25]
    prmedio= tempe(temps)

    print('El prmedio es {}'.format(prmedio))