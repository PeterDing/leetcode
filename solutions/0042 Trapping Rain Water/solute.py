# 0042 - Trapping Rain Water
#
# Road:
# I. Find left_max and right_max
# II. l_max -> <- r_max
#
# Writing cost time 6min


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        m = 0
        for h in height:
            m = max(h, m)
            left_max.append(m)

        right_max = []
        m = 0
        for h in height[::-1]:
            m = max(h, m)
            right_max.append(m)
        right_max.reverse()

        water = 0
        for l, r, h in zip(left_max, right_max, height):
            water += min(l, r) - h

        return water

    def trap2(self, height: List[int]) -> int:
        """At trap(), left_max is ascend, right_max is descend"""

        if len(height) < 3:
            return 0

        l_max = height[0]
        r_max = height[-1]
        l = 1
        r = len(height) - 2
        water = 0
        while l <= r:
            if height[l] > l_max:
                l_max = height[l]
            if height[r] > r_max:
                r_max = height[r]

            if l_max > r_max:
                water += r_max - height[r]
                r -= 1
            else:
                water += l_max - height[l]
                l += 1

        return water
