# 0823 - Binary Trees With Factors

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/binary-trees-with-factors) | [solution](https://leetcode.com/problems/binary-trees-with-factors/solution/)


-----------

<p>Given an array of unique integers, each integer is strictly greater than 1.</p>

<p>We make a binary tree using these integers&nbsp;and each number may be used for any number of times.</p>

<p>Each non-leaf node&#39;s&nbsp;value should be equal to the product of the values of it&#39;s children.</p>

<p>How many binary trees can we make?&nbsp; Return the answer <strong>modulo 10 ** 9 + 7</strong>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>A = [2, 4]</code>
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [4, 2, 2]</code></pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>A = [2, 4, 5, 10]</code>
<strong>Output:</strong> <code>7</code>
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]</code>.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;=&nbsp;1000</code>.</li>
	<li><code>2 &lt;=&nbsp;A[i]&nbsp;&lt;=&nbsp;10 ^ 9</code>.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Dynamic Programming [Accepted]

**Intuition**

The largest value `v` used must be the root node in the tree.  Say `dp(v)` is the number of ways to make a tree with root node `v`.

If the root node of the tree (with value `v`) has children with values `x` and `y` (and `x * y == v`), then there are `dp(x) * dp(y)` ways to make this tree.

In total, there are $$\sum_{\substack{x * y = v}} \text{dp}(x) * \text{dp}(y)$$ ways to make a tree with root node `v`.

**Algorithm**

Actually, let `dp[i]` be the number of ways to have a root node with value `A[i]`.

Since in the above example we always have `x < v` and `y < v`, we can calculate the values of `dp[i]` in increasing order using dynamic programming.

For some root value `A[i]`, let's try to find candidates for the children with values `A[j]` and `A[i] / A[j]` (so that evidently `A[j] * (A[i] / A[j]) = A[i]`).  To do this quickly, we will need `index` which looks up this value: if `A[k] = A[i] / A[j]`, then index[A[i] / A[j]] = k`.

After, we'll add all possible `dp[j] * dp[k]` (with `j < i, k < i`) to our answer `dp[i]`.  In our Java implementation, we carefully used `long` so avoid overflow issues.

```java
class Solution {
    public int numFactoredBinaryTrees(int[] A) {
        int MOD = 1_000_000_007;
        int N = A.length;
        Arrays.sort(A);
        long[] dp = new long[N];
        Arrays.fill(dp, 1);

        Map<Integer, Integer> index = new HashMap();
        for (int i = 0; i < N; ++i)
            index.put(A[i], i);

        for (int i = 0; i < N; ++i)
            for (int j = 0; j < i; ++j) {
                if (A[i] % A[j] == 0) { // A[j] is left child
                    int right = A[i] / A[j];
                    if (index.containsKey(right)) {
                        dp[i] = (dp[i] + dp[j] * dp[index.get(right)]) % MOD;
                    }
                }
            }

        long ans = 0;
        for (long x: dp) ans += x;
        return (int) (ans % MOD);
    }
}
```

```python
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in xrange(i):
                if x % A[j] == 0: #A[j] will be left child
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD
```

</playground>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `A`.  This comes from the two for-loops iterating `i` and `j`.

* Space Complexity: $$O(N)$$, the space used by `dp` and `index`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
