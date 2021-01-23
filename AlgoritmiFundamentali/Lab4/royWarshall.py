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
        pctControl=[False for i in range (v+1)]
        for i in (f.readline().split()):
            pctControl[int(i)]=True
    return mat,muchii_sortate,v,m

def royWarshall():
    global graf,n
    d = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for k in range (1,n+1):
        for i in range(1,n+1):
            for j in range (1,n+1):
                d[i][j]=d[i][j] or (d[i][k] and d[k][j])
    print(d)
graf,muchii_sortate,n,m=readmat(oriented=True)
royWarshall()