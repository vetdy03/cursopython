#5. Trabajando con Archivos y Excepciones

#Descripción: Escribe un programa que lea un archivo y maneje situaciones donde el archivo no exista.
#Objetivo: Profundizar en el manejo de archivos y excepciones para construir aplicaciones más robustas.
try:
    with open('archivo_inexistente.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró.")
