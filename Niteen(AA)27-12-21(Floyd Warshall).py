nV = 4

INF = 999
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

G = [[0, 5, 9, INF],
         [INF, 0, 1, INF],
         [INF, INF, 0, 2],
         [INF, 3, INF, 0]]
floyd_warshall(G)

# O(n cube)