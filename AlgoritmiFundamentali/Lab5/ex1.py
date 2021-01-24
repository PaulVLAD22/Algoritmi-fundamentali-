from collections import deque

def readmat(oriented = False, filename = "ex1.txt"):
    mat = []
    with open(filename,"r") as f:
        muchii_sortate=[]

        v =int(f.readline().split()[0])
        print(v)
        s,t=[int(i) for i in f.readline().split()]
        m=int(f.readline().split()[0])
        for _ in range(v+1):
            mat.append([0]*(v+1))
        for _ in range(m):
            x,y,fMax,fAct = [int(i) for i in f.readline().split()]
            mat[x][y] = (fMax,fAct)
            muchii_sortate.append((x,y))
            if not oriented:
                mat[y][x] = (fMax,fAct)

    return mat,muchii_sortate,v,m,s,t



graf,muchii_sortate,n,m,s,t=readmat(oriented=True)
