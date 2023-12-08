import networkx as nx           #para generar grafos
import matplotlib.pyplot as plt #para graficar
import random

#---------------------------------- algoritmos --------------------------------------------------------------------
def traffic_colors(G):
    colors_dict = {}
    nodes_ordered = list(G.nodes())
    random.shuffle(nodes_ordered)
    
    for vertex in nodes_ordered:
        intersection_key = int(str(vertex).split('_')[0])  # Extract the intersection number from the node name

        # Check if a color has already been assigned within this intersection
        if intersection_key not in [int(i.split('_')[0]) for i in list(colors_dict.keys())]:
            colors_dict[vertex] = 1
        else:
            colors_dict[vertex] = 0

        print("Nodo:", vertex)
        print(intersection_key)
        print("Color:", colors_dict[vertex])
        print("Diccionario:", colors_dict)
        print("----------------------------------------------------------")

    return colors_dict


#------------------------- Main --------------------------------------------------------
#Grafo dirigido
G = nx.DiGraph()

#Cada row representa una interseccion, y los semaforos que tiene
nodes = ['1_1', '1_2', '1_3', '1_4', '1_5', '1_6',
         '2_1', '2_2', '2_3', '2_4', '2_5', '2_6',
         '3_1', '3_2', '3_3', '3_4', '3_5', '3_6',
         '4_1', '4_2', '4_3', '4_4', '4_5', '4_6']

edges = [('1_5', '1_3'), ('1_5', '1_4'), ('1_5', '1_2'),
         ('1_6', '1_1'), ('1_6', '1_3'), ('1_6', '1_4'),
         ('1_4', '2_3'), ('1_4', '2_4'), ('1_4', '2_2'),
         ('1_3', '3_1'), ('1_3', '3_3'), ('1_3', '3_4'),
         
         ('2_5', '2_2'), ('2_5', '2_1'), ('2_5', '2_3'),
         ('2_6', '2_1'), ('2_6', '2_3'), ('2_6', '2_4'),
         ('2_1', '1_2'), ('2_1', '1_1'), ('2_1', '1_3'),   
         ('2_3', '4_1'), ('2_3', '4_3'), ('2_3', '4_4'),
         
         ('3_5', '3_2'), ('3_5', '3_3'), ('3_5', '3_4'), 
         ('3_6', '3_1'), ('3_6', '3_2'), ('3_6', '3_4'), 
         ('3_2', '1_1'), ('3_2', '1_2'), ('3_2', '1_4'),
         ('3_4', '4_2'), ('3_4', '4_3'), ('3_4', '4_4'),
         
         ('4_5', '4_2'), ('4_5', '4_1'), ('4_5', '4_3'),
         ('4_6', '4_1'), ('4_6', '4_2'), ('4_6', '4_4'),
         ('4_1', '3_2'), ('4_1', '3_1'), ('4_1', '3_3'),
         ('4_2', '2_1'), ('4_2', '2_2'), ('4_2', '2_4')]

colors = ['red', 'green' ]

#agregar al grafo nodos y aristas
G.add_nodes_from(nodes)
G.add_edges_from(edges)

print("----------------------------------------------------------")
print("NODOS:", nodes)
print("----------------------------------------------------------")
print("ARISTAS:", edges)
print("----------------------------------------------------------")
print("NUMERO DE COLORES", len(colors))
print("----------------------------------------------------------")

# Dibujar el grafo
pos = nx.spring_layout(G)

my_colors = traffic_colors(G)

ordered_nodes = list(G.nodes())
node_colors = [colors[(my_colors[i])] for i in ordered_nodes]

nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_color="black", font_weight="bold", arrowsize=20)

# Mostrar el grafo
plt.show()