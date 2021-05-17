# 0008 - String to Integer (atoi)
#
# Road:
# see code
#
# Writing cost time 12min


class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        is_neg = False
        started = False
        for c in s:
            if not started:
                if c == " " and not num:
                    continue
                if c == "0" and not num:
                    started = True
                    continue
                if c == "-" and not num:
                    is_neg = not is_neg
                    started = True
                    continue
                if c == "+" and not num:
                    started = True
                    continue

            started = True
            uni = ord(c) - ord("0")
            if 0 <= uni < 10:
                num = num * 10 + uni
            else:
                break

        if not num:
            return 0

        if is_neg:
            num = -num

        if num < -(1 << 31):
            return -(1 << 31)
        if num > (1 << 31) - 1:
            return (1 << 31) - 1
        return num
