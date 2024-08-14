def isValidBST(root, low, high):
    
    if not root:
        return True
    
    if not (node.val > low and node.val < high):
        return False
    
    return (valid(node.left, low, node.val) and valid(node.right, node.val, high))

return isValidBST(root, float("-inf"), float("inf"))


    
    