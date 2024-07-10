# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        
        self.flag = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def bsearch(curr):
            
            if not curr:
                return False

            left = bsearch(curr.left)
            right = bsearch(curr.right)
            
            mid = curr == p or curr == q
                
            if mid + right + left >= 2:
                self.flag = curr
                
            return mid or left or right
        
        bsearch(root)
        return self.flag
        
        