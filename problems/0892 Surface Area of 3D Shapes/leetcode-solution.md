# 0892 - Surface Area of 3D Shapes

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math, Geometry | [Leetcode](https://leetcode.com/problems/surface-area-of-3d-shapes) | [solution](https://leetcode.com/problems/surface-area-of-3d-shapes/solution/)


-----------

<p>On a&nbsp;<code>N&nbsp;*&nbsp;N</code>&nbsp;grid, we place some&nbsp;<code>1 * 1 * 1&nbsp;</code>cubes.</p>

<p>Each value&nbsp;<code>v = grid[i][j]</code>&nbsp;represents a tower of&nbsp;<code>v</code>&nbsp;cubes placed on top of grid cell&nbsp;<code>(i, j)</code>.</p>

<p>Return the total surface area of the resulting shapes.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<ul>
</ul>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[2]]</span>
<strong>Output: </strong><span id="example-output-1">10</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[1,2],[3,4]]</span>
<strong>Output: </strong><span id="example-output-2">34</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[[1,0],[0,2]]</span>
<strong>Output: </strong><span id="example-output-3">16</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[[1,1,1],[1,0,1],[1,1,1]]</span>
<strong>Output: </strong><span id="example-output-4">32</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[[2,2,2],[2,1,2],[2,2,2]]</span>
<strong>Output: </strong><span id="example-output-5">46</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 50</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 50</code></li>
</ul>
</div>
</div>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Square by Square

**Intuition**

Let's try to count the surface area contributed by `v = grid[i][j]`.

When `v > 0`, the top and bottom surface contributes an area of 2.

Then, for each side (west side, north side, east side, south side) of the column at `grid[i][j]`, the neighboring cell with value `nv` means our square contributes `max(v - nv, 0)`.

For example, for `grid = [[1, 5]]`, the contribution at `grid[0][1]` is 2 + 5 + 5 + 5 + 4.  The 2 comes from the top and bottom side, the 5 comes from the north, east, and south side; and the 4 comes from the west side, of which 1 unit is covered by the adjacent column.

**Algorithm**

For each `v = grid[r][c] > 0`, count `ans += 2`, plus `ans += max(v - nv, 0)` for each neighboring value `nv` adjacent to `grid[r][c]`.

<iframe src="https://leetcode.com/playground/JqxzqTG3/shared" frameBorder="0" width="100%" height="497" name="JqxzqTG3"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the number of rows (and columns) in the `grid`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
