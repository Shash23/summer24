class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in intervals:

            # case where new interval hasn't been reached
            if i[1] < newInterval[0]:
                res.append(i)

            # case where inside the interval
            elif i[0] > newInterval[1]: # elif i[1] > newInterval[0]
                res.append(newInterval)
                newInterval = i 

            # case where new interval is over some intervals
            else:

                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])

        res.append(newInterval)

        return res






            
        