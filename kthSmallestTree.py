def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
    def inOrder(node: Optional[TreeNode]) -> List[int]:
        
        return inOrder(node.left) + [node.val] + inOrder(node.right) if node else []
    
    return inOrder(root)[k-1]
    
    