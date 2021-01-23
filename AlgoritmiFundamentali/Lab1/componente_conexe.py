from collections import deque

with open("ex1.txt") as f:
    n, m = [int(i) for i in f.readline().split()]
    lists = [[] for _ in range(n+1)]
    print(n)
    for _ in range(m):
        x, y = [int(i) for i in f.readline().split()]
        lists[x].append(y)
        lists[y].append(x)
# LISTE DE LISTe

noduri = [0 for i in range(n+1)] # lista unde determin componenta fiecaruia

current_component = 1
print(lists)
print(noduri)
# E BF pana cand nu mai sunt elemente nevizitate
while 0 in noduri[1:]:
    i = noduri.index(0,1)
    q = deque()
    q.append(i)
    noduri[i] = current_component
    while q:
        current = q.popleft()
        for j in lists[current]:
            if noduri[j] == 0:
                noduri[j] = current_component
                q.append(j)
    current_component +=1
print('-'*100)
print(noduri)
for i in range(1,max(noduri)+1):
    print('-'*100)
    print(i)
    for j in range(1,n+1):
        if noduri[j] == i:
            print(j,end=" ")
    print()
