import random

class disjointSet:
    def __init__(self, n):
        self.memo = [i for i in range(n)]
    
    def find(self, a):
        assert a < len(self.memo) and a >= 0
        while a != self.memo[a]:
            a = self.memo[a]
        return a
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.memo[root_a] = root_b
            return True
        else:
            return False

def random_tree(num_nodes, weight_low=1, weight_high=10):
    V = disjointSet(num_nodes)
    
    edges = []
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(weight_low, weight_high)
            heapq.heappush(edges, (weight, i, j))
    
    # ncc is number of connective component
    ncc = num_nodes
    tree = []
    while ncc > 1:
        weight, i, j = heapq.heappop(edges)
        if V.union(i, j):
            ncc -= 1
            tree.append([i, j, weight])
    return tree