from collections import deque

def readlist(oriented = False, filename = "ex1.txt"):
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
        ePctControl=[0 for i in range (v+1)]
        for x in f.readline().split():
            ePctControl[int(x)]=1
    return lists,v,m,ePctControl

def ex1a(s):
    global n,m,L,ePctControl
    viz=[0 for i in range (n+1)]
    tata=[0 for i in range (n+1)]
    d=[0 for i in range (n+1)]
    parc_bf=[]
    q=deque()
    q.append(s)
    viz[s]=1
    d[s]=0
    while (q):
        nod_actual=q.popleft()
        parc_bf.append(nod_actual)
        for y in L[nod_actual]:
            if (viz[y]==0):
                q.append(y)
                viz[y]=1
                tata[y]=nod_actual
                d[y]=d[nod_actual]+1
                if (ePctControl[y] == 1):
                    print(tata)
                    print(y)
                    print("____")
                    print(y)
                    while (y!= s):
                        y = tata[y]
                        print(y)
                    return

def ex1b(s):
    global n, m, L, ePctControl
    viz = [0 for i in range(n + 1)]
    tata = [0 for i in range(n + 1)]
    d = [0 for i in range(n + 1)]
    parc_bf = []
    q = deque()
    q.append(s)
    viz[s] = 1
    d[s] = 0
    while (q):
        nod_actual = q.popleft()
        parc_bf.append(nod_actual)
        for y in L[nod_actual]:
            if (viz[y] == 0):
                q.append(y)
                viz[y] = 1
                tata[y] = nod_actual
                d[y] = d[nod_actual] + 1
                if (ePctControl[y] == 1):
                    print(tata)
                    print(y)
                    print("____")
                    print(y)
                    while (y != s):
                        y = tata[y]
                        print(y)
                    return


#L,n,m,ePctControl = readlist()
#ex1a(1)
#print(L)
L,n,m,ePctControl=readlist(oriented=True)
ex1b(1)
