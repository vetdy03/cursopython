#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
def birthdate():
    age = input("Enter your date of birth: ")
    print('Día', age[:3])
    print('Mes', age[3:5])
    print('Año', age[5:])
    #23/10/1996
if __name__ == '__main__':
    birthdate()