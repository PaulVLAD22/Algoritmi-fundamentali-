from collections import deque


def readmat(oriented = False, filename = "ex1.txt"):
    mat = []
    with open(filename,"r") as f:
        muchii_sortate=[]
        v,m = [int(i) for i in f.readline().split()]
        for _ in range(v+1):
            mat.append([1000]*(v+1))
        for i in range (v+1):
            mat[i][i]=0
        for _ in range(m):
            x,y,val = [int(i) for i in f.readline().split()]
            mat[x][y] = val
            muchii_sortate.append((x,y))
            if not oriented:
                mat[y][x] = val
        pctControl=[False for i in range (v+1)]
        for i in (f.readline().split()):
            pctControl[int(i)]=True
    return mat,muchii_sortate,v,m

def colorareAdam(nod):
    global graf,n,m
    if (m>3*n-6):
        print("Graf neplanar")
        return
    q = deque()
    selectat=0
    q.append(nod)
    viz[nod]=1
    while (q):
        selectat=q.pop()
        for y in (graf[selectat]):
            takenCol[col[y]]=1
            if (col[selectat]==col[y]):
                urmCol(selectat)
            if (viz[y]==0):
                q.appendleft(y)
                viz[y]=1
    maxc=0
    for i in range (n+1):
        print(col[i])
        if (maxc<col[i]):
            maxc=col[i]
    print(str(maxc)+" colorabil")

def urmCol(nod):
    global col
    i=0
    while (takenCol[i]==1):
        i+=1
    col[nod]=1



raf,muchii_sortate,n,m=readmat()
takenCol=[0 for i in range (5)]
col =[0 for i in range (101)]
viz =[0 for i in range (101)]

