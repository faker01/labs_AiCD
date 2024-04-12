from collections import deque


def bfs(graph, root):
    lens = [0]
    visited, queue = [], deque([root])
    visited.append(root)
    l = 0
    flag = True
    while queue:
        if flag:
            l += 1
            flag = False
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                lens.append(l)
                queue.append(neighbour)
                flag = True

    return visited


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

n = len(graph)
p = []
for i in range(n):
    new = sorted(bfs(graph, i))
    if new not in p:
        p.append(sorted(bfs(graph, i)))

with open("output.txt", "w") as f:
    for i in range(len(p)):
        f.write("{}: {}\n".format(i, p[i]))