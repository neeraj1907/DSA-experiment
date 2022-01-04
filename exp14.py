class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)

        if self.root == None:
            self.root = newNode
            return newNode

        else:
            newNode = Node(value)
            temp =  self.root
            node = self.root

            while node:
                if temp.data>value:
                    temp = node
                    node = node.left 
                else:
                    temp = node
                    node = node.right

            if temp.data>value:
                temp.left = newNode
            else:
               temp.right = newNode

            return newNode    

    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(root.data)  
            self.printTree(root.right)

    def treeHeight(self, root):
        if(root==None):
            return 0 
        
        leftTree = self.treeHeight(root.left) 
        rightTree = self.treeHeight(root.right) 
        return max(leftTree, rightTree)+1
    
def size(root):
    return 1 + size(root.left) + size(root.right) if root else 0   

def checkSize(root, n):
    if root is None:
        return False
 
    if 2 * size(root) == n:
        return True
 
    return checkSize(root.left, n) or checkSize(root.right, n)

def splitTree(root):
    n = size(root)
    return (n % 2 == 0) and checkSize(root, n)
 

#      5
#    /  \
#   2    6
# /  \  / \
#    4     9
#           \
#           10 

Bt = BinaryTree()
Bt.insert(5)
Bt.insert(6)
Bt.insert(2)
Bt.insert(9)
Bt.insert(10)
Bt.insert(4)

if splitTree(Bt.root):
    print('The binary tree can be split')
else:
    print('The binary tree cannot be split')

