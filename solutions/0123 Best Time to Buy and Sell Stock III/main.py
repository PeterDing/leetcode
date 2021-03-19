import math


def merge(ls):
    while len(ls) >= 3:
        c = ls.pop()
        b = ls.pop()
        a = ls.pop()

        if a <= b <= c:
            ls.append(a)
            ls.append(c)
        elif c <= b <= a:
            ls.append(a)
            ls.append(c)
        else:
            ls.append(a)
            ls.append(b)
            ls.append(c)
            break


def max_it(ls):
    if len(ls) < 2:
        return 0

    min_l = math.inf
    min_ls = []
    for i in ls[:-1]:
        min_l = min(min_l, i)
        min_ls.append(min_l)

    max_r = -math.inf
    max_rs = []
    for i in ls[::-1][:-1]:
        max_r = max(max_r, i)
        max_rs.append(max_r)
    max_rs = max_rs[::-1]

    m = 0
    for min_l, max_r in zip(min_ls, max_rs):
        if min_l > max_r:
            continue
        m = max(m, max_r - min_l)

    return m


class Solution:

    def maxProfit_slow(self, prices) -> int:
        ls = []
        for p in prices:
            ls.append(p)
            merge(ls)

        rs = 0
        for i in range(len(ls) + 1):
            r = max_it(ls[:i]) + max_it(ls[i:])
            rs = max(rs, r)

        return rs

    def maxProfit(self, prices) -> int:
        one_buy_price = math.inf
        one_buy_profit = 0

        two_buy_price = math.inf
        two_buy_profit = 0

        for p in prices:
            one_buy_price = min(one_buy_price, p)  # we use minimum price to buy 1st stock
            one_buy_profit = max(
                one_buy_profit, p - one_buy_price
            )  # sell 1st stock at highest price to get biggest profit

            two_buy_price = min(
                two_buy_price, p - one_buy_profit
            )  # we have get the profit of 1st stock, then using it to buy 2nd stock, minimum it as be lowest
            two_buy_profit = max(
                two_buy_profit, p - two_buy_price
            )  # sell 2nd stock at highest price to get biggest profit

        return two_buy_profit


print(Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
