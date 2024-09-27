'''
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bccccccccccccccyb" y
'''

def first_not_repeating_char(char_sequence):
    seen_letters = {} ##diccionario vacio
    for idx, letter in enumerate(char_sequence):

if __name__ == '__main__':
    char_sequence = input('Ingresa tu secuencia')
    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten ')
    
    else:
        print('El primer char se repite: {}'.format(result))