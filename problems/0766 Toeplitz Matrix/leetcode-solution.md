# 0766 - Toeplitz Matrix

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/toeplitz-matrix) | [solution](https://leetcode.com/problems/toeplitz-matrix/solution/)


-----------

<p>A matrix is <em>Toeplitz</em> if every diagonal from top-left to bottom-right has the same element.</p>

<p>Now given an <code>M x N</code> matrix, return&nbsp;<code>True</code>&nbsp;if and only if the matrix is <em>Toeplitz</em>.<br />
&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong>matrix = [
&nbsp; [1,2,3,4],
&nbsp; [5,1,2,3],
&nbsp; [9,5,1,2]
]
<strong>Output:</strong> True
<strong>Explanation:</strong>
In the above grid, the&nbsp;diagonals are:
&quot;[9]&quot;, &quot;[5, 5]&quot;, &quot;[1, 1, 1]&quot;, &quot;[2, 2, 2]&quot;, &quot;[3, 3]&quot;, &quot;[4]&quot;.
In each diagonal all elements are the same, so the answer is True.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
</strong>matrix = [
&nbsp; [1,2],
&nbsp; [2,2]
]
<strong>Output:</strong> False
<strong>Explanation:</strong>
The diagonal &quot;[1, 2]&quot; has different elements.
</pre>

<p><br />
<strong>Note:</strong></p>

<ol>
	<li><code>matrix</code> will be a 2D array of integers.</li>
	<li><code>matrix</code> will have a number of rows and columns in range <code>[1, 20]</code>.</li>
	<li><code>matrix[i][j]</code> will be integers in range <code>[0, 99]</code>.</li>
</ol>

<p><br />
<strong>Follow up:</strong></p>

<ol>
	<li>What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?</li>
	<li>What if the matrix is so large that you can only load up a partial row into the memory at once?</li>
</ol>


-----------


## Similar Problems

- [Easy] [Valid Word Square](valid-word-square)




## Solution:

[TOC]


---
#### Approach #1: Group by Category [Accepted]

**Intuition and Algorithm**

We ask what feature makes two coordinates `(r1, c1)` and `(r2, c2)` belong to the same diagonal?

It turns out two coordinates are on the same diagonal if and only if `r1 - c1 == r2 - c2`.

This leads to the following idea: remember the value of that diagonal as `groups[r-c]`.  If we see a mismatch, the matrix is not Toeplitz; otherwise it is.

<iframe src="https://leetcode.com/playground/aPydaE7r/shared" frameBorder="0" width="100%" height="293" name="aPydaE7r"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(M*N)$$.  (Recall in the problem statement that $$M, N$$ are the number of rows and columns in `matrix`.)

* Space Complexity: $$O(M+N)$$.

---
#### Approach #2: Compare With Top-Left Neighbor [Accepted]

**Intuition and Algorithm**

For each diagonal with elements in order $$a_1, a_2, a_3, \dots, a_k$$, we can check $$a_1 = a_2, a_2 = a_3, \dots, a_{k-1} = a_k$$.  The matrix is *Toeplitz* if and only if all of these conditions are true for all (top-left to bottom-right) diagonals.

Every element belongs to some diagonal, and it's previous element (if it exists) is it's top-left neighbor.  Thus, for the square `(r, c)`, we only need to check `r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c]`.

<iframe src="https://leetcode.com/playground/bfeF5wnM/shared" frameBorder="0" width="100%" height="208" name="bfeF5wnM"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(M*N)$$, as defined in the problem statement.

* Space Complexity: $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
