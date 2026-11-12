def dfs(graph,current,visited):
    visited[current] = True
    print(current, end=" ")

    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

vertices = 6
graph = [[] for j in range(vertices)]

graph[0] = [1, 2]
graph[1] = [0, 3, 4]
graph[2] = [0, 5]
graph[3] = [1]
graph[4] = [1]
graph[5] = [2]

visited = [False] * vertices
dfs(graph, 0, visited)