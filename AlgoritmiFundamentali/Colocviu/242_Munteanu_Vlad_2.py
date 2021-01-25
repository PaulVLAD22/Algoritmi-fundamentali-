from collections import deque
#a)

#pentru a afla drumul si costul drumului pe care l poate face calatorul
# pana la cel mai indepartata nod din graf, folosim algoritmul djkistra pentru
#a calcula distantele si vectorul de tati apoi luam cel mai mare drum mai mic
# ca b. Pentru drum , mergem de la nodul ales pana la s pe vectorul de tati
#Complexitatea este data de algoritmul lui Dijkstra = O(m*log n)


# b)
#folosim algoritmul multimilor albe, negre si gri pentru a detecta daca exista
#circuite si, cand gasim unul ii calculam costul adunand costurile muchiilor,
#daca este mai mic sau egal cu b este bun circuitul si se pastreaza intr-o
#lista.

#algoritmul merge pentru primul exemplu dat la calator
#pentru al doilea b-ul nu afiseaza
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
        b=int(f.readline().split()[0])
        s=int(f.readline().split()[0])
    return mat,muchii_sortate,v,m,b,s


def dijkstra(s,n,d,tata,graf):
    d[s]=0
    tata[s]=0
    q = deque()
    for i in range (1,n+1):
        q.appendleft(i)
    while (q):
        d_minim = 1000
        d_minim_index = 0
        for i in range(len(q)):
            if (d[q[i]] < d_minim):
                d_minim = d[q[i]]
                d_minim_index = i
        nod_actual = q[d_minim_index]
        q.remove(nod_actual)
        for j in range (1,n+1):
            if (graf[nod_actual][j]!=0):
                if (d[j]>graf[nod_actual][j]+d[nod_actual]):
                    d[j]=graf[nod_actual][j]+d[nod_actual]
                    tata[j]=nod_actual

def dfs(s):
    global L,graf,b,circuitCorect,tata
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
                circuit=[]
                nod_actual=s
                while (nod_actual!=tata[x]):
                    circuit.append(nod_actual)
                    nod_actual=tata[nod_actual]
                costCircuit=0
                circuit=circuit[::-1]
                for i in range (len(circuit)):
                    costCircuit+=graf[circuit[0]][circuit[1]]
                if (costCircuit<=b):
                    circuitCorect=circuit

    blacks.append(s)
    if(s in greys):
        greys.remove(s)


graf,muchii_sortate,n,m,b,s=readmat(oriented=True)

d=[1000 for i in range (n+1)]
tata=[0 for i in range (n+1)]

#a)
dijkstra(1,n,d,tata,graf)

print(d,tata)

a= sorted(d)
a.sort(reverse=True)

nod_v=0
for i in range (1,n+1):
    if (a[i]!=1000 and a[i]<=b):
        print("a)")
        nod_v = d.index(a[i])
        print(nod_v)
        break
drum=[]
while (nod_v!=tata[s]):
    drum.append(nod_v)
    nod_v=tata[nod_v]

print(drum[::-1])

#b)
print("b)")
L={}
for i in range (n+1):
    for j in range(n+1):
        if (graf[i][j]!=0):
            if (L.get(i)==None):
                L[i]=[j]
            else:
                L[i].append(j)

# algoritmul multimilor albe negre si gri
viz = [0 for i in range(n + 1)]
tata = [0 for i in range(n + 1)]
d = [0 for i in range(n + 1)]
whites=[i for i in range (1,n+1)]
whites.remove(s)
viz[s]=1
greys=[s]
blacks=[]
circuit=[]
circuitCorect=[]
dfs(s)

while (whites):
    nod=whites.pop()
    viz[nod]=1
    greys.append(nod)
    tata[nod]=-1
    dfs(nod)

print(circuitCorect)