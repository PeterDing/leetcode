# 0030 - Substring with Concatenation of All Words
#
# Road:
# Force
#
# Writing cost time 39min


from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        wn = len(words)
        maps = {}
        for w in words:
            if w in maps:
                maps[w] += 1
            else:
                maps[w] = 1

        n = len(words[0])
        indexes = []
        for i in range(len(s) - wn * n + 1):
            ok = find(s, maps, i, n, wn)
            if ok:
                indexes.append(i)

        return indexes


def find(s, maps, idx, n, wn):
    # n is the length of word

    maps = dict(**maps)

    for i in range(idx, idx + wn * n, n):
        w = s[i : i + n]
        if maps.get(w):
            maps[w] -= 1
        else:
            return False
    return True


a = Solution()
indexes = a.findSubstring("foobarfoobar", ["foo", "bar"])
print(indexes)
