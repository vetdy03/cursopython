# -*- coding: utf-8 -*-

def run():
    word = input('Ingresu su palabra: ')
    #res = palindromo(word)
    res1 = palin2(word)
    if res1 is True:
        print('Si es palidromo')
    else:
        print('No es palidromo')

def palindromo(word):
    letras = [] # platzi
    for letter in word:
        letras.insert(0, letter)
        #print(letter)

    nuebaLetras = ''.join(letras)
    print(nuebaLetras)
    if nuebaLetras == word:
        return True
    else:
        return False

def palin2(word):
    nuevaLetra = word[::-1]
    nuevaletra1 = ''.join(nuevaLetra)
    print(nuevaletra1)
    res= False
    if word == nuevaletra1:
        res = True
    return res
    
if __name__ == '__main__':
    run()