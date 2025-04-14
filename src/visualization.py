import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(adj, path=None):
    """
    Desenha o grafo direcionado com pesos e destaca o caminho mínimo se fornecido.
    A distância entre os nós é ajustada com base na quantidade de nós.
    """
    INF = float('inf')
    G = nx.DiGraph()
    n = len(adj)

    # Adiciona arestas com pesos
    for i in range(n):
        for j in range(n):
            if adj[i][j] != INF:
                G.add_edge(i, j, weight=adj[i][j])

    # Ajusta dinamicamente a distância entre os nós
    k =  (n ** 1.5)
    pos = nx.spring_layout(G, k=k, seed=42)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    path_edges = set(zip(path, path[1:])) if path else set()

    edge_colors = ['red' if (u, v) in path_edges else 'black' for u, v in G.edges()]

    nx.draw(
        G, pos, with_labels=True, node_color='lightblue',
        edge_color=edge_colors, node_size=500, font_size=10,
        arrows=True, connectionstyle='arc3,rad=0.1'
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Grafo com caminho mínimo (se fornecido)")
    plt.show()
