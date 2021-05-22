# 0028 - Implement strStr()
#
# Road:
# KMP or force
#
# Writing cost time 106min


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "":
            if needle == "":
                return 0
            else:
                return -1

        if needle == "":
            return 0

        # Force
        # for i in range(len(haystack) - len(needle) + 1):
        #     if haystack[i : i + len(needle)] == needle:
        #         return i
        # return -1

        # KMP
        pmt = gen_partial_match_table(needle)

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    return i - j

                i += 1
                j += 1
            else:
                if i > len(haystack) - len(needle) + 2:
                    break
                if j == 0:
                    i += 1
                else:
                    j = pmt[j - 1]

        return -1


def gen_partial_match_table(needle: str):
    table = [0] * len(needle)

    i = 1
    j = 0
    while i < len(needle):
        if needle[i] == needle[j]:
            table[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                table[i] = 0
                i += 1
            else:
                j = table[j - 1]

    return table


a = Solution()
i = a.strStr("aabaaabaaac", "aabaaac")
print(i)
