#4. Decoradores en Python

#Descripción: Escribe un decorador que mida el tiempo de ejecución de una función.
#Objetivo: Aprender a extender y modificar el comportamiento de las funciones en Python.
#Código de Ejemplo:
import time
def temporizador(func):
    def envoltura():
        inicio = time.time()
        func()
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio} segundos")
    return envoltura
@temporizador
def funcion_demorada():
    time.sleep(2)
funcion_demorada()