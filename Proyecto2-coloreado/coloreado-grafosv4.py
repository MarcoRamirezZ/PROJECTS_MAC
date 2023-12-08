# Titulo:      Coloreado de grafos con algoritmo voraz, matula y welsh-powell
# Autores:     Xochitl Hernandez
#              Marco Ramirez
# Fecha:       21 de noviembre del 2023
# Descripcion: Este codigo intenta hacer el coloreado de un grafo dado con 3 algoritmos diferentes y los imprime
#              recibe como entradas los nodos y aristas de un grafo, asi como los colores que se quieren usar para el coloreo
#              Devuelve si el grafo es posible de colorear o no, si si puede, devuelve los colores de cada nodo asi como la grafica
#              Si no puede, devuelve el nodo con el error, asi como lo que alcanzo a colorear (no se grafica)

import networkx as nx           #para generar grafos
import matplotlib.pyplot as plt #para graficar
import sys                      #para terminar el programa si el coloreado no es posible
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np

def animarNodos(G, listaAnimacion,colors, pos, seed=123):
    ordered_nodes = list(grafo.nodes())
    node_colors = [colores[colors[node]-1] for node in ordered_nodes]
    print("colors",node_colors)
    size = len(nx.degree(G))
    fig, ax =plt.subplots(figsize=(6,6))
    color_map=["green"]*size
    #pos= nx.spring_layout(G, seed=seed) 
    eSize = len(G.edges())
    edge_color= ["black"]*eSize
    le = [(u,v) for u,v in G.edges()]
    
    def update(i):
        ax.clear()
        v= listaAnimacion[i]
        if(len(v)==1):
            color_map[i]=node_colors[i]
        else:
            edge_color[le.index((v[0],v[1]))]="red"""

        nx.draw(grafo,node_color=color_map, with_labels=True, pos=pos)
        

    ani = matplotlib.animation.FuncAnimation(fig, update, frames = len(listaAnimacion), interval=1000)
    plt.show()  
    return ani


#Voraz el orden es arbitrario, no se ordenan los nodos y toma la lista como la mande el usuario
def alg_voraz(graph):
    #diccionario vacio donde se van a ir agregando los colores
    colors = {}
    
    print("Orden de nodos del algoritmo Voraz:", graph.nodes())
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
    res = []
    # convert list to numpy array
    arr = np.array(nodos)
    # reshape array into chunk matrix
    chunk_matrix = arr.reshape(-1, 1)
    # convert chunk matrix back to list
    res = chunk_matrix.tolist()
    # printing result
    print("Constructed Chunk Matrix : " + str(res))
    ani= animarNodos(grafo,res,colors, pos)
    from IPython.display import HTML
    HTML(ani.to_jshtml())    
    return colors

#Matula ordena de menor a mayor
def alg_matula(graph):
    #diccionario vacio donde se van a ir agregando los colores
    colors = {}
    # Obtener los nodos ordenados por grado en orden de menor a mayor
    nodes_ordered = sorted(graph.nodes(), key=lambda x: graph.degree(x), reverse=False)
    print("Orden de nodos del algoritmo Matula:", nodes_ordered)
    #Para cada nodo en el grafo despues de ser ordenados
    for vertex in nodes_ordered:
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
    res = []
    # convert list to numpy array
    arr = np.array(nodes_ordered)
    # reshape array into chunk matrix
    chunk_matrix = arr.reshape(-1, 1)
    # convert chunk matrix back to list
    res = chunk_matrix.tolist()
    # printing result
    print("Constructed Chunk Matrix : " + str(res))
    ani= animarNodos(grafo,res,colors, pos)
    from IPython.display import HTML
    HTML(ani.to_jshtml())  
    return colors

#welsh powell de mayor a menor
def alg_welsh_powell(graph):
    #diccionario vacio donde se van a ir agregando los colores
    colors = {}
    # Obtener los nodos ordenados por grado en orden de mayor a menor
    nodes_ordered = sorted(graph.nodes(), key=lambda x: graph.degree(x), reverse=True)
    print("Orden de nodos del algoritmo Welsh-Powell:", nodes_ordered)
    #Para cada nodo en el grafo despues de ser ordenados
    for vertex in nodes_ordered:
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
    res = []
    # convert list to numpy array
    arr = np.array(nodes_ordered)
    # reshape array into chunk matrix
    chunk_matrix = arr.reshape(-1, 1)
    # convert chunk matrix back to list
    res = chunk_matrix.tolist()
    # printing result
    print("Constructed Chunk Matrix : " + str(res))
    ani= animarNodos(grafo,res,colors, pos)
    from IPython.display import HTML
    HTML(ani.to_jshtml())  
    return colors

#Grafo no dirigido
grafo = nx.Graph()

#DEBUG input ---------------------
#Definir nodos, aristas y colores
nodos = [ "AGS",  "BC", "BCS",  "CAMP", "COAH", "COL", "CHIS", "CHIH", "CDMX", "DGO", "GTO",  "GRO", "HGO",  "JAL", "MEX",  "MICH", "MOR",  "NAY", "NL",   "OAX", "PUE",  "QRO", "QROO", "SLP", "SIN",  "SON", "TAB",  "TAMPS", "TLAX", "VER", "YUC",  "ZAC"]
aristas = [ ("AGS", "ZAC"), ("AGS", "JAL"),
                ("BC", "BCS"),  ("BC", "SON"),
                ("CAMP", "TAB"), ("CAMP", "YUC"), ("CAMP", "QROO"),
                ("COAH", "CHIH"), ("COAH", "DGO"), ("COAH", "ZAC"), ("COAH", "NL"),
                ("COL", "JAL"), ("COL", "MICH"), 
                ("CHIS", "TAB"), ("CHIS", "VER"), ("CHIS", "OAX"),
                ("CHIH", "SON"), ("CHIH", "SIN"), ("CHIH", "DGO"),
                ("CDMX", "MEX"), ("CDMX", "MOR"),
                ("DGO", "SIN"), ("DGO", "NAY"), ("DGO", "ZAC"), 
                ("GTO", "ZAC"), ("GTO", "SLP"), ("GTO", "QRO"), ("GTO", "JAL"), ("GTO", "MICH"),
                ("GRO", "MICH"), ("GRO", "MEX"), ("GRO", "MOR"), ("GRO", "PUE"), ("GRO", "OAX"),
                ("HGO", "SLP"), ("HGO", "VER"), ("HGO", "PUE"), ("HGO", "TLAX"), ("HGO", "MEX"), ("HGO", "QRO"),
                ("JAL", "NAY"), ("JAL", "ZAC"), ("JAL", "MICH"),
                ("MEX", "MICH"), ("MEX", "QRO"), ("MEX", "TLAX"), ("MEX", "PUE"),  ("MEX", "MOR"),
                ("MICH", "QRO"), 
                ("MOR", "PUE"),
                ("NAY", "SIN"), ("NAY", "ZAC"),
                ("NL", "ZAC"), ("NL", "SLP"), ("NL", "TAMPS"),
                ("OAX", "PUE"), ("OAX", "VER"),
                ("PUE", "VER"), ("PUE", "TLAX"),
                ("QRO", "SLP"),
                ("QROO", "YUC"),
                ("SLP", "TAMPS"), ("SLP", "ZAC"), ("SLP", "VER"),
                ("SIN", "SON"),
                ("TAB", "VER"),
                ("TAMPS", "VER") 
    ]
colores = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan']
#---------------------------------

#User input ----------------------
# Solicitar nodos, aristas y colores al usuario
#nodos = input("Ingrese nodos separados por coma: ").split(', ')
#aristas = [tuple(input("Ingrese una arista (separada por coma): ").split(', ')) for _ in range(int(input("Ingrese el número de aristas: ")))]
#colores = input("Ingrese colores separados por coma, el orden de ingreso es la prioridad que tiene el color: ").split(', ')
#---------------------------------

print("----------------------------------------------------------")
print("NODOS:", nodos)
print("----------------------------------------------------------")
print("ARISTAS:", aristas)
print("----------------------------------------------------------")
print("NUMERO DE COLORES", len(colores))
print("----------------------------------------------------------")

#Agregar vertices y aristas al grafo
grafo.add_nodes_from(nodos)
grafo.add_edges_from(aristas)

# Visualize the colored graph
pos = nx.spring_layout(grafo)

#Colorear el grafo usando el algoritmo voraz
my_colors_voraz = alg_voraz(grafo)
#Colorear el grafo usando el algoritmo de matula
my_colors_matula = alg_matula(grafo)
#Colorear el grafo usando el algoritmo de welsh-powell
my_colors_welsh = alg_welsh_powell(grafo)

#Si no es posible, el script quiebra en la funcion de arriba
print("Coloreado posible")

# Ordenar los nodos en my_colors_matula según el orden de los nodos en el grafo para que no haya errores
# al momento de imprimir la correspondencia de nodo y color en nx.draw
ordered_nodes = list(grafo.nodes())
node_colors_voraz = [colores[my_colors_voraz[node]-1] for node in ordered_nodes]
node_colors_matula = [colores[my_colors_matula[node]-1] for node in ordered_nodes]
node_colors_welsh = [colores[my_colors_welsh[node]-1] for node in ordered_nodes]

#Muestra en pantalla los colores para cada vertice de los 3 algoritmos
print("----------------------------------------------------------")
print("Nodos y colores del algoritmo voraz")
for vertex, color in my_colors_voraz.items():
    print(f"Vertex {vertex}: Color {colores[color-1]}")

print("----------------------------------------------------------")
print("Nodos y colores del algoritmo Matula")
for vertex, color in my_colors_matula.items():
    print(f"Vertex {vertex}: Color {colores[color-1]}")

print("----------------------------------------------------------")
print("Nodos y colores del algoritmo Welsh-Powell")
for vertex, color in my_colors_welsh.items():
    print(f"Vertex {vertex}: Color {colores[color-1]}")

# Crear dos subgráficos, uno para el grafo original y otro para el grafo coloreado
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

#Visualizar el grafo antes de colorear
nx.draw(grafo, pos=pos, with_labels=True, font_weight='bold', node_color=node_colors_voraz, ax=ax1)
ax1.set_title("Algoritmo Voraz")

nx.draw(grafo, pos=pos, with_labels=True, font_weight='bold', node_color=node_colors_matula, ax=ax2)
ax2.set_title("Algoritmo Matula")  

nx.draw(grafo, pos=pos, with_labels=True, font_weight='bold', node_color=node_colors_welsh, ax=ax3)
ax3.set_title("Algoritmo Welsh-Powell")

plt.show()  


