class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.root = None

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

# making a method to delete a Node from Binary Search Tree

    def delNodeFromBST(self, delNode):
        if delNode < self.data:
            print ("check1")
            if self.left is not None:
                print ("check1.1")
                print (delNode)
                print (self.data)
                if delNode == self.data:
                    print ("check1.2")
                    data = None
                return f"{str(delNode)} has been deleted"
            return self.left.delNodeFromBST(delNode)
        if delNode > self.data:
            print ("check2")
            if self.right is not None:
                print ("check2.1")
                if delNode == self.data:
                    print ("check2.2")
                    data = None
                return f"{str(delNode)} not Found"
            return self.right.delNodeFromBST(delNode)
        if delNode == self.data:
            print ("check2")
            self.data = self.findmin()
            return f"{str(delNode)} not Found"
        # else:
        #     print(f"{str(self.data)} has been deleted")

objectofNodeclass = Node(12)
objectofNodeclass.createBST(6)
objectofNodeclass.createBST(18)
objectofNodeclass.printTree()
print(objectofNodeclass.findNodeInBST(45))
print(objectofNodeclass.findNodeInBST(6))
print(objectofNodeclass.findmin())
print(objectofNodeclass.findmax())
objectofNodeclass.delNodeFromBST(12)
objectofNodeclass.printTree()