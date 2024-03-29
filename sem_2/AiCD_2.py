from collections import deque


def bfs(graph, root):
    lens = [0]
    visited, queue = set(), deque([root])
    visited.add(root)
    l = 0
    while queue:
        l += 1
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                lens.append(l)
                queue.append(neighbour)
    return visited, lens


with open("input.txt", "r") as f:
    data = f.read()
data = [i.split(" ") for i in data.split("\n")]

graph = {}
n = len(data)
for i in range(n):
    r = []
    for j in range(n):
        if data[i][j] == "1":
            r.append(j)
    graph[i] = r

print(bfs(graph, 0))