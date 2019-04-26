# 0867 - Transpose Matrix

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/transpose-matrix) | [solution](https://leetcode.com/problems/transpose-matrix/solution/)


-----------

<p>Given a&nbsp;matrix <code>A</code>, return the transpose of <code>A</code>.</p>

<p>The transpose of a matrix is the matrix flipped over it&#39;s main diagonal, switching the row and column indices of the matrix.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,2,3],[4,5,6],[7,8,9]]</span>
<strong>Output: </strong><span id="example-output-1">[[1,4,7],[2,5,8],[3,6,9]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[1,2,3],[4,5,6]]</span>
<strong>Output: </strong><span id="example-output-2">[[1,4],[2,5],[3,6]]</span>
</pre>

<p>&nbsp;</p>

<p><span><strong>Note:</strong></span></p>

<ol>
	<li><code><span>1 &lt;= A.length&nbsp;&lt;= 1000</span></code></li>
	<li><code><span>1 &lt;= A[0].length&nbsp;&lt;= 1000</span></code></li>
</ol>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Copy Directly

**Intuition and Algorithm**

The transpose of a matrix `A` with dimensions `R x C` is a matrix `ans` with dimensions `C x R` for which `ans[c][r] = A[r][c]`.

Let's initialize a new matrix `ans` representing the answer.  Then, we'll copy each entry of the matrix as appropriate.

<iframe src="https://leetcode.com/playground/npb7vRxu/shared" frameBorder="0" width="100%" height="242" name="npb7vRxu"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(R * C)$$, where $$R$$ and $$C$$ are the number of rows and columns in the given matrix `A`.

* Space Complexity:  $$O(R * C)$$, the space used by the answer.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
