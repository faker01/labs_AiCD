"""
def bfs(st, mx, l, goal):
    path = []
    for k in range(l):
        if mx[k] == 1:
            mx[k] = 0
            return [st] + [bfs(k, mx, l)]
    return st
"""

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)



with open("input.txt", "r") as f:
    matrix = f.read()

matrix = matrix.split("\n")
n = len(matrix)
for i in range(n):
    matrix[i] = matrix[i].split(", ")

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(matrix[i][j])

s_p = int(input())

