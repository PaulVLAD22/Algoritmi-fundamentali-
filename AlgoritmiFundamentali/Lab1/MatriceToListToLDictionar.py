def matriceToList(matrice,n,m):
    lista=[[] for i in range (n+1)]
    for i in range (len(matrice)):
        for j in range (len(matrice[i])):
            if (matrice[i][j]!=0):
                lista[i].append(j)
    return lista

def listaToDictionar(lista,n,m):
    dictionar={}
    for i in range (len(lista)):
        for y in lista[i]:
            if (dictionar.get(i)==None):
                dictionar[i]=[y]
            else:
                dictionar[i].append(y)
    return dictionar

def dictionarToMatrice(dictionar,n,m):
    matrice=[[0 for i in range (n+1)] for j in range(n+1)]
    for k in dictionar.keys():
        for y in dictionar[k]:
            matrice[k][y]=1
    return matrice