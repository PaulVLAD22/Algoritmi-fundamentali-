global color


# Initializer
def isBipartite(graph):
    global color
    for v in graph.keys():
        color[v] = -1

    for v in graph.keys():
        if (color[v] == -1):
            if (not setColor(graph, v, 0)):
                return False

    return True


# Recursive code
def setColor(graph, v, c):
    global color
    color[v] = c
    for w in graph[v]:
        if color[w] == -1:
            if setColor(graph, w, 1 - c) == False:
                return False
        else:
            if color[w] == c:
                return False

    return True


# Read information from file #
# input = open("A-small-practice-1.in", 'r')
input = open("ex1.txt", 'r')

nTestCases = input.readline().strip()

for iTestCase in range(int(nTestCases)):
    nPair = input.readline().strip()
    graph = {}
    for iPair in range(int(nPair)):
        pair = input.readline().replace('\n', '').split()
        if not pair[0] in graph:
            graph[pair[0]] = []
            graph[pair[0]].append(pair[1])
        else:
            graph[pair[0]].append(pair[1])

        if not pair[1] in graph:
            graph[pair[1]] = []
            graph[pair[1]].append(pair[0])
        else:
            graph[pair[1]].append(pair[0])

    color = {}
    global color

    res = False
    if (isBipartite(graph)):
        res = True

    print("Case #{iCase}: {res}".format(iCase=iTestCase + 1, res=("Yes" if isBipartite(graph) else "No")))

input.close()