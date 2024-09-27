def main():
    letter = input('Ingrese su texto: ')
    counterLetter = 0
    searchedletter = input('Ingrese su palabra a buscar: ') #01234 tam 12345
    countersearched = 0
    answer = ''
    while len(letter) > counterLetter and countersearched < len(searchedletter):
        if letter[counterLetter ] == searchedletter[countersearched]:
            countersearched = countersearched + 1
        counterLetter = counterLetter + 1

        if countersearched == len(searchedletter):
            answer = 'La palabra que esta buscando existe'
        else:
            answer = 'La palabra buscada on existe: F chokito'
    print(answer)
    print()

if __name__ == '__main__':
    main()
