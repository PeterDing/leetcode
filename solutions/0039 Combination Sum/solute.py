# 0039 - Combination Sum
#
# Road:
# Backtrack andn stock:
#
# stock.push(e)
# backtrack(..)
# stock.pop()
#
# Writing cost time 18min

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sums = []
        find(candidates, target, sums, 0)
        return sums


def find(candidates, target, sums, idx, stock=[]):
    if target == 0:
        sums.append(list(stock))
        return

    for i, c in enumerate(candidates[idx:], idx):
        if target - c >= 0:
            stock.append(c)
            find(candidates, target - c, sums, i, stock)
            stock.pop()


a = Solution()
s = a.combinationSum([2, 3, 6, 7], target=7)
print(s)
