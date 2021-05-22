# 0034 - Find First and Last Position of Element in Sorted Array
#
# Road:
# Binary search
#
# !!! Elements can be repeated
#
# Writing cost time 10min


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        i = bin_search(nums, 0, len(nums) - 1, target)
        if i == -1:
            return [-1, -1]

        j = i

        while i > 0 and nums[i - 1] == nums[i]:
            i -= 1
        while j < len(nums) - 1 and nums[j] == nums[j + 1]:
            j += 1
        return [i, j]


def bin_search(nums, l, r, target):
    # !!! Edge condition
    if l > r or l < 0 or r > len(nums) - 1:
        return -1

    mid = (l + r) // 2
    if nums[mid] == target:
        return mid

    if nums[mid] < target:
        return bin_search(nums, mid + 1, r, target)
    else:
        return bin_search(nums, l, mid - 1, target)
