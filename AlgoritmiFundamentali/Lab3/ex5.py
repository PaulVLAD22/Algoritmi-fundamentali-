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
def cmp(p1):
    return graf[p1[0]][p1[1]]
def kruskal(n):
    culoare = [i for i in range(n + 1)]
    acpm=[[] for i in range (n+1)]
    tata_acpm=[0 for i in range (n+1)]
    for p in muchii_sortate:
        if (culoare[p[0]]!=culoare[p[1]]):
            acpm[p[0]].append(p[1])
            tata_acpm[p[1]]=p[0]
            deSchimbat=culoare[p[0]]
            for i in range (1,n+1):
                if (culoare[i]==deSchimbat):
                    culoare[i]=culoare[p[1]]
            print(culoare)
    return tata_acpm,acpm



graf,muchii_sortate,n,m=readmat()
muchii_sortate=(sorted(muchii_sortate,key=cmp))
print(muchii_sortate)

tata_acpm,acpm=kruskal(n)

# CONTINUA PROBLEMA

