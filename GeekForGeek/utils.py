import random


def getLength(number):

    if number == 0:
        return 1

    numDigits, aNumber = 0, abs(number)

    while aNumber > 0:
        aNumber //= 10
        numDigits += 1

    numDigits += int(number < 0)

    return numDigits


def printMatrix(matrix, sep=' ', name=None):

    digitMatrix = [[getLength(number) for number in row] for row in matrix]
    maxLength = max([max(row) for row in digitMatrix])

    formatter = lambda i, j: ' ' * (maxLength - digitMatrix[i][j]) + str(matrix[i][j])

    rows, cols = len(matrix), len(matrix[0])
    matrixStr = '\n'.join([' '.join([formatter(i, j) for j in range(cols)]) for i in range(rows)])

    if name is not None:
        hLength = maxLength * len(matrix[0])
        prefix = '=' * (hLength // 2) + f' {name} ' + '=' * (hLength // 2)
        print(f'\n{prefix} START')
        print(matrixStr)
        print(f'{prefix} END\n')
    else:
        print(matrixStr)


# ======================== Binary Tree ======================== START
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
# A tree dictionary should look like `data: [left, right]`.
treeDict = {
    1: [2, 9],
    2: [4, None],
    9: [5, 7],
    4: [8, 19],
    7: [20, 11],
    8: [30, None],
    19: [40, 50]
}
'''

# class BTree:
#     def __init__(self, treeData):
#         if treeData
        
        
def getTree(treeArr):
    root = Node(treeArr[0])
    nodes = [root]
    i = 1
    while len(nodes) > 0:
        new_nodes = []
        for node in nodes:
            if i < len(treeArr):
                if treeArr[i] != 'N':
                    node.left = Node(treeArr[i])
                    new_nodes.append(node.left)
                i += 1
            else:
                break
            if i < len(treeArr):
                if treeArr[i] != 'N':
                    node.right = Node(treeArr[i])
                    new_nodes.append(node.right)
                i += 1
            else:
                break
        nodes = new_nodes
    return root


def getTree(treeDict, root):
    if root is None:
        return None
    node = Node(root)
    if root not in treeDict:
        return node
    else:
        l, r = treeDict[root]
    
    node.left = getTree(treeDict, l)
    node.right = getTree(treeDict, r)
    return node


def preOrder(root, result):
    if root is None:
        return
    result.append(root.data)
    preOrder(root.left, result)
    preOrder(root.right, result)

    
def inOrder(root, result):
    if root is None:
        return
    inOrder(root.left, result)
    result.append(root.data)
    inOrder(root.right, result)
    
    
def postOrder(root, result):
    if root is None:
        return
    postOrder(root.left, result)
    postOrder(root.right, result)
    result.append(root.data)
# ======================== Binary Tree ======================== END