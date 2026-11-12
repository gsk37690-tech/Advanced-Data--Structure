from collections import deque

def bfs(graph, start,vertices):    
    visited = [False] * vertices
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in range(vertices):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return 

vertices = 4
grp = [[] for i in range(vertices)]

grp[0].append(1)
grp[2].append(0)

grp[1].append(0)
grp[2].append(2)

grp[1].append(2)
grp[3].append(1)

print(bfs(grp, 0, vertices))