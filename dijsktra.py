import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos con sus respectivas descripciones
G.add_node('A', label='Inicio')
G.add_node('B', label='Inicializar distancias a infinito')
G.add_node('C', label='Marcar todos los nodos como no visitados')
G.add_node('D', label='Seleccionar nodo con distancia más corta')
G.add_node('E', label='Calcular costo desde el nodo actual')
G.add_node('F', label='¿Nuevo costo menor que el registrado?')
G.add_node('G', label='Actualizar distancia')
G.add_node('H', label='Marcar nodo como visitado')
G.add_node('I', label='¿Todos los nodos visitados?')
G.add_node('J', label='Fin')

# Añadir aristas (transiciones entre pasos)
G.add_edges_from([
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('D', 'E'),
    ('E', 'F'),
    ('F', 'G'),
    ('F', 'H'),
    ('G', 'H'),
    ('H', 'I'),
    ('I', 'D'),
    ('I', 'J'),
])

# Definir las posiciones de los nodos (para visualización)
pos = {
    'A': (0, 0),
    'B': (0, -1),
    'C': (0, -2),
    'D': (0, -3),
    'E': (1, -3),
    'F': (1, -4),
    'G': (2, -4),
    'H': (2, -3),
    'I': (1, -2),
    'J': (2, -2),
}

# Dibujar el grafo
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)

# Etiquetas de los nodos
labels = nx.get_node_attributes(G, 'label')
label_pos = {k: (v[0], v[1] + 0.1) for k, v in pos.items()}  # Ajustamos la posición de las etiquetas
for node, label in labels.items():
    plt.text(label_pos[node][0], label_pos[node][1], label, horizontalalignment='center', fontsize=10)

# Mostrar el diagrama
plt.title("Diagrama de Flujo del Algoritmo de Dijkstra")
plt.show()
