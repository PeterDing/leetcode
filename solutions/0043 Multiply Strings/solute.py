# 0043 - Multiply Strings
#
# Road:
# Use a list to store number
#
# Writing cost time 22min


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = []
        for i in range(len(num1)):
            n1 = ord(num1[-1 - i]) - ord("0")
            for j in range(len(num2)):
                n2 = ord(num2[-1 - j]) - ord("0")

                add(m, i + j, n1 * n2)

        m.reverse()
        i = 0
        while i < len(m) - 1 and m[i] == 0:
            i += 1

        m = m[i:]

        return "".join([str(n) for n in m])


def add(m, idx, n):
    if len(m) == idx:
        m.append(0)

    s = m[idx] + n

    r = s % 10
    m[idx] = r

    if s > 9:
        add(m, idx + 1, s // 10)


a = Solution()
m = a.multiply("0", "501")
print(m)
