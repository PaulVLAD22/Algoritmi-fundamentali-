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

#IA TE DUPA SEMINAR


graf,muchii_sortate,n,m=readmat()

