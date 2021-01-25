
#a)
#Nu am avut timp pentru a face si implementarea.

#Ideea de rezolvare : Adaugam 2 noduri ,unul de start si unul de destinatie. Astfel, ducem cate o muchie
#de la nodul de start la toate nodurile din prima jumatate a grafului bipartit, si de la fiecare nod din a doua in nodul destinatie. Tratam ca pe o problema
#de flux, astfel, cuplajul maxim in graful initial este egal cu fluxul maxim in noul graf in care avem muchii orientate de la 0 la prima jumatate,
#de la primul set la al doilea set si de la al doilea set la nodul n + 1. Astfel, aplicand Ford Fulkerson vom determina un cuplaj maximal.

#Ca implementarea am pus un program cu ford flukeron

#Complexitatea este O(n * m ), dat de complexitatea lui Ford Fulkerson

#b)



with open('ex1.txt') as f:
    n, m = [int(i) for i in f.readline().split()]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    source = 0
    sink = n-1
    for _ in range(m):
        x, y = [int(i) for i in f.readline().split()]
        graph[x-1][y-1] = 1

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

def ford_fulkerson(source, sink):
    parent = [-1] * (ROW)
    max_flow = 0

    while searching_algo_BFS(source, sink, parent):

        path_flow = float("Inf")
        s = sink
        while(s != source):
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]


        max_flow += path_flow


        v = sink
        while(v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


ROW = len(graph)


print("Max Flow: %d " % ford_fulkerson(source, sink))