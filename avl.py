class avl_treenode:
    def __init__(self,value):
        self.value= value
        self.left= None
        self.right= None
        self.height= 0

node= avl_treenode(10)
print(node.value)
print(node.left)
print(node.right)

def get_max(a,b):
    if a>b:
        return a
    return b

def  get_height(root):
    if root== None:
        return -1
    if root.left== None and root.right== None:
        return 0
    htr= get_height(root.right)
    htl=  get_height(root.left)
    height= 1+ get_max(htr, htl)
    return height

def get_balance(root):
    return (get_height(root.left)- get_height(root.right))         


def single_left_rotation(p):
    lc= p.left
    p.left= lc.right
    lc.right= p
    p.height= get_height(p)
    lc.heught= get_height(lc) 

def single_right_rotation(p):
    rc= p.right
    p.right= rc.left
    rc.left= p
    p.height= get_height(p)
    rc.heught= get_height(rc)

def double_left_right_rotation(p):
    p.right= single_left_rotation(p.left)
    return single_right_rotation(p)

def double_right_left_rotation(p):
    p.left= single_right_rotation(p.right)
    return single_left_rotation(p)

def insert(root,value):
    if root== None: 
        newNode= avl_treenode(value)
        return newNode
    if value< root.value:
        root.left= insert(root.left, value)
        if get_balance(root)==2 :
            if value< root.left.value:
                return single_right_rotation(root)
            return double_left_right_rotation(root)
    elif value> root.value:
        root.right= insert(root.right, value)
        if get_balance(root)==-2:
            if value> root.right.value:
                return single_left_rotation(root)
            return double_right_left_rotation(root)

    root.height= get_height(root)
    return root

def inorder_successor(node):
    while node.left!= None:
        node=node.left
    return node

def delete(root,value):
    if root== None:
       print('Root not found')
       return 
    if value < root.value:
        root.left= delete(root.left, value)
    if value > root.value:
        root.right= delete(root.right, value)
    else:
        if root.left== None:
            return root.right
        if root.right== None:
            return root.left 
        temp= inorder_successor(root.right)
        root.value= temp.value
        root.right= delete(root.right, value)
    return root     

    if root== None:
        return root
        

