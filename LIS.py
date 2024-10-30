class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # [10,9,2,5,3,7,101,18]
        # 8
        n = len(nums)
        ans = []
        ans.append(nums[0])
        # 10

        for i in range(1, n):

            if nums[i] > ans[-1]:

                ans.append(nums[i])

            else:

                lp = 0
                rp = len(ans) - 1
                # 3x

                while lp < rp:

                    mid = (lp + rp) // 2

                    if ans[mid] < nums[i]:

                        lp = mid + 1
                    
                    else:

                        rp = mid

                ans[lp] = nums[i]
                # 9, 2 5, 2 3 7 101, 

        return len(ans)
        