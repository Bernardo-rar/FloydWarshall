import random
from visualization import draw_graph

def gerar_matriz_adj(n_pontos, n_conexoes, peso_max=10):
    if n_pontos < 2:
        print("Número mínimo de pontos é 2, caso seja 1 a distancia minima é 0")
        return 0

    #if n_conexoes <= n_pontos - 1:
        #print("Número mínimo de conexões deve ser menor que n-pontos?.")
        #return 0
    if n_conexoes > n_pontos * (n_pontos - 1):
        print("Número máximo de conexões excedido.Realmente necessário?")
        return 0

    INF = float('inf')
    matriz = [[INF] * n_pontos for _ in range(n_pontos)]

    # Zera a diagonal principal (distância de um ponto para ele mesmo é 0)
    for i in range(n_pontos):
        matriz[i][i] = 0

    # Garantir conectividade: criar uma árvore mínima (n - 1 arestas)
    pontos_disponiveis = list(range(n_pontos))
    random.shuffle(pontos_disponiveis)

    for i in range(1, n_pontos):
        a = pontos_disponiveis[i]
        b = pontos_disponiveis[random.randint(0, i - 1)]
        peso = random.randint(1, peso_max)
        matriz[a][b] = peso

    # Adicionar arestas extras até atingir o número desejado
    conexoes_atuais = n_pontos - 1
    while conexoes_atuais < n_conexoes:
        i = random.randint(0, n_pontos - 1)
        j = random.randint(0, n_pontos - 1)
        if i != j and matriz[i][j] == INF:
            matriz[i][j] = random.randint(1, peso_max)
            conexoes_atuais += 1

    return matriz
##ef main():
    ##n_pontos = 8
    ##n_conexoes = 25 
    ##peso_max = 7

    ##matriz_adj = gerar_matriz_adj(n_pontos, n_conexoes, peso_max)

    ##matriz = gerar_matriz_adj(7, 21, 5)
    

    ##draw_graph(matriz_adj)
    ##draw_graph(matriz)
    
##main()
