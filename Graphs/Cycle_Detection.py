def has_cycle(graph,current, visited, parent):
    visited[current] = True

    for neighbor in graph[current]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, current):
                return True
        elif parent != neighbor:
            return True

    return False

vertices = 4
grp = [[] for i in range(vertices)]
grp[0] = [1,3]
grp[1] = [0,2]
grp[2] = [1,3]
grp[3] = [0,2]

visited = [False] * vertices
if has_cycle(grp, 0, visited, -1):
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")

