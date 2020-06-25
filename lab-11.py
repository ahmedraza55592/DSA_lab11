class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# making a method to insertNodeIn a Binary Search Tree

    def insertNodeInBST(self, data):

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

    # finding the maximum value in a BST

    def findmax(self):
        if self.right is None:
            self.val = self.data
            return f"{str(self.val)} is the maximum number"
        else: 
            return self.right.findmax()

    # finding the maximum value in a BST

    def findmin(self):
        if self.left is None:
            self.val = self.data
            return f"{str(self.val)} is minimum number"
        else:
            return self.left.findmin()

# making a method to delete a Node from Binary Search Tree




objectofNodeclass = Node(12)
objectofNodeclass.insertNodeInBST(6)
objectofNodeclass.insertNodeInBST(18)
objectofNodeclass.printTree()
print(objectofNodeclass.findNodeInBST(45))
print(objectofNodeclass.findNodeInBST(6))
print(objectofNodeclass.findmin())
print(objectofNodeclass.findmax())
# objectofNodeclass.minimumValueInBST()
objectofNodeclass.delNodeFromBST(6)
objectofNodeclass.printTree()
objectofNodeclass.delNodeFromBST(6)