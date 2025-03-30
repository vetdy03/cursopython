def replacetovocal():
    phrase= input("Enter your phrase: ")
    vocal = input("Enter your vocal: ")
    print("Your phrase inverted is: {}".format(phrase.replace(vocal, vocal.upper())))
    
if __name__ == '__main__':
    replacetovocal()