def max_money(nums):
    m1, m2 = 0, 0

    for p in nums:
        t = m2
        m2 = max(m2, m1 + p)
        m1 = t

    return max(m1, m2)


def max_money_cycle(nums):
    if len(nums) == 1:
        return nums[0]
    r1 = max_money(nums[1:])
    r2 = max_money(nums[:-1])
    return max(r1, r2)


nums = [1, 2, 3, 1]
print(max_money_cycle(nums))
