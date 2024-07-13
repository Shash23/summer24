# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

        def dfs(node, curr_max):

            # check if curr node is greater
            if(node.val >= curr_max):
                self.count += 1

            # if right exists, go right
            if node.right:
                dfs(node.right, max(curr_max, node.val))

            # if left exists, go left
            if node.left:
                dfs(node.left, max(curr_max, node.val))

        self.count = 0
        dfs(root, -10000000000)
        return self.count
            

            


        