import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(adj, path=None):
    """
    Desenha o grafo e destaca o caminho mínimo se fornecido.
    """
    INF = float('inf')
    G = nx.DiGraph()
    n = len(adj)

    # Adiciona arestas com pesos
    for i in range(n):
        for j in range(n):
            if adj[i][j] != INF:
                G.add_edge(i, j, weight=adj[i][j])

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Cor vermelha para o caminho, preto para o resto
    edge_colors = ['red' if path and (u, v) in zip(path, path[1:]) else 'black' for u, v in G.edges()]

    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color=edge_colors, node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Grafo com caminho mínimo (se fornecido)")
    plt.show()
