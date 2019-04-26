# 0840 - Magic Squares In Grid

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/magic-squares-in-grid) | [solution](https://leetcode.com/problems/magic-squares-in-grid/solution/)


-----------

<p>A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers <strong>from 1 to 9</strong> such that each row, column, and both diagonals all have the same sum.</p>

<p>Given an <code>grid</code>&nbsp;of integers, how many 3 x 3 &quot;magic square&quot; subgrids are there?&nbsp; (Each subgrid is contiguous).</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
<strong>Output: </strong>1
<strong>Explanation: </strong>
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length&nbsp;&lt;= 10</code></li>
	<li><code>1 &lt;= grid[0].length&nbsp;&lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 15</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Brute Force [Accepted]

**Intuition and Algorithm**

Let's check every 3x3 grid individually.  For each grid, all numbers must be unique and between 1 and 9; plus every row, column, and diagonal must have the same sum.

**Extra Credit**

We could also include an `if grid[r+1][c+1] != 5: continue` check into our code, helping us skip over our `for r... for c...` for loops faster.  This is based on the following observations:

* The sum of the grid must be 45, as it is the sum of the distinct values from 1 to 9.
* Each horizontal and vertical line must add up to 15, as the sum of 3 of these lines equals the sum of the whole grid.
* The diagonal lines must also sum to 15, by definition of the problem statement.
* Adding the 12 values from the four lines that cross the center, these 4 lines add up to 60; but they also add up to the entire grid (45), plus 3 times the middle value.  This implies the middle value is 5.

<iframe src="https://leetcode.com/playground/6yuMDRxQ/shared" frameBorder="0" width="100%" height="500" name="6yuMDRxQ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(R*C)$$, where $$R, C$$ are the number of rows and columns in the given `grid`.

* Space Complexity:  $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
