# 0033 - Search in Rotated Sorted Array
#
# Road:
# Stock
#
# Writing cost time 43min


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bin_search(nums, 0, len(nums) - 1, target)


def bin_search(nums, l, r, target):
    # !!! Edge condition
    if l > r or l < 0 or r > len(nums) - 1:
        return -1

    mid = (l + r) // 2
    if nums[mid] == target:
        return mid

    if nums[mid] < nums[r]:
        if nums[mid] < target:
            if target <= nums[r]:
                return bin_search(nums, mid + 1, r, target)
            else:
                return bin_search(nums, l, mid - 1, target)
        else:
            return bin_search(nums, l, mid - 1, target)
    else:  # nums[mid] > nums[r]
        if nums[mid] < target:
            return bin_search(nums, mid + 1, r, target)
        else:
            if nums[l] <= target:
                return bin_search(nums, l, mid - 1, target)
            else:
                return bin_search(nums, mid + 1, r, target)


a = Solution()
a.search([1, 3], 0)
