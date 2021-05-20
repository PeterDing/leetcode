# 0017 - Letter Combinations of a Phone Number
#
# Road:
# Recursion
#
# Writing cost time 15min


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        maps = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 1:
            return list(maps[digits])

        all_combines = []
        for c in maps[digits[0]]:
            all_combines.extend(
                [c + sub for sub in self.letterCombinations(digits[1:])]
            )
        return all_combines
