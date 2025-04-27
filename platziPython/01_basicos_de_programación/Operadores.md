# Operadores de asignación combinados en Python

Estos operadores permiten modificar y asignar una variable en un solo paso:

| Operador | Significado | Ejemplo | Resultado |
|:---|:---|:---|:---|
| `+` | Sumar | `2+2= ` | `4` |
| `-` | Restar | `4-2=` | `2`|
| `*` | Multiplicar | `4*2` | `8`|
| `/` | División | `4/2` | `2.0`|
| `//` | División Entera | `4//2` | `2`|
| `%` | Módulo | `7%2` | `1`|
| `**` | Potencia | `4**2` | `16`|
| `>` | Mayor que | `4>2` | `True`|
| `<` | Menor que | `4<2` | `Flase`|
| `==` | Igual que | `4==2` | `False`|
| `+=` | Sumar y asignar | `x += 3` | `x = x + 3` |
| `-=` | Restar y asignar | `x -= 2` | `x = x - 2` |
| `/=` | Dividir y asignar | `x /= 4` | `x = x / 4` |
| `//=` | División entera y asignar | `x //= 2` | `x = x // 2` |
| `%=` | Módulo y asignar (residuo) | `x %= 5` | `x = x % 5` |
| `*=` | Multiplicar y asignar | `x *= 6` | `x = x * 6` |
| `**=` | Potencia y asignar | `x **= 2` | `x = x ** 2` |

## Ejemplo completo

```python
x = 10
x += 5    # x ahora es 15
x -= 3    # x ahora es 12
x *= 2    # x ahora es 24
x /= 4    # x ahora es 6.0
x **= 2   # x ahora es 36.0
x %= 7    # x ahora es 1.0
x //= 1   # x ahora sigue siendo 1.0
```

# Variables y expresiones
● Una expresión (expression) es una combinación de valores, variables y
operadores
○ El intérprete evalúa expresiones
○ Ej. 2 + 2
● Un enunciado (statement) es una unidad de código que tiene un efecto
○ Ej. age = 20

● Orden de operaciones:
○ Parentesis
■ Exponente
● Multiplicación
● División
○ Adición
○ Substracción
● PEMDAS
