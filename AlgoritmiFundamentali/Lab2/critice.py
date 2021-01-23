from collections import deque

with open("ex1.txt") as f:
    n, m = [int(i) for i in f.readline().split()]
    lists = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y,val = [int(i) for i in f.readline().split()]
        lists[x].append(y)
        lists[y].append(x)
# LISTA DE LISTE INPUT


'''A recursive function that finds and prints bridges 
using DFS traversal 
u --> The vertex to be visited next 
visited[] --> keeps tract of visited vertices 
disc[] --> Stores discovery times of visited vertices 
parent[] --> Stores parent vertices in DFS tree'''


def muchie_critica(u, visited, parent, low, disc):
    global Time
    #global n
    global lists
    # Mark the current node as visited and print it
    visited[u] = True

    # Initialize discovery time and low value
    disc[u] = Time
    low[u] = Time
    Time += 1

    # Recur for all the vertices adjacent to this vertex
    for v in lists[u]:
        # If v is not visited yet, then make it a child of u
        # in DFS tree and recur for it
        if visited[v] == False:
            parent[v] = u
            muchie_critica(v, visited, parent, low, disc)

            # Check if the subtree rooted with v has a connection to
            # one of the ancestors of u
            low[u] = min(low[u], low[v])

            ''' If the lowest vertex reachable from subtree 
            under v is below u in DFS tree, then u-v is 
            a bridge'''
            if low[v] > disc[u]:
                print(u,v)


        elif v != parent[u]:  # Update low value of u for parent function calls.
            low[u] = min(low[u], disc[v])

            # DFS based function to find all bridges. It uses recursive


'''A recursive function that find articulation points  
using DFS traversal 
u --> The vertex to be visited next 
visited[] --> keeps tract of visited vertices 
disc[] --> Stores discovery times of visited vertices 
parent[] --> Stores parent vertices in DFS tree 
ap[] --> Store articulation points'''
def punct_critic(u, visited, ap, parent, low, disc):
    global Time
    #global n
    global lists

    # Count of children in current node
    children = 0
    # Mark the current node as visited and print it
    visited[u] = True
    # Initialize discovery time and low value
    disc[u] = Time
    low[u] = Time
    Time += 1

    # Recur for all the vertices adjacent to this vertex
    for v in lists[u]:
        # If v is not visited yet, then make it a child of u
        # in DFS tree and recur for it
        if visited[v] == False:
            parent[v] = u
            children += 1
            punct_critic(v, visited, ap, parent, low, disc)

            # Check if the subtree rooted with v has a connection to
            # one of the ancestors of u
            low[u] = min(low[u], low[v])

            # u is an articulation point in following cases
            # (1) u is root of DFS tree and has two or more chilren.
            if parent[u] == -1 and children > 1:
                ap[u] = True

            # (2) If u is not root and low value of one of its child is more
            # than discovery value of u.
            if parent[u] != -1 and low[v] >= disc[u]:
                ap[u] = True

                # Update low value of u for parent function calls
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


            # Mark all the vertices as not visited and Initialize parent and visited,
# and ap(articulation point) arrays
#####################################################################
print('MUCHII CRITICE')
Time = 0
visited = [False for _ in range(n+1)]
disc = [float("Inf") for _ in range(n+1)]
low = [float("Inf") for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]

for i in range(1,n+1):
    if visited[i] == False:
        muchie_critica(i, visited, parent, low, disc)
#######################################################################
print()
print('PUNCTE CRITICE')
Time = 0
visited = [False for _ in range(n+1)]
disc = [float("Inf") for _ in range(n+1)]
low = [float("Inf") for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
ap = [False for _ in range(n+1)] #store articulation_points

for i in range(1,n+1):
    if visited[i] == False:
        punct_critic(i, visited, ap, parent, low, disc)

for i in range(1,n+1):
    if ap[i]:
        print(i)