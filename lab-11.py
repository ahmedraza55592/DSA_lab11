class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# making a method to create a Binary Search Tree

    def createBST(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# making a method to find a Node in Binary Search Tree

    def findNodeInBST(self, searchNo):
        if searchNo < self.data:
            if self.left is None:
                return f"{str(searchNo)} not Found"
            return self.left.findNodeInBST(searchNo)
        elif searchNo > self.data:
            if self.right is None:
                return f"{str(searchNo)} not Found"
            return self.right.findNodeInBST(searchNo)
        else:
            print(f"{str(self.data)} is Found")



    # making a method to Print the Tree

    def printTree(self):
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()
        print(self.data)

    # finding the maximum and minimum value in a BST

    def findmax(self):
        if self.right is None:
            self.val = self.data
            return f"{str(self.val)} is the maximum number"
        else: 
            return self.right.findmax()

    def findmin(self):
        if self.left is None:
            self.val = self.data
            return f"{str(self.val)} is minimum number"
        else:
            return self.left.findmin()

    # making a method to find a node with minimum value in Binary Search Tree

    # def minimumValueInBST(self):
    #     if (self.data.left is not None):
    #         self.data = self.data.left
    #         return minimumValueInBST()

    #     return self.data

    # def maximumValueInBST(self):
    #     if (self.current == None):
    #         return float('-inf')

    #     res = self.node.data
    #     lres = maximumValueInBST(self.node.left)
    #     rres = maximumValueInBST(self.node.right)
    #     if (lres > res):
    #         res = lres
    #     if (rres > res):
    #         res = rres
    #     return res


objectofNodeclass = Node(12)
objectofNodeclass.createBST(6)
objectofNodeclass.createBST(18)
objectofNodeclass.printTree()
print(objectofNodeclass.findNodeInBST(45))
print(objectofNodeclass.findNodeInBST(6))
print(objectofNodeclass.findmin())
print(objectofNodeclass.findmax())
# objectofNodeclass.minimumValueInBST()