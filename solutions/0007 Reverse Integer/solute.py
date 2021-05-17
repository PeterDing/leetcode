# 0007 - Reverse Integer
#
# Road:
# see code
#
# Writing cost time 12min


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        is_neg = -x > 0
        x = abs(x)

        rev = 0
        while x != 0:
            remain = x % 10
            rev = rev * 10 + remain
            x = x // 10

        if is_neg:
            rev = -rev

        if -(1 << 31) <= rev <= ((1 << 31) - 1):
            return rev
        else:
            return 0
