from collections import deque

def readmat(oriented = False, filename = "ex1.txt"):
    mat = []
    with open(filename,"r") as f:
        muchii_sortate=[]
        v,m = [int(i) for i in f.readline().split()]
        for _ in range(v+1):
            mat.append([0]*(v+1))
        for _ in range(m):
            x,y,val = [int(i) for i in f.readline().split()]
            mat[x][y] = val
            muchii_sortate.append((x,y))
            if not oriented:
                mat[y][x] = val
    return mat,muchii_sortate,v,m

#drum minim de la s la t

def dijkstra(s,n,d,tata,graf):
    d[s]=0
    tata[s]=0
    q = deque()
    for i in range (1,n+1):
        q.appendleft(i)
    while (q):
        d_minim = 1000
        d_minim_index = 0
        for i in range(len(q)):
            if (d[q[i]] < d_minim):
                d_minim = d[q[i]]
                d_minim_index = i
        nod_actual = q[d_minim_index]
        q.remove(nod_actual)
        for j in range (1,n+1):
            if (graf[nod_actual][j]!=0):
                if (d[j]>graf[nod_actual][j]+d[nod_actual]):
                    d[j]=graf[nod_actual][j]+d[nod_actual]
                    tata[j]=nod_actual
            print(nod_actual,d,tata)
    return d,tata



graf,muchii_sortate,n,m=readmat(oriented=True)

s=1
t=5
d=[1000 for i in range (n+1)]
tata=[1000 for i in range(n+1)]
d,tata=dijkstra(s,n,d,tata,graf)
drum=[]
while (t!=tata[s]):
    drum.append(t)
    t=tata[t]
print(drum[::-1])
