class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_elements = 1
        count = 1
        
        for i in range(1,len(nums)):
            
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[unique_elements] = nums[i]
                unique_elements += 1

        return unique_elements
            



