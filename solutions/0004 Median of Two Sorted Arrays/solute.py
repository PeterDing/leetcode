# 0004 - Median of Two Sorted Arrays
#
# Road:
# [ A ] [ B ]
# [ C ] [ D ]
# cat(A, C) < cat [B, D]
#
# Writing cost time 120min


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1) + len(nums2)
        if N == 1:
            return (nums1 + nums2)[0]

        # Let nums1 is longer than nums2
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        if len(nums2) == 0:
            return (nums1[len(nums1) // 2] + nums1[(len(nums1) - 1) // 2]) / 2

        is_even = (len(nums1) + len(nums2)) % 2 == 0
        half = (len(nums1) + len(nums2)) // 2

        p1 = half - len(nums2)
        p2 = half - p1
        while p1 < len(nums1) and p2 > 0:
            if nums1[p1] < nums2[p2 - 1]:
                p1 += 1
                p2 -= 1
            else:
                break

        if is_even:
            if p1 == 0:
                return (nums1[0] + nums2[-1]) / 2
            if p1 == len(nums1):
                return (nums1[-1] + nums2[0]) / 2
            if p2 == 0:
                return (nums1[p1 - 1] + min(nums1[p1], nums2[0])) / 2
            if p2 == len(nums2):
                return (max(nums1[p1 - 1], nums2[p2 - 1]) + nums1[p1]) / 2
            else:
                return (
                    max(nums1[p1 - 1], nums2[p2 - 1]) + min(nums1[p1], nums2[p2])
                ) / 2
        else:
            if p1 == 0:
                return nums1[0]
            if p2 == len(nums2):
                return nums1[p1]
            else:
                return min(nums1[p1], nums2[p2])


a = Solution()

l1 = [3]
l2 = [-1, -2]
s = a.findMedianSortedArrays(l1, l2)
print(s)
