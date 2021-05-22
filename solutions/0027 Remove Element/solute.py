# 0027 - Remove Element
#
# Road:
# only store val which is not the target
#
# Writing cost time 2min


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for e in nums:
            if e != val:
                nums[p] = e
                p += 1

        return p
