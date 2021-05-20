# 0022 - Generate Parentheses
#
# Road:
# backtrack:
# If we have one of these parenthesis as p,
# then, p[:i] can add next '(' if l_remain > 0 and l_remain <= r_remain,
# or ')' if r_remain > 0 and l_remain < r_remain.
#
# Writing cost time 60min

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        gen_parens("", n, n, parens)
        return parens


def gen_parens(paren, l, r, parens=[]):
    if l + r == 0:
        parens.append(paren)
        return

    if l > 0 and l <= r:
        gen_parens(paren + "(", l - 1, r, parens)

    if r > 0 and l < r:
        gen_parens(paren + ")", l, r - 1, parens)

    return parens


a = Solution()
s = a.generateParenthesis(1)
print(s)
