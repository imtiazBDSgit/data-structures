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

