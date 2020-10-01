def preorder(root):
    if root is None:
        return
    print(root.info)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.info)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.info)
    inorder(root.right)

from collections import deque
def levelorder(root):
    if root is None:
        return
    result=[]
    q=deque()
    q.append(root)
    node=None
    while len(q)!=0:
        node=q.popleft()
        result.append(node.info)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    for i in  result:
        print(i)
