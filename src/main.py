import matplotlib.pyplot as plt
import networkx as nx

INF = float('inf')

def floyd_warshall_with_paths(adj):
    """
    Executa o algoritmo de Floyd-Warshall e retorna:
    - a matriz de distâncias mínimas
    - uma matriz com os caminhos reconstruídos
    """
    n = len(adj)
    
    # Inicializa distâncias e caminhos
    distance = [[INF] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]

    # Inicialização com base na matriz de adjacência
    for i in range(n):
        for j in range(n):
            if i == j:
                distance[i][j] = 0
                next_node[i][j] = i
            elif adj[i][j] != INF:
                distance[i][j] = adj[i][j]
                next_node[i][j] = j

    # Algoritmo de Floyd-Warshall com reconstrução de caminho
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_node[i][j] = next_node[i][k]

    return distance, next_node

def reconstruct_path(u, v, next_node):
    """
    Reconstrói o caminho de u até v usando a matriz next_node.
    """
    if next_node[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path

def draw_graph(adj, path=None):
    """
    Desenha o grafo e destaca o caminho mínimo se fornecido.
    """
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


adj = [
    [0,   3, INF, 5],
    [2,   0, INF, 4],
    [INF, 1,   0, INF],
    [INF, INF, 2,   0]
]

dist, next_node = floyd_warshall_with_paths(adj)

# Exemplo: caminho mínimo de 0 para 2
path_0_2 = reconstruct_path(0, 3, next_node)
print("Caminho mínimo de 0 para 3:", path_0_2)
print("Distância mínima:", dist[0][3])

# Visualizar grafo e o caminho mínimo de 0 até 2
draw_graph(adj, path_0_2)
