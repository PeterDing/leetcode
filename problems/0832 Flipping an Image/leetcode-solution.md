# 0832 - Flipping an Image

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/flipping-an-image) | [solution](https://leetcode.com/problems/flipping-an-image/solution/)


-----------

<p>Given a binary matrix <code>A</code>, we want to flip the image horizontally, then invert it, and return the resulting image.</p>

<p>To flip an image horizontally means that each row of the image is reversed.&nbsp; For example, flipping&nbsp;<code>[1, 1, 0]</code>&nbsp;horizontally results in&nbsp;<code>[0, 1, 1]</code>.</p>

<p>To invert an image means&nbsp;that each <code>0</code> is replaced by <code>1</code>, and each <code>1</code> is replaced by <code>0</code>.&nbsp;For example, inverting&nbsp;<code>[0, 1, 1]</code>&nbsp;results in&nbsp;<code>[1, 0, 0]</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[1,1,0],[1,0,1],[0,0,0]]
<strong>Output: </strong>[[1,0,0],[0,1,0],[1,1,1]]
<strong>Explanation:</strong> First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong>Output: </strong>[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong>Explanation:</strong> First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

<p><strong>Notes:</strong></p>

<ul>
	<li><code>1 &lt;= A.length = A[0].length &lt;= 20</code></li>
	<li><code>0 &lt;= A[i][j]<font face="sans-serif, Arial, Verdana, Trebuchet MS">&nbsp;&lt;=&nbsp;</font>1</code></li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Direct [Accepted]

**Intuition and Algorithm**

We can do this in place.  In each row, the `i`th value from the left is equal to the inverse of the `i`th value from the right.

We use `(C+1) / 2` (with floor division) to iterate over all indexes `i` in the first half of the row, including the center.

<iframe src="https://leetcode.com/playground/rePZz3yF/shared" frameBorder="0" width="100%" height="276" name="rePZz3yF"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where `N` is the total number of elements in `A`.

* Space Complexity: $$O(1)$$ in *additional* space complexity.

---

Analysis written by: [@awice](https://leetcode.com/awice).
