import networkx as nx           #para generar grafos
import matplotlib.pyplot as plt #para graficar

#------------------------- Main --------------------------------------------------------
#Grafo dirigido
G = nx.DiGraph()

#Cada row representa una interseccion, y los semaforos que tiene
nodes = [1_1, 1_2, 1_3, 1_4, 1_5, 1_6,
         2_1, 2_2, 2_3, 2_4, 2_5, 2_6,
         3_1, 3_2, 3_3, 3_4, 3_5, 3_6,
         4_1, 4_2, 4_3, 4_4, 4_5, 4_6]

edges = [ (1_5, 1_3), (1_5, 1_4), (1_5, 1_2),
          (1_6, 1_1), (1_6, 1_3), (1_6, 1_4),
          (1_4, 2_3), (1_4, 2_4), (1_4, 2_2),
          (1_3, 3_1), (1_3, 3_3), (1_3, 3_4),
          
          (2_5, 2_2), (2_5, 2_1), (2_5, 2_3),
          (2_6, 2_1), (2_6, 2_3), (2_6, 2_4),
          (2_1, 1_2), (2_1, 1_1), (2_1, 1_3),   
          (2_3, 4_1), (2_3, 4_3), (2_3, 4_4),
          
          (3_5, 3_2), (3_5, 3_3), (3_5, 3_4), 
          (3_6, 3_1), (3_6, 3_2), (3_6, 3_4), 
          (3_2, 1_1), (3_2, 1_2), (3_2, 1_4),
          (3_4, 4_2), (3_4, 4_3), (3_4, 4_4),
          
          (4_5, 4_2), (4_5, 4_1), (4_5, 4_3),
          (4_6, 4_1), (4_6, 4_2), (4_6, 4_4),
          (4_1, 3_2), (4_1, 3_1), (4_1, 3_3),
          (4_2, 2_1), (4_2, 2_2), (4_2, 2_4) ]

colors = ['red', 'green']

G.add_nodes_from(nodes)
# Agregar todos los arcos en una sola línea
G.add_edges_from(edges)

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)

# Mostrar el grafo
plt.show()