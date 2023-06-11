class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sol = []
        for k in range(len(nums)-1,1,-1):
            if k + 1 < len(nums) and nums[k] == nums[k+1]:
                continue
            target = -nums[k]
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > target:
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    entry = sorted([nums[k],nums[i],nums[j]])
                    if sol == [] or sol[-1] != entry:
                        sol.append(entry)
                    i += 1
                    j -= 1
        return sol

        