# 0038 - Count and Say
#
# Road:
# two pointers
#
# Writing cost time 7min


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        said = "1"
        for _ in range(n - 1):
            said = say(said)
        return said


def say(s):
    said = ""

    # s[i:j+1] has same elements
    i = 0
    j = 0
    count = 0
    while j < len(s):
        if s[i] == s[j]:
            count += 1
            j += 1
        else:
            said = said + str(count) + s[i]
            i = j
            count = 0

    if count:
        said = said + str(count) + s[i]

    return said
