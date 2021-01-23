from collections import deque

def readmat(oriented = False, filename = "ex1.txt"):
    mat = []

    with open(filename,"r") as f:
        muchii_sortate=[]
        v,m = [int(i) for i in f.readline().split()]
        for _ in range(v+1):
            mat.append([0]*(v+1))
        gradeInt = [0 for i in range(v + 1)]
        for _ in range(m):
            x,y,val= [int(i) for i in f.readline().split()]
            mat[x][y] = val
            muchii_sortate.append((x,y))
            gradeInt[y]+=1
            if not oriented:
                mat[y][x] = val
    return mat,muchii_sortate,v,m,gradeInt

def sortateTopologica():
    global gradeInt,graf
    sortare=[]

    #graf orientat
    q = deque()
    #adaugam varfuri cu grad interior =0
    for i in range (1,n+1):
        if (gradeInt[i]==0):
            q.appendleft(i)
    while (q):
        i=q.pop()
        print(i)
        sortare.append(i)
        for j in range (1,n+1):
            if(graf[i][j]!=0):
                gradeInt[j]-=1
                if (gradeInt[j]==0):
                    q.appendleft(j)
    return sortare



graf,muchii_sortate,n,m,gradeInt=readmat()
sortare=sortateTopologica()
print(sortare)

