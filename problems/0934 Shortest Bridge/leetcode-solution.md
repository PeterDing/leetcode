# 0934 - Shortest Bridge

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Depth-first Search, Breadth-first Search | [Leetcode](https://leetcode.com/problems/shortest-bridge) | [solution](https://leetcode.com/problems/shortest-bridge/solution/)


-----------

<p>In a given 2D binary array <code>A</code>, there are two islands.&nbsp; (An island is a 4-directionally connected group of&nbsp;<code>1</code>s not connected to any other 1s.)</p>

<p>Now, we may change <code>0</code>s to <code>1</code>s so as to connect the two islands together to form 1 island.</p>

<p>Return the smallest number of <code>0</code>s that must be flipped.&nbsp; (It is guaranteed that the answer is at least 1.)</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[0,1],[1,0]]</span>
<strong>Output: </strong>1
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[0,1,0],[0,0,0],[0,0,1]]</span>
<strong>Output: </strong>2
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]</span>
<strong>Output: </strong><span id="example-output-3">1</span></pre>

<p>&nbsp;</p>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length =&nbsp;A[0].length &lt;= 100</code></li>
	<li><code>A[i][j] == 0</code> or <code>A[i][j] == 1</code></li>
</ol>

<div>
<div>
<div>&nbsp;</div>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Find and Grow

**Intuition**

Conceptually, our method is very straightforward: find both islands, then for one of the islands, keep "growing" it by 1 until we touch the second island.

We can use a depth-first search to find the islands, and a breadth-first search to "grow" one of them.  This leads to a verbose but correct solution.

**Algorithm**

To find both islands, look for a square with a `1` we haven't visited, and dfs to get the component of that region.  Do this twice.  After, we have two components `source` and `target`.

To find the shortest bridge, do a BFS from the nodes `source`.  When we reach any node in `target`, we will have found the shortest distance.

Please see the code for more implementation details.

<iframe src="https://leetcode.com/playground/wfdtey9G/shared" frameBorder="0" width="100%" height="500" name="wfdtey9G"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\mathcal{A})$$, where $$\mathcal{A}$$ is the content of `A`.

* Space Complexity:  $$O(\mathcal{A})$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
