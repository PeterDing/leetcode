# 0031 - Next Permutation
#
# Road:
# 1. find first slip
# 2. find minimum number at right which is larger than nums[i-1]
# and swap them
# 3. reverse nums[i:]
#
# Writing cost time 40min


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            return nums

        # 1. find first slip
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                break

        # if nums = [n-1, n-2, ..., 0]
        if nums[i - 1] > nums[i] and i - 1 == 0:
            nums.reverse()
            return

        # 2. find minimum number at right which is larger than nums[i-1]
        # and swap them
        j = i
        while j < len(nums):
            if nums[i - 1] < nums[j]:
                j += 1
            else:
                break
        j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # 3. reverse nums[i:]
        nums[i:] = nums[i:][::-1]


a = Solution()

nums = [3, 2, 1]
for _ in range(6):
    a.nextPermutation(nums)
    print(nums)
