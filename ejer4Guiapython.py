#Ejercicio 4: Verificar si un número es positivo, negativo o cero
#Objetivo: Introducir las declaraciones condicionales (if, elif, else).
In [5]:
# Solicitar un número al usuario
num = int(input("Introduce un número: "))
# Verificamos si el número es positivo, negativo o cero
if num > 0:
print("El número es positivo")
elif num < 0:
print("El número es negativo")
else:
print("El número es 0")
