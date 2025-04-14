INF = float('inf')  # Constante usada para representar "infinito" (sem conexão entre nós)

def floyd_warshall_with_paths(adj):
    """
    Executa o algoritmo de Floyd-Warshall e retorna:
    - a matriz de distâncias mínimas entre todos os pares de nós
    - a matriz next_node que permite reconstruir os caminhos mínimos
    """

    n = len(adj)  # Número de vértices no grafo

    # Inicializa a matriz de distâncias com infinito e a matriz de caminhos com None
    distance = [[INF] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]

    # Inicializa as matrizes com base na matriz de adjacência fornecida
    for i in range(n):
        for j in range(n):
            if i == j:
                # A distância de um nó para ele mesmo é sempre zero
                distance[i][j] = 0
                next_node[i][j] = i
            elif adj[i][j] != INF:
                # Se há uma aresta direta de i para j, inicializamos com esse peso
                distance[i][j] = adj[i][j]
                next_node[i][j] = j  # O próximo nó no caminho de i para j é o próprio j

    # Algoritmo de Floyd-Warshall propriamente dito
    # Para cada vértice intermediário k...
    for k in range(n):
        # ... verifica todos os pares de vértices (i, j)
        for i in range(n):
            for j in range(n):
                # Se o caminho passando por k é mais curto do que o atual, atualiza
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_node[i][j] = next_node[i][k]  # Atualiza o próximo nó no caminho

    return distance, next_node  # Retorna a matriz de distâncias e os caminhos reconstruíveis

def reconstruct_path(u, v, next_node, weight_matrix):
    """
    Reconstrói o caminho mínimo de u até v usando a matriz next_node.
    Também imprime o peso de cada aresta no caminho com base na weight_matrix.
    
    Parâmetros:
    - u: nó de origem
    - v: nó de destino
    - next_node: matriz com os próximos nós no caminho mínimo
    - weight_matrix: matriz de pesos original do grafo
    
    Retorna:
    - Lista com a sequência de nós no caminho mínimo
    """
    if next_node[u][v] is None:
        print(f"Não existe caminho de {u} até {v}.")
        return []

    path = [u]
    print(f"Caminho de {u} até {v}:")

    while u != v:
        next_u = next_node[u][v]
        peso = weight_matrix[u][next_u]
        print(f"  {u} -> {next_u} (peso {peso})")
        path.append(next_u)
        u = next_u

    return path