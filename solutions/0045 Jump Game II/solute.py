# 0045 - Jump Game II
#
# Road:
# Greedy:
# 1. ooooooooooooooo
#       i     j
# 2. find max_steps between [i+1, j+1]
# 3. set i = j, j = max_steps
#
# Writing cost time 17min


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        step = 0
        i = 0
        j = nums[i]

        while True:
            if j >= len(nums) - 1:
                return step + 1

            max_steps = 0
            for p in range(i + 1, j + 1):
                max_steps = max(p + nums[p], max_steps)

            step += 1
            i = j
            j = max_steps
