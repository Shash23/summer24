def isBalanced(self, root: Optional[TreeNode]) -> bool:

    def helper(root):
        
        if not root:
            return True, 0
        
        left_balanced, left_height = helper(root.left)
        
        if not left_balanced:
            return False, 0
        
        right_balanced, right_height = helper(root.right)
        
        if not right_balanced:
            return False, 0
        
        return (abs(left_height - right_height) <= 1), 1 + max(left_height, right_height)
    
    if not root:
        return True
    
    if not root.right and not root.left:
        return True
    
    return helper(root)[0]
    
    

            