import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

<<<<<<< HEAD
# CreazioneNodi
G.add_node(0)
G.add_nodes_from([1, 2, 3])
G.add_nodes_from([4, 5])
G.add_nodes_from([6, 7, 8])
G.add_nodes_from([9, 10, 11])
G.add_nodes_from([12, 13])

# Creazione Archi
G.add_edges_from([(0, 1), (1, 2), (2, 3)])
G.add_edges_from([(0, 4), (4, 5)])
G.add_edges_from([(0, 6), (6, 7), (7, 8)])
G.add_edges_from([(8, 9), (9, 10), (10, 11)])
G.add_edges_from([(8, 12), (12, 13)])
G.add_edges_from([(3, 11)])
=======
# Creazione Nodi
G.add_node(0)
G.add_nodes_from([1,2,3])
G.add_nodes_from([4,5])
G.add_nodes_from([6,7,8])
G.add_nodes_from([9,10,11])
G.add_nodes_from([12,13])


# Creazione Archi
G.add_edges_from([(0,1),(1,2),(2,3)])
G.add_edges_from([(0,4),(4,5),])
G.add_edges_from([(0,6),(6,7),(7,8)])
G.add_edges_from([(8,9),(9,10),(10,11)])
G.add_edges_from([(8,12),(12,13)])
G.add_edges_from([(3,11)])

>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d

# Visualizzazione Grafo
nx.draw(G, with_labels=True)
plt.show()

print("Numero di nodi: ", G.number_of_nodes())
print("Numero di archi: ", G.number_of_edges())
<<<<<<< HEAD
=======

#shortest_path = nx.shortest_path(G,source=0, target=13)
#print("Cammino più breve tra 0 e 3: ", shortest_path)
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
