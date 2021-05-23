# 0044 - Wildcard Matching
#
# Road:
# dp:
# if s[i - 1] == p[j - 1] or p[j - 1] == "?":
#     dp[i][j] = dp[i - 1][j - 1]
# else:
#     if p[j - 1] == "*":
#         dp[i][j] = (
#             dp[i - 1][j - 1]
#             or dp[i][j - 1]  # empty
#             or dp[i - 1][j]  # multi
#         )
#
# Writing cost time 25min


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[0][0] = True

        for i in range(len(p)):
            if p[i] == "*":
                dp[0][i + 1] = True
            else:
                break

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == "*":
                        dp[i][j] = (
                            dp[i - 1][j - 1]
                            or dp[i][j - 1]  # empty
                            or dp[i - 1][j]  # multi
                        )

        return dp[-1][-1]
