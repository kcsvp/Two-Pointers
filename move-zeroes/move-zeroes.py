class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_p = []
        j = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_p.append(i)
            elif zero_p != []:
                index = zero_p[j]
                nums[index] = nums[i]
                nums[i] = 0
                zero_p.append(i)
                j += 1