# 0861 - Score After Flipping Matrix

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Greedy | [Leetcode](https://leetcode.com/problems/score-after-flipping-matrix) | [solution](https://leetcode.com/problems/score-after-flipping-matrix/solution/)


-----------

<p>We have a two dimensional matrix&nbsp;<code>A</code> where each value is <code>0</code> or <code>1</code>.</p>

<p>A move consists of choosing any row or column, and toggling each value in that row or column: changing all <code>0</code>s to <code>1</code>s, and all <code>1</code>s to <code>0</code>s.</p>

<p>After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.</p>

<p>Return the highest possible&nbsp;score.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[0,0,1,1],[1,0,1,0],[1,1,0,0]]</span>
<strong>Output: </strong><span id="example-output-1">39</span>
<strong>Explanation:
</strong>Toggled to <span id="example-input-1-1">[[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39</span></pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20</code></li>
	<li><code>1 &lt;= A[0].length &lt;= 20</code></li>
	<li><code>A[i][j]</code>&nbsp;is <code>0</code> or <code>1</code>.</li>
</ol>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Brute Force

**Intuition**

Notice that a `1` in the $$i$$th column from the right, contributes $$2^i$$ to the score.

Say we are finished toggling the rows in some configuration.  Then for each column, (to maximize the score), we'll toggle the column if it would increase the number of `1`s.

We can brute force over every possible way to toggle rows.

**Algorithm**

Say the matrix has `R` rows and `C` columns.

For each `state`, the transition `trans = state ^ (state-1)` represents the rows that must be toggled to get into the state of toggled rows represented by (the bits of) `state`.

We'll toggle them, and also maintain the correct column sums of the matrix on the side.

Afterwards, we'll calculate the score.  If for example the last column has a column sum of `3`, then the score is `max(3, R-3)`, where `R-3` represents the score we get from toggling the last column.

In general, the score is increased by `max(col_sum, R - col_sum) * (1 << (C-1-c))`, where the factor `(1 << (C-1-c))` is the power of `2` that each `1` contributes.

Note that this approach may not run in the time allotted.


<iframe src="https://leetcode.com/playground/RqkiosdE/shared" frameBorder="0" width="100%" height="500" name="RqkiosdE"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(2^R * R * C)$$, where $$R, C$$ is the number of rows and columns in the matrix.

* Space Complexity:  $$O(C)$$ in additional space complexity.
<br />
<br />


---
#### Approach 2: Greedy

**Intuition**

Notice that a `1` in the $$i$$th column from the right, contributes $$2^i$$ to the score.

Since $$2^n > 2^{n-1} + 2^{n-2} + \cdots + 2^0$$, maximizing the left-most digit is more important than any other digit.  Thus, the rows should be toggled such that the left-most column is either all `0` or all `1` (so that after toggling the left-most column [if necessary], the left column is all `1`.)

**Algorithm**

If we toggle rows by the first column (`A[r][c] ^= A[r][0]`), then the first column will be all `0`.

Afterwards, the base score is `max(col, R - col)` where `col` is the column sum; and `(1 << (C-1-c))` is the power of 2 that each `1` in that column contributes to the score.

<iframe src="https://leetcode.com/playground/2SApjxHH/shared" frameBorder="0" width="100%" height="276" name="2SApjxHH"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(R * C)$$, $$R, C$$ is the number of rows and columns in the matrix.

* Space Complexity:  $$O(1)$$ in additional space complexity.
<br />
<br />

---


Analysis written by: [@awice](https://leetcode.com/awice).
