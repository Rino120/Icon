from igraph import *
import Utils

# Lista dei valori dei vertici
vertex_values = []
for x in range(0, 20):
    vertex_values.append(str(x))

# Esegue una ricerca in ampiezza (BFS) su un grafo
def bfs(graph, start, end):
    # Mantieni una coda di percorsi
    queue = [[start]]
    # Inserisce il primo percorso nella coda
    while queue:
        # Ottiene il primo percorso dalla coda
        path = queue.pop(0)
        # Ottiene l'ultimo nodo dal percorso
        node = path[-1]
        # Percorso trovato
        if node == end:
            return path
        # Enumera tutti i nodi adiacenti, costruisce un
        # nuovo percorso e lo inserisce nella coda
        for adjacent in graph.neighbors(node):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

# Calcola il costo di un percorso
def path_cost(path):
    """
    restituisce il costo di un percorso
    :param path: percorso di cui trovare il costo
    :return: costo del percorso
    """
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]

# Aggiunge il costo alla lista dei vicini
def add_cost(graph, start, neighbours):
    """
    aggiunge il costo alla lista dei vicini
    :param graph:
    :param start:
    :param neighbours:
    :return weighted_list: lista dei vicini con i costi aggiunti
    """
    weighted_list = []

    for node2 in neighbours:
        weighted_list.append([node2, graph.es.select(_source=start, _target=node2)['weight'][0]])

    return weighted_list

# Esegue una ricerca del percorso con il costo più basso
def lowest_cost_first(graph, start, end):
    """
    restituisce il percorso al nodo finale, partendo dal nodo di inizio, utilizzando la ricerca del costo più basso
    :param graph:
    :param start:
    :param end:
    :return path: percorso al nodo finale
    """
    visited = []
    queue = [[(start, 0)]]

    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        visited.append(node)
        if node == end:
            return path

        else:
            adjacent_nodes = add_cost(graph, node, graph.neighbors(node))
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)

# Crea il grafo pesato
def setup_graph():
    """
    crea un grafo pesato
    :return graph: grafo
    :return edges: lista degli archi del grafo
    :return weights: lista dei pesi degli archi del grafo
    """

    # Definizione degli archi e dei loro pesi
    a = [('0', '1', 3), ('0', '4', 2), ('0', '7', 3), ('1', '2', 5), ('2', '3', 2), ('4', '5', 3), ('4', '6', 3),
         ('7', '8', 5), ('8', '9', 2), ('4', '10', 5), ('10', '11', 3), ('10', '15', 2), ('10', '13', 3), ('11', '12', 5),
         ('12', '17', 2), ('17', '16', 5), ('15', '16', 2), ('15', '18', 3), ('18', '19', 5), ('19', '14', 2),
         ('14', '13', 5)]

    edge = []
    weights = []

    # Generazione archi e pesi
    for i in range(20):

        for j in range(2):
            k = 2
            edge.append(a[i][j])
        weights.append(a[i][k])

    # Creazione archi e pesi
    edges = [(i, j) for i, j in zip(edge[::2], edge[1::2])]
    list1 = []

    # Creazione grafo e aggiunta di vertici
    graph = Graph()
    for i in range(0, 20):
        graph.add_vertex(i)

    # Aggiunta archi al grafo e attribuzione pesi agli archi
    graph.add_edges(list1)
    graph.es['weight'] = weights
    edges = graph.get_edgelist()
    return graph, edges, weights

# Trova una soluzione
def find_solution(graph, start):
    """
    esegue una ricerca sul grafo e restituisce il percorso sotto forma di lista di nodi
    :param start: nodo di partenza
    :param graph: grafo su cui effettuare la ricerca
    :return solution: lista di nodi rappresentanti la soluzione
    """
    goal = -1
    while goal < 0 or goal > 19:
        goal = int(input("Inserisci il nodo che vuoi raggiungere (0-19)\n"))

        if goal < 0 or goal > 19:
            print("Valore non corretto")

    search_method = -1
    while search_method != 1 and search_method != 2:

        search_method = int(input("Inserisci il metodo di ricerca: \n1: Ricerca in ampiezza (BFS)\n2: Ricerca del percorso con il costo più basso\n"))

        if search_method == 1:
            solution = bfs(graph, start, goal)
            print("La soluzione è:\n" + str(solution))
