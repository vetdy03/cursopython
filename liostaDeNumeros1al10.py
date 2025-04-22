# Solicitar el número final de la lista
num = int(input("Introduce el número final de la lista: "))
# Crear una lista desde 1 hasta el número ingresado
lista = list(range(1, num + 1))
# Calcular la suma de los elementos de la lista
resultado = sum(lista)
# Mostrar el resultado
print(f"La suma de la lista hasta {num} es {resultado}")
