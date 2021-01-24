# Ford-Fulkerson algorith in Python

from collections import defaultdict


# Using BFS as a searching algorithm
def searching_algo_BFS(s, t, parent):
    global ROW
    visited = [False] * (ROW)
    queue = []

    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False

# Applying fordfulkerson algorithm
def ford_fulkerson(source, sink):
    parent = [-1] * (ROW)
    max_flow = 0

    while searching_algo_BFS(source, sink, parent):

        path_flow = float("Inf")
        s = sink
        while(s != source):
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # Adding the path flows
        max_flow += path_flow

        # Updating the residual values of edges
        v = sink
        while(v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow
with open('fluxuri.in') as f:
    n, m = [int(i) for i in f.readline().split()]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    #source = int(f.readline())
    #sink = int(f.readline())
    source = 0
    sink = n-1
    for _ in range(m):
        x, y, c = [int(i) for i in f.readline().split()]
        graph[x][y] = c

print(graph)
ROW = len(graph)


print("Max Flow: %d " % ford_fulkerson(source, sink))