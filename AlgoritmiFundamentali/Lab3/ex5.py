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
    acpm=[]
    tata_acpm=[0 for i in range (n+1)]
    for p in muchii_sortate:
        if (culoare[p[0]]!=culoare[p[1]]):
            acpm.append((p[0],p[1]))
            tata_acpm[p[1]]=p[0]
            deSchimbat=culoare[p[0]]
            for i in range (1,n+1):
                if (culoare[i]==deSchimbat):
                    culoare[i]=culoare[p[1]]
    return tata_acpm,acpm

def costAPCM(apcm):
    cost=0
    for p in apcm:
        cost+=graf[p[0]][p[1]]
    return cost

def dfs(s):
    if (L.get(s)!=None):
        for x in L[s]:
            if (viz[x]==0 and not(x in blacks)):
                whites.remove(x)
                viz[x]=1
                greys.append(x)
                tata[x]=s
                d[x]=d[s]+1

                dfs(x)
            elif (viz[x]==1 and not(x in blacks)):
                print(s,x,blacks)
                print(tata[1:])
                nod_actual=s
                while (nod_actual!=tata[x]):
                    circuit.append(nod_actual)
                    nod_actual=tata[nod_actual]

    blacks.append(s)
    if(s in greys):
        greys.remove(s)


graf,muchii_sortate,n,m=readmat()
muchii_sortate=(sorted(muchii_sortate,key=cmp))
print(muchii_sortate)

tata_acpm,acpm=kruskal(n)
print(acpm)
# CONTINUA PROBLEMA

noua_muchie=(3,5,4)

graf[noua_muchie[0]][noua_muchie[1]]=noua_muchie[2]
muchii_sortate.append((noua_muchie[0],noua_muchie[1]))
muchii_sortate=(sorted(muchii_sortate,key=cmp))


tata_acpm2,acpm2=kruskal(n)

print(acpm2)

#a)
acpm.append((noua_muchie[0],noua_muchie[1]))

L={}
for p in acpm:
    if (L.get(p[0])==None):
        L[p[0]]=[p[1]]
    else:
        L[p[0]].append(p[1])
s=1
viz = [0 for i in range(n + 1)]
tata = [0 for i in range(n + 1)]
d = [0 for i in range(n + 1)]
whites=[i for i in range (1,n+1)]
whites.remove(s)
viz[s]=1
greys=[s]
blacks=[]
circuit=[]
dfs(s)

while (whites):
    nod=whites.pop()
    viz[nod]=1
    greys.append(nod)
    tata[nod]=-1
    dfs(nod)
print("CICUITUL:")
print (circuit)
maxim=0
ma1=0
m2=0
for x in circuit:
    for y in circuit:
        if (graf[x][y]>maxim):
            maxim=graf[x][y]
            m1=x
            m2=y

print(maxim,m1,m2)



#b)
print(costAPCM(acpm),costAPCM(acpm2))



