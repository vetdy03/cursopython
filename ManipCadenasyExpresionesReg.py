#Descripción: Escribe un programa que encuentre todas las direcciones de correo electrónico en una cadena utilizando expresiones regulares.
#Objetivo: Profundizar en la manipulación de cadenas y el uso de expresiones regulares para el procesamiento de texto.

import re
texto = "Contacto: ana@example.com, pedro@mail.com"
correos = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
print(correos)
