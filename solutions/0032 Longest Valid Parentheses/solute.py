# 0032 - Longest Valid Parentheses
#
# Road:
# Stock
#
# Writing cost time 19min


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stock = []

        max_len = 0
        for i, c in enumerate(s):
            if not stock:
                stock.append((i, c))
                continue

            j, p = stock[-1]
            if p == "(" and c == ")":
                stock.pop()
                # !!! no need
                # max_len = max(max_len, i - j + 1)
                continue
            else:
                stock.append((i, c))
                max_len = max(max_len, i - j - 1)
                continue

        # !!! The edge conditions
        if stock:
            # from start of s
            j, _ = stock[0]
            max_len = max(max_len, j)

            # from end of s
            j, _ = stock[-1]
            max_len = max(max_len, len(s) - 1 - j)
        else:
            return len(s)

        return max_len


a = Solution()
l = a.longestValidParentheses("(()()(")
print(l)
