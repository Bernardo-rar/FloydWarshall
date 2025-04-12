
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
