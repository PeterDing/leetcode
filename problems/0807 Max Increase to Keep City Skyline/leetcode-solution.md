# 0807 - Max Increase to Keep City Skyline

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/max-increase-to-keep-city-skyline) | [solution](https://leetcode.com/problems/max-increase-to-keep-city-skyline/solution/)


-----------

<p>In a 2 dimensional array <code>grid</code>, each value <code>grid[i][j]</code> represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts&nbsp;can be different for different buildings). Height&nbsp;0 is considered to be a&nbsp;building&nbsp;as well.&nbsp;</p>

<p>At the end, the &quot;skyline&quot; when viewed from all four directions&nbsp;of the grid, i.e.&nbsp;top, bottom, left, and right,&nbsp;must be the same as the&nbsp;skyline of the original grid. A city&#39;s skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See&nbsp;the following example.</p>

<p>What is the maximum total sum that the height of the buildings can be increased?</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
<strong>Output:</strong> 35
<strong>Explanation:</strong> 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

</pre>

<p><strong>Notes: </strong></p>

<ul>
	<li><code>1 &lt; grid.length = grid[0].length &lt;= 50</code>.</li>
	<li>All heights <code>grid[i][j]</code> are in the range <code>[0, 100]</code>.</li>
	<li>All buildings in <code>grid[i][j]</code> occupy the entire grid cell: that is, they are a <code>1 x 1 x grid[i][j]</code> rectangular prism.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Row and Column Maximums [Accepted]

**Intuition and Algorithm**

The skyline looking from the top is `col_maxes = [max(column_0), max(column_1), ...]`.  Similarly, the skyline from the left is `row_maxes [max(row_0), max(row_1), ...]`

In particular, each building `grid[r][c]` could become height `min(max(row_r), max(col_c))`, and this is the largest such height.  If it were larger, say `grid[r][c] > max(row_r)`, then the part of the skyline `row_maxes = [..., max(row_r), ...]` would change.

These increases are also independent (none of them change the skyline), so we can perform them independently.

<iframe src="https://leetcode.com/playground/ELQgWsrX/shared" frameBorder="0" width="100%" height="395" name="ELQgWsrX"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the number of rows (and columns) of the grid.  We iterate through every cell of the grid.

* Space Complexity: $$O(N)$$, the space used by `row_maxes` and `col_maxes`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
