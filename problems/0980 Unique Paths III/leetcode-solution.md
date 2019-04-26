# 0980 - Unique Paths III

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Backtracking, Depth-first Search | [Leetcode](https://leetcode.com/problems/unique-paths-iii) | [solution](https://leetcode.com/problems/unique-paths-iii/solution/)


-----------

<p>On a 2-dimensional&nbsp;<code>grid</code>, there are 4 types of squares:</p>

<ul>
	<li><code>1</code> represents the starting square.&nbsp; There is exactly one starting square.</li>
	<li><code>2</code> represents the ending square.&nbsp; There is exactly one ending square.</li>
	<li><code>0</code> represents empty squares we can walk over.</li>
	<li><code>-1</code> represents obstacles that we cannot walk over.</li>
</ul>

<p>Return the number of 4-directional walks&nbsp;from the starting square to the ending square, that <strong>walk over every non-obstacle square&nbsp;exactly once</strong>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[1,0,0,0],[0,0,0,0],[0,0,0,2]]</span>
<strong>Output: </strong><span id="example-output-2">4</span>
<strong>Explanation: </strong>We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[[0,1],[2,0]]</span>
<strong>Output: </strong><span id="example-output-3">0</span>
<strong>Explanation: </strong>
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
</pre>
</div>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length * grid[0].length &lt;= 20</code></li>
</ol>

-----------


## Similar Problems

- [Hard] [Sudoku Solver](sudoku-solver)

- [Medium] [Unique Paths II](unique-paths-ii)

- [Hard] [Word Search II](word-search-ii)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Backtracking DFS

**Intuition and Algorithm**

Let's try walking to each `0`, leaving an obstacle behind from where we walked.  After, we can remove the obstacle.

Given the input limits, this can work because bad paths tend to get stuck quickly and run out of free squares.

<iframe src="https://leetcode.com/playground/bfNeazhV/shared" frameBorder="0" width="100%" height="500" name="bfNeazhV"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(4^{R*C})$$, where $$R, C$$ are the number of rows and columns in the grid.  (We can find tighter bounds, but such a bound is beyond the scope of this article.)

* Space Complexity:  $$O(R*C)$$.
<br />
<br />


---
#### Approach 2: Dynamic Programming

**Intuition and Algorithm**

Let `dp(r, c, todo)` be the number of paths starting from where we are (`r, c`), and given that `todo` is the set of empty squares we've yet to walk on.

We can use a similar approach to *Approach 1*, except we will memoize these states `(r, c, todo)` so as not to repeat work.

<iframe src="https://leetcode.com/playground/KxYhLJfP/shared" frameBorder="0" width="100%" height="500" name="KxYhLJfP"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(R * C * 2^{R*C})$$, where $$R, C$$ are the number of rows and columns in the grid.

* Space Complexity:  $$O(R * C)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
