# 0003 - Longest Substring Without Repeating Characters
#
# Road:
# if
# [. . . o . . .]o
# then
#         [. . . o]
# special:
# a b b a
#     | |
#     | |-> to 0
#     |-> p1 is here, so p1 must be > 0
#
# . are each different
#
# Writing cost time 70min


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        p1 = 0
        p2 = 0
        cache = {}
        max_len = 0
        while p2 < len(s):
            index = cache.get(s[p2])
            cache[s[p2]] = p2
            p2 += 1
            if index is not None:
                # case: 'abba'
                p1 = max(index + 1, p1)
            max_len = max(max_len, p2 - p1)

        return max_len
