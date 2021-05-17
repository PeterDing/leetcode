# 0001 - Two Sum
#
# Road:
# target - elem1 = elem2 as mapping A to B
#
# Writing cost time 11min

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i, elem in enumerate(nums):
            indexes = cache.get(target - elem)
            if not indexes:
                if elem in cache:
                    cache[elem].append(i)
                else:
                    cache[elem] = [i]
                continue
            else:
                j = indexes[0]
                if i < j:
                    return [i, j]
                else:
                    return [j, i]
