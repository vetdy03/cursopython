
#Introduce una cadena de texto: anitalavalatina
#La cadena invertida es: anitalavalatina
In [9]:
# Definir las vocales
vocales = "aeiouAEIOU"
# Solicitar una cadena de texto al usuario
cadena = input("Introduce una cadena de texto: ")
# Inicializar un contador para las vocales
contador_vocales = 0
# Usar un bucle para contar las vocales en la cadena
for letra in cadena:
if letra in vocales:
contador_vocales += 1
# Mostrar el número de vocales
print(f"El número de vocales en la cadena es: {contador_vocales}")
