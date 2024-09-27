def binary_search(numbers):
    inicial =  0
    fin = len(numbers) -1
    vetdy03 = 0
    givenNumber = int(input('Ingrese su numero a buscar: '))  #28
    res = False
    while inicial <= fin: #y y
        idx = (inicial +fin) // 2 # 7 11 9
        if numbers[idx] == givenNumber: 
            res = True
            vetdy03 = vetdy03 +1 
            break
            
        elif numbers[idx] > givenNumber:
            fin = idx # 
            fin -= 1
        else:
            inicial = idx #7 9 
            inicial += 1 # 8 10 
    
    if res:
        print('Si se encontro el numero: ')
    else: 
        print('No se encontro el numero: ')
        
    return res
        

if __name__ == '__main__':
                 #1     #3           #7       9       #11
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51] #14
    res= binary_search(numbers)
    


