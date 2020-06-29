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

def deleteNodeinBST(root, key): 
  
    # Base Case 
    if root is None: 
        return root  
  
    if key < root.data: 
        root.left = deleteNodeinBST(root.left, key) 
  
    elif(key > root.data): 
        root.right = deleteNodeinBST(root.right, key) 
  
    else: 
          
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        temp = minValueNode(root.right) 
  
        root.data = temp.data 
  
        root.right = deleteNodeinBST(root.right , temp.data) 
  
  
    return root           

# making a method to delete a Node from Binary Search Tree

    # def delNodeFromBST(self, delNode):
    #     if delNode < self.data:
    #         print ("check1")
    #         if self.left is not None:
    #             print ("check1.1")
    #             print (delNode)
    #             print (self.data)
    #             if delNode == self.data:
    #                 print ("check1.2")
    #                 data = None
    #             return f"{str(delNode)} has been deleted"
    #         return self.left.delNodeFromBST(delNode)
    #     if delNode > self.data:
    #         print ("check2")
    #         if self.right is not None:
    #             print ("check2.1")
    #             if delNode == self.data:
    #                 print ("check2.2")
    #                 data = None
    #             return f"{str(delNode)} not Found"
    #         return self.right.delNodeFromBST(delNode)
    #     if delNode == self.data:
    #         print ("check2")
    #         self.data = self.findmin()
    #         return f"{str(delNode)} not Found"
    #     # else:
    #     #     print(f"{str(self.data)} has been deleted")

objectofNodeclass = Node(12)
objectofNodeclass.insertNodeInBST(6)
objectofNodeclass.insertNodeInBST(18)
objectofNodeclass.printTree()
print(objectofNodeclass.findNodeInBST(45))
print(objectofNodeclass.findNodeInBST(6))
print(objectofNodeclass.findmin())
print(objectofNodeclass.findmax())
print("All nodes in BST")
objectofNodeclass.printTree()
deleteNodeinBST(objectofNodeclass, 6)
print("6 Deleted from BST")
objectofNodeclass.printTree()
deleteNodeinBST(objectofNodeclass, 18)
print("18 deleted from BST and now node has only one element")
objectofNodeclass.printTree()