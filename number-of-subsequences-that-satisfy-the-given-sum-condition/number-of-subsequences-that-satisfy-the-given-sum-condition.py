class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums) - 1
        nums.sort()
        sol = 0
        while i <= j:
            while i <= j and  (nums[i] + nums[j]) > target:
                j -= 1
            if i <= j:
                sol += 1<<(j-i)
            i += 1

        return sol%(10**9 +7)
