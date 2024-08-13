# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = Nonea# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traverse(curr):

            if not root:
                return None

            # Does the left subtree contain either p or q?
            left_trav = lowestCommonAncestor(curr.left, p, q)

            # Does the right subtree contain either p or q?
            right_trav = lowestCommonAncestor(curr.right, p, q)

            # Is the current node itself either p or q?
            pa = curr == p or curr == q

            if pa + left_trav + right_trav >= 2:
                self.ans = curr

            return pa 
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
        
        