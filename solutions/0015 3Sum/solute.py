# 0015 - 3Sum
#
# Road:
# one + two sum
# 1. sort
# 2.
#   l -> <- r
#   if l + r < target:
#       l += 1
#   else:
#       r -= 1
#
# Writing cost time 44min

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        if len(nums) == 3 and sum(nums) == 0:
            return [nums]

        nums.sort()

        rs = []

        i = 0
        for i in range(len(nums) - 2):
            # !!! Skipping repeat
            if i == 0 or nums[i - 1] != nums[i]:
                if nums[i] > 0:
                    break

                l = i + 1
                r = len(nums) - 1

                while l < r:
                    if nums[i] == -(nums[l] + nums[r]):
                        rs.append([nums[i], nums[l], nums[r]])

                        # !!! Skipping repeat
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        l += 1
                        r -= 1
                    else:
                        if nums[l] + nums[r] < -nums[i]:
                            l += 1
                        else:
                            r -= 1

        return [list(e) for e in rs]


a = Solution()
a.threeSum([0, 0, 0])
