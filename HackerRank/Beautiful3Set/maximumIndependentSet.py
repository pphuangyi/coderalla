#!/usr/bin/env python3.7

import random
import sys
    
def randomSimpleGraph(n, p=.2):
    adjList = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(i + 1, n):
            k = random.uniform(0, 1)
            if k < p:
                adjList[i].append(j)
                adjList[j].append(i)

    return adjList


def getMaximumInd(vertices, adjList):
    maxInd = set()

    V = set(range(len(vertices)))

    # while len(V) > 0:
    for i, node in enumerate(V):
        # print(i)
        W, indSet = V.copy(), set()

        # print(node)
        while True:
            # print(f'\t{node}')
            indSet.add(node)
            # print(f'\t{W}, {adjList[node]}')
            W -= adjList[node]
            # print(f'\t{W}')
            if len(W) > 0:
                node = W.pop()
            else:
                break
        
        if len(indSet) > len(maxInd):
            maxInd = indSet
        
        # print(indSet)
    
    return [vertices[i] for i in maxInd]         
    

def getKSets(n, k):
    if k == 1:
        return [[n]]

    results = []
    for i in range(n + 1):
        R = getKSets(n - i, k - 1)
        results += [r + [i] for r in R]
        
    return results


def getAdjList(n, k, vertices):


    pre_adjList = [{i: set() for i in range(n + 1)} for l in range(k)]
    for v_idx, v in enumerate(vertices):
        for l, i in enumerate(v):
            pre_adjList[l][i].add(v_idx)
    
    adjList = {}
    for v_idx, v in enumerate(vertices):
        al = set()
        for l, i in enumerate(v):
            al.update(pre_adjList[l][i])
        adjList[v_idx] = al 

    return adjList


if __name__ == '__main__':

    n = int(sys.argv[1])
    k = int(sys.argv[2])

    vertices = getKSets(n, k)
    # for i, v in enumerate(vertices):
    #     print(f'{i}: {v}')    
    adjList = getAdjList(n, k, vertices)
    # for k, v in adjList.items():
    #     print(f'{k}: {v}')
    maxInd = getMaximumInd(range(len(vertices)), adjList)
    print(len(maxInd))

    # vertices = getKSets(n, k)
    # for i, v in enumerate(vertices):
    #     print(f'{i}: {v}')    

    # adjList = getAdjList(n, k, vertices)
    # for k, v in adjList.items():
    #     print(f'{k}: {v}')
    # maxInd = getMaximumInd(vertices, adjList)    
    # print(len(maxInd))
    # for v in maxInd:
    #     print(v)


