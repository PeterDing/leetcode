# 0013 - Roman to Integer
#
# Road:
# Roman number is a sum
#
# Writing cost time 12min


class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        i = 0
        num = 0
        while i < len(s):
            if s[i : i + 2] in maps:
                num += maps[s[i : i + 2]]
                i += 2
                continue
            else:
                num += maps[s[i]]
                i += 1

        return num
