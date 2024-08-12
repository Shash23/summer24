class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        
        for _ in nums:
            
            heapq.heappush(_, nums)
            
            if len(heap) > k:
                heapq.heappop(nums)
                
        return heap[0]
    
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:

        return heapq.nlargest(k, nums)[k-1]
    '''
    