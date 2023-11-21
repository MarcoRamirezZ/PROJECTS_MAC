import networkx as nx           #para generar grafos
import matplotlib.pyplot as plt #para graficar
import sys                      #para terminar el programa si el coloreado no es posible

def alg_voraz(graph):
    #diccionario vacio donde se van a ir agregando los colores
    colors = {}
    
    #Para cada nodo en el grafo
    for vertex in graph.nodes():
        #crea un conjunto neighbor_colors y para el nodo actual, agrega en el conjunto los vecinos de ese vertice que ya hayan sido coloreados y con que color
        neighbor_colors = set(colors[neighbor] for neighbor in graph.neighbors(vertex) if neighbor in colors)
        #Siempre empieza con el primer color y ve aumentando de numero de color si el color actual ya esta en el conjunto neighbor_colors
        color = 1
        while color in neighbor_colors:
            color += 1
            
        #Si el color necesitado sobrepasa el numero de colores disponibles, manda un mensaje y termina de correr el script ya que el coloreado no es posible
        if color > len(colores):
            print("Coloreado no posible, terminando el programa")
            print("Vertice del conflicto: ", vertex)
            print("Colores colindantes: ", neighbor_colors)
            print("Colores totales: ", len(colores))
            print("Coloreado hasta el error: ", colors)
            sys.exit()
            
        #Agrega el color del vertice a su instancia en el diccionario
        colors[vertex] = color
        
    return colors

#Grafo no dirigido
grafo = nx.Graph()

#DEBUG input ---------------------
#Definir nodos, aristas y colores
#nodos = [ "AGS",  "BC", "BCS",  "CAMP", "COAH", "COL", "CHIS", "CHIH", "CDMX", "DGO", "GTO", "GRO", "HGO", "JAL", "MEX", "MICH", "MOR", "NAY", "NL", "OAX", "PUE", "QRO", "QROO", "SLP", "SIN", "SON", "TAB", "TAMPS", "TLAX", "VER", "YUC",  "ZAC"]
#aristas = [ ("AGS", "ZAC"), ("AGS", "JAL"),
#                ("BC", "BCS"),  ("BC", "SON"),
#                ("CAMP", "TAB"), ("CAMP", "YUC"), ("CAMP", "QROO"),
#                ("COAH", "CHIH"), ("COAH", "DGO"), ("COAH", "ZAC"), ("COAH", "NL"),
#                ("COL", "JAL"), ("COL", "MICH"), 
#                ("CHIS", "TAB"), ("CHIS", "VER"), ("CHIS", "OAX"),
#                ("CHIH", "SON"), ("CHIH", "SIN"), ("CHIH", "DGO"),
#                ("CDMX", "MEX"), ("CDMX", "MOR"),
#                ("DGO", "SIN"), ("DGO", "NAY"), ("DGO", "ZAC"), 
#                ("GTO", "ZAC"), ("GTO", "SLP"), ("GTO", "QRO"), ("GTO", "JAL"), ("GTO", "MICH"),
#                ("GRO", "MICH"), ("GRO", "MEX"), ("GRO", "MOR"), ("GRO", "PUE"), ("GRO", "OAX"),
#                ("HGO", "SLP"), ("HGO", "VER"), ("HGO", "PUE"), ("HGO", "TLAX"), ("HGO", "MEX"), ("HGO", "QRO"),
#                ("JAL", "NAY"), ("JAL", "ZAC"), ("JAL", "MICH"),
#                ("MEX", "MICH"), ("MEX", "QRO"), ("MEX", "TLAX"), ("MEX", "PUE"),  ("MEX", "MOR"),
#                ("MICH", "QRO"), 
#                ("MOR", "PUE"),
#                ("NAY", "SIN"), ("NAY", "ZAC"),
#                ("NL", "ZAC"), ("NL", "SLP"), ("NL", "TAMPS"),
#                ("OAX", "PUE"), ("OAX", "VER"),
#                ("PUE", "VER"), ("PUE", "TLAX"),
#                ("QRO", "SLP"),
#                ("QROO", "YUC"),
#                ("SLP", "TAMPS"), ("SLP", "ZAC"), ("SLP", "VER"),
#                ("SIN", "SON"),
#                ("TAB", "VER"),
#                ("TAMPS", "VER") 
#    ]
#colores = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan']
#---------------------------------

#User input ----------------------
# Solicitar nodos, aristas y colores al usuario
nodos = input("Ingrese nodos separados por coma: ").split(', ')
aristas = [tuple(input("Ingrese una arista (separada por coma): ").split(', ')) for _ in range(int(input("Ingrese el número de aristas: ")))]
colores = input("Ingrese colores separados por coma, el orden de ingreso es la prioridad que tiene el color: ").split(', ')
#---------------------------------

print("NODOS:", nodos)
print("ARISTAS:", aristas)
print("NUMERO DE COLORES", len(colores))

#Agregar vertices y aristas al grafo
grafo.add_nodes_from(nodos)
grafo.add_edges_from(aristas)

#Colorear el grafo usando el algoritmo de matula
my_colors = alg_voraz(grafo)
#Si no es posible, el script quiebra en la funcion de arriba
print("Coloreado posible")

#Muestra en pantalla los colores para cada vertice
for vertex, color in my_colors.items():
    print(f"Vertex {vertex}: Color {color}")

#Obten una lista de los nodos del grafo para el coloreo en nx.draw()    
ordered_nodes = list(grafo.nodes())

# Visualize the colored graph
pos = nx.spring_layout(grafo)

# Crear dos subgráficos, uno para el grafo original y otro para el grafo coloreado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

#Visualizar el grafo antes de colorear
nx.draw(grafo, pos=pos, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray', ax=ax1)
ax1.set_title("Original Graph")

nx.draw(grafo, pos=pos, with_labels=True, font_weight='bold', node_color=[my_colors[node] for node in ordered_nodes], cmap=plt.cm.rainbow, ax=ax2)
ax2.set_title("Colored Graph")
plt.show()    