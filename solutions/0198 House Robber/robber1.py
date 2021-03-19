def max_money(nums):
        m1, m2 = 0, 0

        for p in nums:
            t = m2
            m2 = max(m2, m1 + p)
            m1 = t

        return max(m1, m2)


nums = [1, 2, 3, 1]
print(max_money(nums))
