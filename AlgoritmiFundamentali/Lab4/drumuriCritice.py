from _collections import deque

def read1(oriented = False, filename = "ex1.txt"):
    with open(filename, "r") as f:
        n=int(f.readline().split()[0])
        precede = [[] for i in range(n + 1)]
        durata=[int(x) for x in f.readline().split()]
        gradeInt=[0 for i in range (n+1)]
        m=int(f.readline().split()[0])
        for i in range (m):
            x,y = [int(i) for i in f.readline().split()]
            precede[x].append(y)
            gradeInt[x]+=1
    return n,precede,durata,gradeInt,m



def drumuriCritice():
    global q, graf, n, m, gradeInt, drumCritic, durata, precede
    inProcess=[0 for i in range (n+1)]# activitate inceputa

    previousTask=[0 for i in range (n+1)] #task ul anterior
    earliestEndTime =[1000 for i in range (n+1)] #cel mai devreme terminat un task
    projectDuration=0 # ce se cere


    lastTask=0
    nod=0
    while (q):
        nod=q.pop()
        inProcess[nod]=True
        for i in range (len(precede[nod])):
            nod_urm = precede[nod][i]
            if (not inProcess[nod_urm]):
                gradeInt[nod_urm]-=1
                if (earliestEndTime[nod_urm]<durata[nod_urm]+earliestEndTime[nod]):
                    previousTask[nod_urm]=nod
                    earliestEndTime[nod_urm]=durata[nod_urm]+earliestEndTime[nod]
                if (gradeInt[nod_urm]):
                    q.append(nod_urm)

    for i in range (1,n+1):
        if (projectDuration<earliestEndTime[i]):
            projectDuration=earliestEndTime[i]
            lastTask=i
    nod =lastTask
    while (nod):
        drumCritic.append(nod)
        nod=previousTask[nod]
    return precede,inProcess,durata,previousTask,earliestEndTime,projectDuration





n,precede,durata,gradeInt,m=read1()
q=deque()

for i in range (1,n+1):
    q.append(i)
drumCritic=[]

precede,inProcess,durata,previousTask,earliestEndTime,projectDuration = drumuriCritice()

print(projectDuration)

for i in range (len(drumCritic)-1,0):
    print(drumCritic[i]+" ")


