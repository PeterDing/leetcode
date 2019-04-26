# 0994 - Rotting Oranges

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Breadth-first Search | [Leetcode](https://leetcode.com/problems/rotting-oranges) | [solution](https://leetcode.com/problems/rotting-oranges/solution/)


-----------

<p>In a given grid, each cell can have one of three&nbsp;values:</p>

<ul>
	<li>the value <code>0</code> representing an empty cell;</li>
	<li>the value <code>1</code> representing a fresh orange;</li>
	<li>the value <code>2</code> representing a rotten orange.</li>
</ul>

<p>Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.</p>

<p>Return the minimum number of minutes that must elapse until no cell has a fresh orange.&nbsp; If this is impossible, return <code>-1</code> instead.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/02/16/oranges.png" style="width: 712px; height: 150px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[2,1,1],[1,1,0],[0,1,1]]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[2,1,1],[0,1,1],[1,0,1]]</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
<strong>Explanation: </strong> The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[[0,2]]</span>
<strong>Output: </strong><span id="example-output-3">0</span>
<strong>Explanation: </strong> Since there are already no fresh oranges at minute 0, the answer is just 0.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length &lt;= 10</code></li>
	<li><code>1 &lt;= grid[0].length &lt;= 10</code></li>
	<li><code>grid[i][j]</code> is only <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ol>
</div>
</div>
</div>

-----------


## Similar Problems

- [Medium] [Walls and Gates](walls-and-gates)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Breadth-First Search

**Intuition**

Every turn, the rotting spreads from each rotting orange to other adjacent oranges.  Initially, the rotten oranges have 'depth' 0 [as in the spanning tree of a graph], and every time they rot a neighbor, the neighbors have 1 more depth.  We want to know the largest possible depth.

**Algorithm**

We can use a breadth-first search to model this process.  Because we always explore nodes (oranges) with the smallest depth first, we're guaranteed that each orange that becomes rotten does so with the lowest possible depth number.

We should also check that at the end, there are no fresh oranges left.

<iframe src="https://leetcode.com/playground/8S5VkeTc/shared" frameBorder="0" width="100%" height="500" name="8S5VkeTc"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of cells in the grid.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
