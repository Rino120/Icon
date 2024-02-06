import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Creazione Nodi
G.add_node(0)
G.add_nodes_from([1,2,3])
G.add_nodes_from([4,5,6])
G.add_nodes_from([7,8,9])
G.add_nodes_from([10,11,12])
G.add_nodes_from([15,16,17])
G.add_nodes_from([13,14])
G.add_nodes_from([18,19])

# Creazione Archi
G.add_edges_from([(0,1),(1,2),(2,3)])
G.add_edges_from([(0,4),(4,5),(4,6)])
G.add_edges_from([(0,7),(7,8),(8,9)])
G.add_edges_from([(4,10),(10,11),(11,12)])
G.add_edges_from([(10,15),(15,16),(16,17),(12,17)])
G.add_edges_from([(10,13),(13,14)])
G.add_edges_from([(15,18),(18,19),(14,19)])


# Visualizzazione Grafo
nx.draw(G, with_labels=True)
plt.show()

print("Numero di nodi: ", G.number_of_nodes())
print("Numero di archi: ", G.number_of_edges())

shortest_path = nx.shortest_path(G,source=1, target=3)
print("Cammino più breve tra 0 e 3: ", shortest_path)