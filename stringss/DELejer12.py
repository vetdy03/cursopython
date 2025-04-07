Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el siguiente formato:

<producto>: <unidades> unidades x <precio>€ = <total>€

donde <unidades> es el número de unidades con cinco dígitos, <precio> es el precio unitario con 6 dígitos enteros y 2 decimales y <total> es el coste total con 8 dígitos enteros y 2 decimales.
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))