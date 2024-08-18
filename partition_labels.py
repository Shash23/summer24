class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashmap = {}
        hashset = set()
        
        for idx, i in enumerate(s):
            
            if not i in hashset:
                hashset.add(i)
                hashmap[i] = [idx, s.rfind(i)]
                
        tmp = []
        start, end = 0, 0
        
        for idx, char in enumerate(s):
            
            end = max(end, hashmap[char][1])

            if idx == end:
                
                tmp.append(end - start + 1)
                start = idx + 1
                
        return tmp
                