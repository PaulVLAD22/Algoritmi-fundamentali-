from collections import deque

def readlist(oriented = False, filename = "ex1.txt"):
    lists = {}
    with open(filename,"r") as f:
        v,m = [int(i) for i in f.readline().split()]
        for _ in range(m):
            x, y = [int(i) for i in f.readline().split()]
            if x in lists.keys():
                lists[x].append(y)
            else:
                lists[x] = [y]
            if not oriented:
                if y in lists.keys():
                    lists[y].append(x)
                else:
                    lists[y] = [x]
    return lists,v,m

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




L,n,m = readlist(oriented=True)
print(L)

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

print (circuit)
if (len(circuit)==0):
    print("NICIUN CIRCUIT")
# DEBUG