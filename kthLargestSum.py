# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return 0

        pq = []
        queue = deque()
        queue.append(root)

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

            heapq.heappush(pq, -level_sum)
        
        if len(pq) < k:
            
            return -1

        for _ in range(k - 1):

            heapq.heappop(pq)

        return -heapq.heappop(pq)



            