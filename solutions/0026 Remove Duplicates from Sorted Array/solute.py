# 0026 - Remove Duplicates from Sorted Array
#
# Road:
# 3 pointers
# p: next different element
# i-1: pre element
# i: next element
# if nums[i - 1] != nums[i], nums[i] is a new element
#
# Writing cost time 4min


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        p = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[p] = nums[i]
                p += 1

        return p
