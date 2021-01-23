from collections import deque

def readmat(oriented = False, filename = "graf.in"):
    mat = []
    with open(filename,"r") as f:
        v,m = [int(i) for i in f.readline().split()]
        for _ in range(v+1):
            mat.append([0]*(v+1))
        for _ in range(m):
            x,y = [int(i) for i in f.readline().split()]
            mat[x][y] = 1
            if not oriented:
                mat[y][x] = 1
    return mat

def readlist(oriented = False, filename = "graf.in"):
    lists = {}
    with open(filename,"r") as f:
        v,m = [int(i) for i in f.readline().split()]
        for _ in range(m):
            x, y = [int(i) for i in f.readline().split()]
            if x in lists.keys():
                lists[x].append(y)
            else:
                lists[x] = [y]
            if not oriented:
                if y in lists.keys():
                    lists[y].append(x)
                else:
                    lists[y] = [x]
    return lists


def shortest_path(adjlist, points, start = 1):
    q = deque()
    q.append(start)
    visited = {}
    level = {}
    dads = {}
    point = False
    for i in adjlist.keys():
        visited[i] = False
        dads[i] = []
        level[i] = 0
    visited[start] = True
    dads[start].append(None)
    while q:
        current = q.popleft()
        for i in adjlist[current]:
            if not visited[i]:
                #dads[i].append(current)
                level[i] = level[current]+1
                visited[i] = True
                q.append(i)
                if i in points and point == False:
                    point = i
            else:
                if level[i] < level[current]:
                    dads[current].append(i)
    print(point)
    print("-"*100)
    print(dads)
    current = point
    solution = []
    while True:
        solution.append(current)
        current = dads[current][0]
        if current == None:
            break
    solution.reverse()
    print()
    print(point," with the path - ",*solution)

def testcyclic(adjlist, start = 1):
    q = deque()
    q.append(start)
    visited = {}
    dads = {}
    level = {}
    for i in adjlist.keys():
        visited[i] = 0
        dads[i] = []
        level[i] = 0
    visited[start] = 1
    dads[start].append(None)
    while q:
        current = q.popleft()
        for i in adjlist[current]:
            if visited[i] == 0:
                q.append(i)
                dads[i].append()
            else:
                if level[i] < level[current]:
                    dads[current].append(i)


#def testcyclicrecursive(adjlist,current,visited,dads,levels)

M = readmat()

for i in M:
    print(*i)

L = readlist()

print(L)

nodelist =[8,9]

shortest_path(L,nodelist)

