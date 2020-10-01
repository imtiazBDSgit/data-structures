from binaryTree import Node
from binaryTree import BinaryTree
from Traversals import preorder,postorder,inorder,levelorder
if __name__=="__main__":
    print("enter the number of elements in tree:")
    t=int(input())
    arr=[]
    for i in range(t):
        print("enter the next element in the tree")
        arr.append(int(input()))
    bT=BinaryTree()
    for e in arr:
        bT.create(e)
    
    ##### testing preorder tree traversal
    print(" Pre Order traversal of tree is :" )
    # test case : 1 2 5 3 6 4  output : 1 2 5 3 6 4
    preorder(bT.root)
    
    print(" Post order traversal of tree is :")
    postorder(bT.root)

    print(" In order traversal of tree is :")
    inorder(bT.root)
    
    print("Level order traversal of tree is:")
    levelorder(bT.root)
    



    
