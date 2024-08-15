def inOrder(root, ) -> Node:
    
    ans = None
    while root:
        if root.val > p.val:
            ans = root
            root = root.left
        else:
            root = root.right
    return ans
        