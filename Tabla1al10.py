n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try:
    with open(nombre_fichero, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
