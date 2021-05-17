# 0010 - Regular Expression Matching
#
# Road:
# DP
# 1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
# 2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
# 3, If p.charAt(j) == '*':
#    here are two sub conditions:
#                1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
#                2   if p.charAt(j-1) == s.charAt(i) or p.charAt(j-1) == '.':
#                               dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a
#                            or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
#                            or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
#
# Writing cost time 127min


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(len(p)):
            if p[j] == "*" and dp[0][j - 1]:
                dp[0][j + 1] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]

                if p[j - 1] == "*":
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        dp[i][j] = (
                            dp[i][j - 2]  # a* match empty
                            or dp[i][j - 1]  # a* match one a
                            or dp[i - 1][j]  # a* match multi a
                        )
                    else:
                        dp[i][j] = dp[i][j - 2]  # a* match empty

        return dp[-1][-1]
