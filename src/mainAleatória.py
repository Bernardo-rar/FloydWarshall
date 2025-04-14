from visualization import draw_graph
from floyd import floyd_warshall_with_paths, reconstruct_path
from geradorMatriz import gerar_matriz_adj

blele=gerar_matriz_adj(5, 10, 5)


print("Matriz de adjacência gerada aleatoriamente:")
print("---"*20)

dist1, next_node1 = floyd_warshall_with_paths(blele)

path_0_3= reconstruct_path(0, 3, next_node1,blele)
print("Caminho mínimo de 0 para 5:", path_0_3)
print("Distância mínima:", dist1[0][3])
# Visualizar grafo e o caminho mínimo de 0 até 2

for row in blele:
    print(row)
print("---"*20)
for row in dist1:
    print(row)


draw_graph(blele,path_0_3)