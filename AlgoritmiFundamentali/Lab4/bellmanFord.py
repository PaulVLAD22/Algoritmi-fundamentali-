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

def bellmanFord(s):
    global d,tata,graf
    d[s]=0
    for i in range (1,n):
        print(i)
        for p in muchii_sortate:
            if (d[p[0]]+graf[p[0]][p[1]]<d[p[1]]):
                d[p[1]]=d[p[0]]+graf[p[0]][p[1]]
                tata[p[1]]=p[0]
    print(d)
#ciclu negativ => am repetat pasi de n+1 ori, am fost la toate nodurile si la unul am fost inca odata
#care sunt nodurile => de fiecare data avem un contor cu de cate ori am mers in nodul respectiv in bellanford
graf,muchii_sortate,n,m=readmat(oriented=True)

d=[1000 for i in range (n+1)]
tata=[0 for i in range (n+1)]
bellmanFord(1)
