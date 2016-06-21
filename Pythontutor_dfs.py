# Path
#
#   2--0--6--7   1--9   5
#   |  |  |
#   3--4  8 
#
n = 10
adj_list = [[2, 4, 6],
            [9],
            [0, 3],
            [2, 4],
            [0, 3],
            [],
            [0, 7, 8],
            [6],
            [6],
            [1]]

s = 3
t = 7
i = [0] * 2
visited = [False] * n  # массив "посещена ли вершина?"
num_components = 0
component = [-1] * n  # для каждой вершины храним номер её компоненты
path = []

def dfs(v):
    component[v] = num_components
    visited[v] = True
    for w in adj_list[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)

for v in range(n):
    if not visited[v]:
        dfs(v)
        num_components += 1

def bind(a, b):
    if component[a] == component[b]:
        return 1
    else:
        return 0

def dfs_path(a, b):
    if i[0] == 0:
        path.append(a)
    if a != b:
        visited[a] = True
        for x in adj_list[a]:
            if not visited[x]:  # посещён ли текущий сосед?
                dfs_path(x, b)
        if i[0] == 0:
            path.pop()
    else:
        i[0] += 1

dfs(s)
print(bind(s, t))
visited = [False] * n
dfs_path(s, t)
print(path)
