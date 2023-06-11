class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # queue = []
        # j = 0
        # n = len(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         queue.append(i)
        #         n -= 1
        #     elif queue != []:
        #         index = queue[j]
        #         j += 1
        #         queue.append(i)
        #         nums[index] = nums[i]

        unique_count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_count] = nums[i]
                unique_count += 1



        return unique_count

       