from visualization import draw_graph
from floyd import floyd_warshall_with_paths, reconstruct_path

INF = float('inf')
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
