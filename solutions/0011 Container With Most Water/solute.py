# 0011 - Container With Most Water
#
# Road:
# Small width needs larger height
#
# Writing cost time 45min


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        water = 0

        while i < j:
            water = max(water, min(height[i], height[j]) * (j - i))

            # small width needs larger height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return water
