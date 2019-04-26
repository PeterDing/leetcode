# 0835 - Image Overlap

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/image-overlap) | [solution](https://leetcode.com/problems/image-overlap/solution/)


-----------

<p>Two images <code>A</code> and <code>B</code> are given, represented as&nbsp;binary, square matrices of the same size.&nbsp; (A binary matrix has only 0s and 1s as values.)</p>

<p>We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.&nbsp; After, the <em>overlap</em> of this translation is the number of positions that have a 1 in both images.</p>

<p>(Note also that a translation does <strong>not</strong> include any kind of rotation.)</p>

<p>What is the largest possible overlap?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = [[1,1,0],
            [0,1,0],
&nbsp;           [0,1,0]]
&nbsp;      B = [[0,0,0],
&nbsp;           [0,1,1],
&nbsp;           [0,0,1]]
<strong>Output: </strong>3
<strong>Explanation:</strong> We slide A to right by 1 unit and down by 1 unit.</pre>

<p><strong>Notes:</strong>&nbsp;</p>

<ol>
	<li><code>1 &lt;= A.length = A[0].length = B.length = B[0].length &lt;= 30</code></li>
	<li><code>0 &lt;=&nbsp;A[i][j], B[i][j] &lt;= 1</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Translate by Delta [Accepted]

**Intuition and Algorithm**

For each translation `delta`, we calculate the candidate answer `overlap(delta)`, which is the size of the overlap if we shifted the matrix `A` by delta.

We only need to check `delta` for which some point in `A` maps to some point in `B`, since a candidate overlap must be at least 1.  Using a Set `seen`, we remember if we've calculated `overlap(delta)`, so that we don't perform this expensive check more than once per `delta`.

We use `java.awt.Point` (or `complex` in Python) to handle our 2D vectors gracefully.  We could have also mapped a vector `delta = (x, y)` (which has coordinates between `-(N-1)` and `N-1`) to `2*N x + y` for convenience.  Note that we cannot map it to `N*dx, dy` as there would be interference: `(0, N-1)` and `(1, -1)` would map to the same point.

<iframe src="https://leetcode.com/playground/gnwqTeGt/shared" frameBorder="0" width="100%" height="500" name="gnwqTeGt"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^6)$$, where $$N$$ is the length of `A` or `B`.

* Space Complexity: $$O(N^2)$$.


---
#### Approach #2: Count by Delta [Accepted]

**Intuition and Algorithm**

We can do the reverse of *Approach #1*: count every possible `delta = b - a` we see.  If we see say, 5 of the same `delta = b - a`, then the translation by `delta` must have overlap 5.

<iframe src="https://leetcode.com/playground/YmA2kxzz/shared" frameBorder="0" width="100%" height="378" name="YmA2kxzz"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^4)$$, where $$N$$ is the length of `A` or `B`.

* Space Complexity: $$O(N^2)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
