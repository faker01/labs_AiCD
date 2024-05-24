def dijkstra(graph, start):
    n = len(graph)
    inf = float('inf')
    dist = [inf] * n
    visited = [False] * n
    dist[start] = 0

    for _ in range(n):
        u = -1
        min_dist = inf
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                u = i
                min_dist = dist[i]
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if not visited[v] and graph[u][v] > 0:
                new_dist = dist[u] + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
    return dist


with open("inputt.txt", "r") as f:
    data = f.read()
data = [i.split(" ") for i in data.split("\n")]

n = len(data)
for i in range(n):
    for j in range(n):
        data[i][j] = int(data[i][j])

start_vertex = 0
shortest_paths = dijkstra(data, start_vertex)
print("Shortest paths from vertex", start_vertex, ":")
for i, dist in enumerate(shortest_paths):
    print("Vertex", i, ":", dist)