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

def prim(nod,graf):
    global d,tata
    q=deque()
    for i in range (1,n+1):
        q.append(i)
    d[nod]=0
    while (q):
        d_minim=10000
        d_minim_index=0
        for i in range (len(q)):
            if (d[q[i]]<d_minim):
                d_minim=d[q[i]]
                d_minim_index=i
        nod_actual = q[d_minim_index]
        q.remove(q[d_minim_index])
        for j in range (1,n+1):
            if (graf[nod_actual][j]!=0):
                if (d[j]>graf[nod_actual][j] and j in q ):
                    d[j]=graf[nod_actual][j]
                    tata[j]=nod_actual
            print(nod_actual,d[1:],tata[1:])

    print(tata)

#VERIFICA
graf,muchii_sortate,n,m=readmat()
d=[ 1000 for i in range (n+1)]
tata= [0 for i in range (n+1)]
prim(1,graf)
