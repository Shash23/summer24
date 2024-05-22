from collections import Counter
import heapq
from typing import List

class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # don't forget base case
        if(k == len(nums)):
            return nums

        # takes O(n)
        freqs = Counter(nums)

        return heapq.nlargest(k, freqs.keys(), key = freqs.get)


        





        

        
        