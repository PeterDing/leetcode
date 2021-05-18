# 0016 - 3Sum Closest
#
# Road:
# like 3Sum, but no need to skip repeat elements
#
# Writing cost time 73min

from typing import List
import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        if len(nums) == 3:
            return sum(nums)

        nums.sort()

        s = 0
        min_dist = math.inf
        for i in range(len(nums) - 2):
            t = target - nums[i]

            l = i + 1
            r = len(nums) - 1

            dist = min_dist
            while l < r:
                dist = nums[l] + nums[r] - t
                if dist == 0:
                    return dist + target

                # !!! No remove repeat
                # e.g.
                #   if [..., 1, 1, 1, ...], target = 3.
                #            ------- can be missing
                #
                # while l < r - 1 and nums[l] == nums[l + 1]:
                #     l += 1
                # while l + 1 < r and nums[r - 1] == nums[r]:
                #     r -= 1

                if abs(dist) < min_dist:
                    min_dist = abs(dist)
                    s = dist + target

                if dist < 0:
                    l += 1
                else:
                    r -= 1

        return int(s)


a = Solution()
s = a.threeSumClosest([-1, 0, 1, 1, 55], 3)
print(s)
