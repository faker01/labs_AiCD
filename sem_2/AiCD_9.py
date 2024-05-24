def bellman_ford(graph, start):
    n = len(graph)
    inf = float('inf')
    dist = [inf] * n
    dist[start] = 0

    for _ in range(1, n):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != 0:
                    new_dist = dist[u] + graph[u][v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist

    for u in range(n):
        for v in range(n):
            if graph[u][v] != 0:
                new_dist = dist[u] + graph[u][v]
                if new_dist < dist[v]:
                    print("Граф содержит отрицательный цикл")
                    return None

    return dist


with open("inputt.txt", "r") as f:
    data = f.read()
data = [i.split(" ") for i in data.split("\n")]

n = len(data)
for i in range(n):
    for j in range(n):
        data[i][j] = int(data[i][j])

start_vertex = 0
shortest_paths = bellman_ford(data, start_vertex)
if shortest_paths:
    print("Shortest paths from vertex", start_vertex, ":")
    for i, dist in enumerate(shortest_paths):
        print("Vertex", i, ":", dist)