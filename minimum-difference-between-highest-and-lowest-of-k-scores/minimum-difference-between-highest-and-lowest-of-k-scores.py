class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = k - 1
        res = 1000000

        while j < len(nums):
            res = min(res,nums[j]-nums[i])
            i += 1
            j += 1
        
        return res
        