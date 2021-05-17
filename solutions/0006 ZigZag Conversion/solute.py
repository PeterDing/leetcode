# 0006 - ZigZag Conversion
#
# Road:
# indexes:
# 0     0
# 1  1     1
# 2           2
#
# Writing cost time 12min


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        idx = list(range(numRows)) + list(range(numRows - 2, 0, -1))

        rs = [""] * numRows

        for i, c in enumerate(s):
            j = idx[i % len(idx)]
            rs[j] += c

        return "".join(rs)
