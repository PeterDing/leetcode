# 0712 - Minimum ASCII Delete Sum for Two Strings

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings) | [solution](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solution/)


-----------

<p>Given two strings <code>s1, s2</code>, find the lowest ASCII sum of deleted characters to make two strings equal.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> s1 = "sea", s2 = "eat"
<b>Output:</b> 231
<b>Explanation:</b> Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> s1 = "delete", s2 = "leet"
<b>Output:</b> 403
<b>Explanation:</b> Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
</pre>
</p>

<p><b>Note:</b>
<li><code>0 < s1.length, s2.length <= 1000</code>.</li>
<li>All elements of each string will have an ASCII value in <code>[97, 122]</code>.</li> 
</p>

-----------


## Similar Problems

- [Hard] [Edit Distance](edit-distance)

- [Medium] [Longest Increasing Subsequence](longest-increasing-subsequence)

- [Medium] [Delete Operation for Two Strings](delete-operation-for-two-strings)




## Solution:

[TOC]


#### Approach #1: Dynamic Programming [Accepted]

**Intuition and Algorithm**

Let `dp[i][j]` be the answer to the problem for the strings `s1[i:], s2[j:]`.

When one of the input strings is empty, the answer is the ASCII-sum of the other string.  We can calculate this cumulatively using code like `dp[i][s2.length()] = dp[i+1][s2.length()] + s1.codePointAt(i)`.

When `s1[i] == s2[j]`, we have `dp[i][j] = dp[i+1][j+1]` as we can ignore these two characters.

When `s1[i] != s2[j]`, we will have to delete at least one of them.  We'll have `dp[i][j]` as the minimum of the answers after both deletion options.

The solutions presented will use *bottom-up* dynamic programming.

**Python**
```python
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]

        for i in xrange(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for j in xrange(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in xrange(len(s1) - 1, -1, -1):
            for j in xrange(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                   dp[i][j+1] + ord(s2[j]))

        return dp[0][0]
```

**Java**
```java
class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int[][] dp = new int[s1.length() + 1][s2.length() + 1];

        for (int i = s1.length() - 1; i >= 0; i--) {
            dp[i][s2.length()] = dp[i+1][s2.length()] + s1.codePointAt(i);
        }
        for (int j = s2.length() - 1; j >= 0; j--) {
            dp[s1.length()][j] = dp[s1.length()][j+1] + s2.codePointAt(j);
        }
        for (int i = s1.length() - 1; i >= 0; i--) {
            for (int j = s2.length() - 1; j >= 0; j--) {
                if (s1.charAt(i) == s2.charAt(j)) {
                    dp[i][j] = dp[i+1][j+1];
                } else {
                    dp[i][j] = Math.min(dp[i+1][j] + s1.codePointAt(i),
                                        dp[i][j+1] + s2.codePointAt(j));
                }
            }
        }
        return dp[0][0];
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(M*N)$$, where $$M, N$$ are the lengths of the given strings.  We use nested for loops: each loop is $$O(M)$$ and $$O(N)$$ respectively.

* Space Complexity: $$O(M*N)$$, the space used by `dp`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
