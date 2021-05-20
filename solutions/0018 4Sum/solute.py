# 0018 - 4Sum
#
# Road:
# two_sum maps to indexes
#
# Writing cost time 32min

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        rs = set()
        maps = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sm = nums[i] + nums[j]
                key = target - sm
                if key in maps:
                    for two in maps[key]:
                        four = sorted([i, j] + list(two))
                        if len(set(four)) == 4:
                            rs.add(tuple(four))

                if sm in maps:
                    maps[sm].append([i, j])
                else:
                    maps[sm] = [[i, j]]

        return [list(j) for j in set([tuple(sorted(nums[i] for i in e)) for e in rs])]
