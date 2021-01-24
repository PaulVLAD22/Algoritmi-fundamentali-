def keysort(a):
    return a[2]

def retclass(w):
    global classes
    for i in range(len(classes)):
        if w in classes[i]:
            return i
    return -1

def reuneste(u,v):
    global classes
    ui = retclass(u)
    vi = retclass(v)
    classes[ui].extend(classes.pop(vi))

def editdistance(s1,s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


file = "cluster_input.txt"
d = editdistance
words = []
with open(file) as f:
    k = int(f.readline())
    x = f.readline().replace("\n","")
    while x:
        words.append(x)
        x = f.readline().replace("\n","")

distances = []
lastindex = 0
for i in words:
    for j in words:
        if i > j: # and i != j
            distances.append((i,j,d(i,j)))
distances.sort(key = keysort)

classes = [[w] for w in words]
while len(classes) > k:
    while lastindex < len(distances):
        e = distances[lastindex]
        if retclass(e[0]) != retclass(e[1]):
            reuneste(e[0],e[1])
            break
        lastindex+=1
print(classes)
