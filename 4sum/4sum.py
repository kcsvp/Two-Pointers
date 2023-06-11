class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        sol = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1,len(nums)):
                if j > i + 1 and nums[j]==nums[j-1]:
                    continue
                t1 = target - nums[i] - nums[j]
                l,r = j +1, len(nums) -1
                while l < r:
                    if nums[l] + nums[r] > t1:
                        r -= 1
                    elif nums[l] + nums[r] < t1:
                        l += 1
                    else:
                        if sol == [] or ( sol != [] and sol[-1] != [nums[i],nums[j],nums[l],nums[r]]):
                            sol.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1

        return sol

