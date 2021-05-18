# 0014 - Longest Common Prefix
#
# Road:
# skipping
#
# Writing cost time 7min


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            c = ""
            is_same = True
            for s in strs:
                if i < len(s):
                    if not c:
                        c = s[i]
                else:
                    is_same = False
                    break

                if s[i] != c:
                    is_same = False
                    break

            if not is_same:
                break

            i += 1

        return strs[0][:i]
