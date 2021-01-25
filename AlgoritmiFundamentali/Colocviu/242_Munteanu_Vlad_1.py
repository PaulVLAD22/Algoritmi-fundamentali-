from collections import deque
#pentru a afla arborii de distante ne folosim de bfs deoarece graful este
#neponderat. T1 il aflam cu bfs in s , T2 cu bfs in alt nod(astfel
# T2 nu e graf de distante fata de s ) si pt distanta
#dintre s si u din T2 vom face bfs in T2 cu nodu de inceput s.
#O(n+m) - cea mai mare complexitate fiind data de bfs


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
        s=[int(i) for i in f.readline().split()]
        s=s[0]
    return lists,v,m,s


def bfs(L,s):
    global n,m
    viz=[0 for i in range (n+1)]
    tata=[0 for i in range (n+1)]
    d=[0 for i in range (n+1)]
    muchii_bf=[]
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
                muchii_bf.append((nod_actual,y))
                viz[y]=1
                tata[y]=nod_actual
                d[y]=d[nod_actual]+1
    return muchii_bf,d

L,n,m,s = readlist()
muchii_bf1,d1=bfs(L,s)
print ("T1:")
for p in muchii_bf1:
    print(str(p[0])+" "+str(p[1]))

nod_2=1

while (nod_2==s):
    nod_2+=1

muchii_bf2,d2=bfs(L,nod_2)
print("T2:")
for p in muchii_bf2:
    print(str(p[0])+" "+str(p[1]))

T2={}
for p in muchii_bf2:
    if (T2.get(p[0])==None):
        T2[p[0]]=[p[1]]
    else:
        T2[p[0]].append(p[1])
    if (T2.get(p[1])==None):
        T2[p[1]]=[p[0]]
    else:
        T2[p[1]].append(p[0])

muchii_bf3,d3=bfs(T2,s)

for i in range (1,len(d1)):
    if (d1[i]!=d3[i]):
        print(i)
        break




