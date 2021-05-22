# 0035 - Search Insert Position
#
# Road:
# Binary search. Consider edge conditions
#
# Writing cost time 22min

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bin_search(nums, 0, len(nums) - 1, target)


def bin_search(nums, l, r, target):
    # Edge condition
    if l > r:
        return l
    if l == r:
        if nums[l] < target:
            return l + 1
        else:
            return l

    # !!! mid can be equal to l when l+1 == r
    # So, in next recurse, l can be > r
    mid = (l + r) // 2
    if nums[mid] < target:
        return bin_search(nums, mid + 1, r, target)
    else:
        return bin_search(nums, l, mid - 1, target)


a = Solution()
i = a.searchInsert([3, 5, 7, 9, 10], 5)
print(i)
