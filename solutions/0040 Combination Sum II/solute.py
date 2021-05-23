# 0040 - Combination Sum II
#
# Road:
# Backtrack:
# !!! At each time, there must be abs(target - c) <= abs(target),
# else c is too bigger, so missing it.
#
# Writing cost time 43min

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sums = []
        find(candidates, target, 0, sums)
        return sums


def find(candidates, target, idx, sums, stock=[]):
    if target == 0:
        sums.append(list(stock))
        return

    i = idx
    while i < len(candidates):
        c = candidates[i]

        # !!! c is too bigger
        if abs(target - c) > abs(target):
            return

        stock.append(c)
        find(candidates, target - c, i + 1, sums, stock)
        stock.pop()

        i += 1

        # Missing repeat
        while 0 < i < len(candidates) and candidates[i - 1] == candidates[i]:
            i += 1
            continue


a = Solution()
s = a.combinationSum2(
    [
        14,
        6,
        25,
        9,
        30,
        20,
        33,
        34,
        28,
        30,
        16,
        12,
        31,
        9,
        9,
        12,
        34,
        16,
        25,
        32,
        8,
        7,
        30,
        12,
        33,
        20,
        21,
        29,
        24,
        17,
        27,
        34,
        11,
        17,
        30,
        6,
        32,
        21,
        27,
        17,
        16,
        8,
        24,
        12,
        12,
        28,
        11,
        33,
        10,
        32,
        22,
        13,
        34,
        18,
        12,
    ],
    27,
)
print(s)
