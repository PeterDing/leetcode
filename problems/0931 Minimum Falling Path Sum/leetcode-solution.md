# 0931 - Minimum Falling Path Sum

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/minimum-falling-path-sum) | [solution](https://leetcode.com/problems/minimum-falling-path-sum/solution/)


-----------

<p>Given a <strong>square</strong> array of integers <code>A</code>, we want the <strong>minimum</strong> sum of a <em>falling path</em> through <code>A</code>.</p>

<p>A falling path starts at any element in the first row, and chooses one element from each row.&nbsp; The next row&#39;s choice must be in a column that is different from the previous row&#39;s column by at most one.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,2,3],[4,5,6],[7,8,9]]</span>
<strong>Output: </strong><span id="example-output-1">12</span>
<strong>Explanation: </strong>
The possible falling paths are:
</pre>

<ul>
	<li><code>[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]</code></li>
	<li><code>[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]</code></li>
	<li><code>[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]</code></li>
</ul>

<p>The falling path with the smallest sum is <code>[1,4,7]</code>, so the answer is <code>12</code>.</p>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length == A[0].length &lt;= 100</code></li>
	<li><code>-100 &lt;= A[i][j] &lt;= 100</code></li>
</ol>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

This problem has an optimal substructure, meaning that the solutions to subproblems can be used to solve larger instances of this problem.  This makes dynamic programming an ideal candidate.

Let `dp(r, c)` be the minimum total weight of a falling path starting at `(r, c)` and reaching the bottom row.

Then, `dp(r, c) = A[r][c] + min(dp(r+1, c-1), dp(r+1, c), dp(r+1, c+1))`, and the answer is $$\min\limits_c \text{dp}(0, c)$$.

**Algorithm**

Usually, we would make an auxillary array `dp` to cache intermediate values `dp(r, c)`.  However, this time we will use `A` to cache these values.  Our goal is to transform the values of `A` into the values of `dp`.

We process each row, starting with the second last.  (The last row is already correct.)  We set `A[r][c] = min(A[r+1][c-1], A[r+1][c], A[r+1][c+1])`, handling boundary conditions gracefully.

Let's look at the recursion a little more to get a handle on why it works.  For an array like `A = [[1,1,1],[5,3,1],[2,3,4]]`, imagine you are at `(1, 0)` (`A[1][0] = 5`).  You can either go to `(2, 0)` and get a weight of 2, or `(2, 1)` and get a weight of 3.  Since 2 is lower, we say that the minimum total weight at `(1, 0)` is `dp(1, 0) = 5 + 2` (5 for the original `A[r][c]`.)

After visiting `(1, 0)`, `(1, 1)`, and `(1, 2)`, `A` [which is storing the values of our `dp`], looks like `[[1,1,1],[7,5,4],[2,3,4]]`.  We do this procedure again by visiting `(0, 0)`, `(0, 1)`, `(0, 2)`.  We get `A = [[6,5,5],[7,5,4],[2,3,4]]`, and the final answer is `min(A[0]) = 5`

<iframe src="https://leetcode.com/playground/zERoz5Wa/shared" frameBorder="0" width="100%" height="412" name="zERoz5Wa"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$ in *additional* space complexity.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
