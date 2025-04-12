INF = float('inf')

def floyd_warshall(adj):
    n = len(adj)
    
    # Inicializa a matriz de distâncias
    distance = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                distance[i][j] = 0
            elif adj[i][j] != 0:
                distance[i][j] = adj[i][j]
            else:
                distance[i][j] = INF

    # Aplica o algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance


adj = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

dist = floyd_warshall(adj)

for row in dist:
    print(row)
