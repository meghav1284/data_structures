#class
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        
#tree traversal in DFS manner
#inorder

def printinorder(root):
    if root:
        printinorder(root.left)
        print root.val
        printinorder(root.right)
        
#preorder
def preorder(root):
    if root:
        print root.val
        preorder(root.left)
        preorder(root.right)
        
def post(root):
    if root:
        post(root.left)
        post(root.right)
        print root.val        
root=Node(1);
root.left=Node(2);
root.right=Node(3);
root.left.left=Node(4);
root.left.right=Node(5);
print 'Preorder';
preorder(root)
print 'inorder'
printinorder(root)
print 'Post order'
post(root)