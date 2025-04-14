from visualization import draw_graph
from floyd import floyd_warshall_with_paths, reconstruct_path
from geradorMatriz import gerar_matriz_adj

INF = float('inf')
adj = [
    [0,   3, INF, 5],
    [2,   0, INF, 4],
    [INF, 1,   0, INF],
    [INF, INF, 2,   0]
]


dist, next_node = floyd_warshall_with_paths(adj)


# Exemplo: caminho mínimo de 0 para 2
path_0_2 = reconstruct_path(0, 2, next_node)
print("Caminho mínimo de 0 para 3:", path_0_2)
print("Distância mínima:", dist[0][2])
draw_graph(adj, path_0_2)


blele=gerar_matriz_adj(5, 10, 5)

dist1, next_node1 = floyd_warshall_with_paths(blele)

path_0_3= reconstruct_path(0, 3, next_node1)
print("Caminho mínimo de 0 para 5:", path_0_3)
print("Distância mínima:", dist1[0][3])
# Visualizar grafo e o caminho mínimo de 0 até 2

for row in blele:
    print(row)
print("---"*20)
for row in dist1:
    print(row)


draw_graph(blele,path_0_3)


