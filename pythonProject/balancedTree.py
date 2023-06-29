# binarytree - implements tree for event feedback

# author: Mahad Ghani
# instructor: Karla (CS-302)

class treeNode:
    def __init__(self, key, event):
        self.left = None
        self.right = None
        self.val = key
        self.event = event
 
def insert(root, key, event):
    if root is None:
        return treeNode(key, event)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key, event)
        else:
            root.left = insert(root.left, key, event)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print("Event: ", root.event)
        print("Rating: ", root.val)
        print("")
        inorder(root.right)