# 0005 - Longest Palindromic Substring
#
# Road:
# 1. search  <---(i)--->
# 2. search  <---(i)(i+1)--->
#
# Writing cost time 23min


class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxs = ""
        for i in range(len(s)):
            pal = self.findPal(s, i, i, min(i + 1, len(s) - i))
            print(i, pal)
            if len(pal) > len(maxs):
                maxs = pal

            if i != len(s) - 1:
                pal = self.findPal(s, i, i + 1, min(i + 1, len(s) - i - 1))
                print(i, pal)
                if len(pal) > len(maxs):
                    maxs = pal

        return maxs

    def findPal(self, s, left, right, length):
        for _ in range(length):
            if s[left] != s[right]:
                break

            left -= 1
            right += 1
        return s[left + 1 : right]


a = Solution()
a.longestPalindrome("babad")
