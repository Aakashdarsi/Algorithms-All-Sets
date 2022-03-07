# Two check whether ttwo trees are identical or not



def identical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.data == root2.data and identical(root1.left,root2.left) and identical(root1.right,root2.right):
            return True
    
    return False 

    