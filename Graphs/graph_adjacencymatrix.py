from collections import deque

vertices = 4
graph = [[0 for j in range(vertices)]
        for i in range(vertices)]
graph[0][1] = 1
graph[1][0] = 1

graph[2][0] = 1
graph[0][2] = 1

graph[1][2] = 1
graph[2][1] = 1

graph[1][3] = 1
graph[3][1] = 1

for row in graph:
    print(row)

grp = [[] for i in range(vertices)]

grp[0].append(1)
grp[2].append(0)

grp[1].append(0)
grp[2].append(2)

grp[1].append(2)
grp[3].append(1)

for i in range(vertices):
    print(i, "->", grp[i])



