# 0940 - Distinct Subsequences II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming | [Leetcode](https://leetcode.com/problems/distinct-subsequences-ii) | [solution](https://leetcode.com/problems/distinct-subsequences-ii/solution/)


-----------

<p>Given a string <code>S</code>, count the number of distinct, non-empty subsequences of <code>S</code> .</p>

<p>Since the result may be large, <strong>return the answer modulo <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;abc&quot;</span>
<strong>Output: </strong><span id="example-output-1">7</span>
<span><strong>Explanation</strong>: The 7 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, &quot;ab&quot;, &quot;ac&quot;, &quot;bc&quot;, and &quot;abc&quot;.</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;aba&quot;</span>
<strong>Output: </strong><span id="example-output-2">6
</span><strong>Explanation</strong>: The 6 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;ab&quot;, &quot;ba&quot;, &quot;aa&quot; and &quot;aba&quot;.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;aaa&quot;</span>
<strong>Output: </strong><span id="example-output-3">3
</span><strong>Explanation</strong>: The 3 distinct subsequences are &quot;a&quot;, &quot;aa&quot; and &quot;aaa&quot;.
</pre>
</div>
</div>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>S</code> contains only lowercase letters.</li>
	<li><code>1 &lt;= S.length &lt;= 2000</code></li>
</ol>

<div>
<p>&nbsp;</p>

<div>
<div>&nbsp;</div>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition and Algorithm**

Even though the final code for this problem is very short, it is not very intuitive to find the answer.  In the solution below, we'll focus on finding all subsequences (including empty ones), and subtract the empty subsequence at the end.

Let's try for a dynamic programming solution.  In order to not repeat work, our goal is to phrase the current problem in terms of the answer to previous problems.  A typical idea will be to try to count the number of states `dp[k]` (distinct subsequences) that use letters `S[0], S[1], ..., S[k]`.

Naively, for say, `S = "abcx"`, we have `dp[k] = dp[k-1] * 2`.  This is because for `dp[2]` which counts `("", "a", "b", "c", "ab", "ac", "bc", "abc")`, `dp[3]` counts all of those, plus all of those with the `x` ending, like `("x", "ax", "bx", "cx", "abx", "acx", "bcx", "abcx")`.

However, for something like `S = "abab"`, let's play around with it.  We have:

* `dp[0] = 2`, as it counts `("", "a")`
* `dp[1] = 4`, as it counts `("", "a", "b", "ab")`;
* `dp[2] = 7` as it counts `("", "a", "b", "aa", "ab", "ba", "aba")`;
* `dp[3] = 12`, as it counts `("", "a", "b", "aa", "ab", "ba", "bb", "aab", "aba", "abb", "bab", "abab")`.

We have that dp[3]` counts `dp[2]`, plus `("b", "aa", "ab", "ba", "aba")` with `"b"` added to it.  Notice that `("", "a")` are missing from this list, as they get double counted.  In general, the sequences that resulted from putting `"b"` the last time (ie. `"b", "ab"`) will get double counted.

This insight leads to the recurrence:

`dp[k] = 2 * dp[k-1] - dp[last[S[k]] - 1]`

The number of distinct subsequences ending at `S[k]`, is twice the distinct subsequences counted by `dp[k-1]` (all of them, plus all of them with S[k] appended), minus the amount we double counted, which is `dp[last[S[k]] - 1]`.

<iframe src="https://leetcode.com/playground/XejQAwZ4/shared" frameBorder="0" width="100%" height="463" name="XejQAwZ4"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(N)$$.  It is possible to adapt this solution to take $$O(1)$$ space.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
