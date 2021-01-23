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

def floydWarshall():
    global graf,n
    d=[[0 for j in range (n+1)] for i in range (n+1)]
    p= [[0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range (1,n+1):
        for j in range(1,n+1):
            d[i][j]=graf[i][j]
            if (graf[i][j]==1000):
                p[i][j]=0
            else:
                p[i][j]=i
    for k in range (1,n+1):
        for i in range (1,n+1):
            for j in range (1,n+1):
                if (d[i][j]>d[i][k]+d[k][j]):
                    d[i][j]=d[i][k]+d[k][j]
                    p[i][j]=p[k][j]
    print(d)
    print(p)



graf,muchii_sortate,n,m=readmat(oriented=True)
floydWarshall()