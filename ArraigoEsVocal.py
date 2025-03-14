def main():
    letra = input('INgresa tu letra plox: ')
    if letra =='a' or letra =='e' or letra =='i' or letra =='o' or letra =='u':
        print('La letra {} es una vocal '.format(letra) )
    else: 
        print('La letra {} no es una vocal '.format(letra) )
    
    
if __name__ == '__main__':
    main()