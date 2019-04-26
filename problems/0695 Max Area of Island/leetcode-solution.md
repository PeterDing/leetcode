# 0695 - Max Area of Island

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Depth-first Search | [Leetcode](https://leetcode.com/problems/max-area-of-island) | [solution](https://leetcode.com/problems/max-area-of-island/solution/)


-----------

<p>Given a non-empty 2D array <code>grid</code> of 0&#39;s and 1&#39;s, an <b>island</b> is a group of <code>1</code>&#39;s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)</p>

<p><b>Example 1:</b></p>

<pre>
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,0,<b>1</b>,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,<b>1</b>,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,0,0,0,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
</pre>
Given the above grid, return <code>6</code>. Note the answer is not 11, because the island must be connected 4-directionally.

<p><b>Example 2:</b></p>

<pre>
[[0,0,0,0,0,0,0,0]]</pre>
Given the above grid, return <code>0</code>.

<p><b>Note:</b> The length of each dimension in the given <code>grid</code> does not exceed 50.</p>


-----------


## Similar Problems

- [Medium] [Number of Islands](number-of-islands)

- [Easy] [Island Perimeter](island-perimeter)




## Solution:

[TOC]

#### Approach #1: Depth-First Search (Recursive) [Accepted]

**Intuition and Algorithm**

We want to know the area of each connected shape in the grid, then take the maximum of these.

If we are on a land square and explore every square connected to it 4-directionally (and recursively squares connected to those squares, and so on), then the total number of squares explored will be the area of that connected shape.

To ensure we don't count squares in a shape more than once, let's use `seen` to keep track of squares we haven't visited before.  It will also prevent us from counting the same shape more than once.

<iframe src="https://leetcode.com/playground/CQGNqDhr/shared" frameBorder="0" name="CQGNqDhr" width="100%" height="479"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(R*C)$$, where $$R$$ is the number of rows in the given `grid`, and $$C$$ is the number of columns.  We visit every square once.

* Space complexity: $$O(R*C)$$, the space used by `seen` to keep track of visited squares, and the space used by the call stack during our recursion.

---
#### Approach #2: Depth-First Search (Iterative) [Accepted]

**Intuition and Algorithm**

We can try the same approach using a stack based, (or "iterative") depth-first search.

Here, `seen` will represent squares that have either been visited or are added to our list of squares to visit (`stack`).  For every starting land square that hasn't been visited, we will explore 4-directionally around it, adding land squares that haven't been added to `seen` to our `stack`.

On the side, we'll keep a count `shape` of the total number of squares seen during the exploration of this shape.  We'll want the running max of these counts.

<iframe src="https://leetcode.com/playground/khZHhSir/shared" frameBorder="0" name="khZHhSir" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(R*C)$$, where $$R$$ is the number of rows in the given `grid`, and $$C$$ is the number of columns.  We visit every square once.

* Space complexity: $$O(R*C)$$, the space used by `seen` to keep track of visited squares, and the space used by `stack`.

---

Analysis written by: [@awice](https://leetcode.com/awice)
