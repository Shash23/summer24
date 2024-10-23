# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return 0

        queue = deque()
        queue.append(root)
        level_sums = []

        while queue:

            length = len(queue)
            level_sum = 0

            for _ in range(length):

                node = queue.popleft()
                level_sum += node.val

                if node.left:

                    queue.append(node.left)
                
                if node.right:

                    queue.append(node.right)

            level_sums.append(level_sum)

        # update each node's value
        
        queue.append(root)
        idx = 1

        root.val = 0 # root does not have cousins

        while queue:

            length = len(queue) 

            for _ in range(length):

                node = queue.popleft()

                sib_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)

                if node.left:
                    node.left.val = level_sums[idx] - sib_sum
                    queue.append(node.left)
                if node.right:
                    node.right.val = level_sums[idx] - sib_sum
                    queue.append(node.right)

            idx += 1

        return root




        




        