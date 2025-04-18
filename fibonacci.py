# Creación de un Generador Fibonacci

#Descripción: Implementa un generador que produzca los números de la secuencia Fibonacci.
#Objetivo: Comprender y utilizar generadores en Python para manejar secuencias grandes de manera eficiente.
Código de Ejemplo:
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci_gen()
for _ in range(10):
    print(next(fib))
