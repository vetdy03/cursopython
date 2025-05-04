#Ejercicio 10: Encontrar el número máximo en una lista sin usar funciones incorporadas
#Objetivo: Enseñar cómo iterar a través de una lista y comparar valores.
In [16]:
# Definir la lista de números
lista = [5, 6, 9, 1, 15, 19, 1, 2]
# Inicializar el valor máximo como el primer número de la lista
max_num = lista[0]
# Iterar a través de la lista para encontrar el número máximo
for num in lista:
if num > max_num:
max_num = num
# Mostrar el número máximo
print(max_num)
