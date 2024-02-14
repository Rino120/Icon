import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

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

# Visualizzazione Grafo
nx.draw(G, with_labels=True)
plt.show()

print("Numero di nodi: ", G.number_of_nodes())
print("Numero di archi: ", G.number_of_edges())
