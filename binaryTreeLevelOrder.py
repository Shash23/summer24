# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = [] # store the answer
        
        if not root:
            return result
        
        level = 0
        queue = deque()
        queue.append(root)

        while queue:

            result.append([])

            for i in range(len(queue)): # it goes for the length of the queue,     
                
                node = queue.popleft()
                
                result[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            level += 1
            
        return result

        
        