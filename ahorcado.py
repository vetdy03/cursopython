import random


IMAGES = [ '''
          
           +---+
           |   |
               |
               |
               |
               |
         =========''','''

           +---+
           |   |
           O   |
               |
               |
               |
         =========''','''
         
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========''','''

           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========''','''

           +---+
           |   |
           O   |
          /|\  |
               |
               |
         =========''','''

           +---+
           |   |
           O   |
          /|\  |
           |   |
               |
         =========''','''

           +---+
           |   |
           O   |
          /|\  |
           |   |
          /    |
         =========''','''

           +---+
           |   |
           O   |
          /|\  |
           |   |
          / \  |
         =========''','''
''']

WORDS = [
    'sofa', 
    'mesa', 
    'alfombra', 'cojin', 'armario',
    'cortina', 'estante', 'reloj', 'cuadro', 'cama', 'comoda', 'television',
    'frigorifico', 'lavadora', 'horno', 'microondas', 'plancha', 'cafetera',
    'licuadora', 'ventilador', 'radiador', 'ducha', 'bañera', 'toalla',
    'escurridor', 'escoba', 'recogedor', 'fregona', 'cocina', 'estufa',
    'tetera', 'vajilla', 'plato', 'vaso', 'cuchara', 'tenedor', 'cuchillo',
    'sarten', 'cazuela', 'ollas', 'tapas', 'escurridor', 'batidora', 'manteles',
    'servilleta', 'almohada', 'edredon', 'colchon', 'percha', 'zapatero',
    'botiquin'
]











def random_word(): 
    idx= random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def show_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * ---')


def main():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        show_board(hidden_word, tries)
        current_letter = input('Ingres su letra: ')

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        
        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                show_board(hidden_word, tries)
                print('')
                print('Perdiste. La correcta fue {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []
        
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Felicidades. Ganaste. la palabra es {}'.format(word))
            break
    

if __name__ == '__main__':
    print('BIENVENIDOS A AHORCADOS')
    main()

