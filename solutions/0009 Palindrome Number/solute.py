# 0009 - Palindrome Number
#
# Road:
# num == ? rev
#
# Writing cost time 16min


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if -x > 0:
            return False

        num = x

        rev = 0
        while x != 0:
            remain = x % 10
            rev = rev * 10 + remain
            x = x // 10

        return num == rev
