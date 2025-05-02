#Ejercicio 6: Calcular el factorial de un número usando un bucle while
#Objetivo: Introducir bucles while y control básico de bucles.
In [7]:
# Solicitar el número al usuario
num = int(input("Introduce un número: "))
# Inicializar variables
factorial = 1
i = 1
# Usar un bucle while para calcular el factorial
while i <= num:
factorial *= i
i += 1
# Mostrar el resultado
print(f"El factorial de {num} es {factorial}")
