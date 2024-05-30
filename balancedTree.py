def height(self, root: Optional[TreeNode]) -> int:
    
    if root is None:
        return -1
    
    return max(height(root.left) + height(root.right)) + 1


def isBalanced(self, root: Optional[TreeNode]) -> bool:

    if root is None:
        
        return True
    
    if(abs(self.height(root.right) - self.height(root.left)) > 1):
        
        return False
    
    else:
        return isBalanced(root.right) and isBalanced(root.left)
    
    
    

            