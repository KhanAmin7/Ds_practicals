# inorder, preorder, postorder
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None 
        self.val=key

def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)
def printPosteorder(root):
    if root:
        printPosteorder(root.left)
        printPosteorder(root.right)
        print(root.val)
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Pre order traversal of tree")
printPreorder(root)
print("\nPost order traversal of tree ")  
printPosteorder(root)
print("\nIn-Order Traversal Of Tree:")  
printInorder(root)