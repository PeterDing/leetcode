# 0020 - Valid Parentheses
#
# Road:
#
# Writing cost time 3min


class Solution:
    def isValid(self, s: str) -> bool:
        stock = []

        for c in s:
            if not stock:
                stock.append(c)
                continue

            if stock[-1] == "(" and c == ")":
                stock.pop()
                continue
            if stock[-1] == "{" and c == "}":
                stock.pop()
                continue
            if stock[-1] == "[" and c == "]":
                stock.pop()
                continue

            stock.append(c)

        return not stock
