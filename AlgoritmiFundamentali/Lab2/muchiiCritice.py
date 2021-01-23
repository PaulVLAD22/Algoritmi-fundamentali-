def readmat(oriented = False, filename = "ex1.txt"):
    mat = []
    with open(filename,"r") as f:
        muchii_sortate=[]
        v,m = [int(i) for i in f.readline().split()]
        for _ in range(v+1):
            mat.append([0]*(v+1))
        for _ in range(m):
            x,y = [int(i) for i in f.readline().split()]
            mat[x][y] = 1
            if not oriented:
                mat[y][x] = 1
    return mat,v,m


def dfs(nod):
    global times,status,crit
    times += 1
    status[nod]=1#devine gray
    nrc=0 #nr copii
    dt[nod]=low[nod]=times
    for y in vecini[nod]:
        if (status[y]==0):
            tata[y]=nod
            nrc+=1
            dfs(y)
            low[nod]=min(low[nod],low[y])
            if (dt[nod]<=low[y]):
                crit[nod]=1
            if (dt[nod]<low[y]):
                print("Muchie Critica : "+str(nod)+" "+str(y)+"\n")
        if (status[y]==1):
            if (y!=tata[nod]): #xy muchie de intoarcere
                low[nod]=min(low[nod],dt[y])
    status[nod]=2
    return nrc


graf,n,m=readmat()
times=0#nr pasi
status= [0 for i in range (100)]
dt = [0 for i in range (100)]
tata = [0 for i in range (100)]
low = [ 0 for i in range (100)]
crit = [0 for i in range (100)] #vector caracteristic de noduri critice
vecini = [0 for i in range (100)]
s=int(input)
if (dfs(s)>1):
    crit[s]=1
else:
    crit[s]=0
print("Discovery Time: ")
for i in range (1,n+1):
    print(str(dt[i])+" ")
print("Lower:")
for i in range (1,n+1):
    print(str(low[i])+" ")
print("Noduri Critice: ")
for i in range (1,n+1):
    if (crit[i]==1):
        print(str(i)+" ")
    print("\n")



