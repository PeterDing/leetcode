# 0885 - Spiral Matrix III

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math | [Leetcode](https://leetcode.com/problems/spiral-matrix-iii) | [solution](https://leetcode.com/problems/spiral-matrix-iii/solution/)


-----------

<p>On a 2 dimensional grid with <code>R</code> rows and <code>C</code> columns, we start at <code>(r0, c0)</code> facing east.</p>

<p>Here, the north-west corner of the grid is at the&nbsp;first row and column, and the south-east corner of the grid is at the last row and column.</p>

<p>Now, we walk in a clockwise spiral shape to visit every position in this grid.&nbsp;</p>

<p>Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.)&nbsp;</p>

<p>Eventually, we reach all <code>R * C</code> spaces of the grid.</p>

<p>Return a list of coordinates representing the positions of the grid in the order they were visited.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>R = <span id="example-input-1-1">1</span>, C = <span id="example-input-1-2">4</span>, r0 = <span id="example-input-1-3">0</span>, c0 = <span id="example-input-1-4">0</span>
<strong>Output: </strong><span id="example-output-1">[[0,0],[0,1],[0,2],[0,3]]</span>

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png" style="width: 174px; height: 99px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>R = <span id="example-input-2-1">5</span>, C = <span id="example-input-2-2">6</span>, r0 = <span id="example-input-2-3">1</span>, c0 = <span id="example-input-2-4">4</span>
<strong>Output: </strong><span id="example-output-2">[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]</span>

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png" style="width: 202px; height: 142px;" />
</pre>

<div>
<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= R &lt;= 100</code></li>
	<li><code>1 &lt;= C &lt;= 100</code></li>
	<li><code>0 &lt;= r0 &lt; R</code></li>
	<li><code>0 &lt;= c0 &lt; C</code></li>
</ol>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Walk in a Spiral

**Intuition**

We can walk in a spiral shape from the starting square, ignoring whether we stay in the grid or not.  Eventually, we must have reached every square in the grid.

**Algorithm**

Examining the lengths of our walk in each direction, we find the following pattern: `1, 1, 2, 2, 3, 3, 4, 4, ...`  That is, we walk 1 unit east, then 1 unit south, then 2 units west, then 2 units north, then 3 units east, etc.  Because our walk is self-similar, this pattern repeats in the way we expect.

After, the algorithm is straightforward: perform the walk and record positions of the grid in the order we visit them.  Please read the inline comments for more details.

<iframe src="https://leetcode.com/playground/XTsQ5Bi8/shared" frameBorder="0" width="100%" height="500" name="XTsQ5Bi8"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O((\max(R, C))^2)$$.  Potentially, our walk needs to spiral until we move $$R$$ in one direction, and $$C$$ in another direction, so as to reach every cell of the grid.

* Space Complexity:  $$O(R * C)$$, the space used by the answer.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
