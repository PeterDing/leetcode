# 0012 - Integer to Roman
#
# Road:
# Split 10 base:
# e.g. 1994 -> 1 9 9 4
#
# Writing cost time 25min


class Solution:
    def intToRoman(self, num: int) -> str:
        maps = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        r = ""
        base = 1
        while num > 0:
            remain = num % (10 ** base)
            # uni the leftest number of remain
            uni = remain // (10 ** (base - 1))
            if remain in maps:
                r = maps[remain] + r
            else:
                if remain < 5 * 10 ** (base - 1):
                    # 0 < uni < 5, so uni
                    r = maps[10 ** (base - 1)] * uni + r
                else:  # 5 < uni < 9, so uni - 5
                    r = (
                        maps[10 ** (base - 1) * 5]
                        + maps[10 ** (base - 1)] * (uni - 5)
                        + r
                    )
            base += 1
            num -= remain

        return r
