# 0827 - Making A Large Island

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Depth-first Search | [Leetcode](https://leetcode.com/problems/making-a-large-island) | [solution](https://leetcode.com/problems/making-a-large-island/solution/)


-----------

<p>In a 2D grid of <code>0</code>s and <code>1</code>s, we change at most one <code>0</code> to a <code>1</code>.</p>

<p>After, what is the size of the largest island?&nbsp;(An island is a 4-directionally connected group of <code>1</code>s).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[1, 0], [0, 1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[1, 1], [1, 0]]
<strong>Output:</strong> 4
<strong>Explanation: </strong>Change the 0 to 1 and make the island bigger, only one island with area = 4.</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>[[1, 1], [1, 1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Can&#39;t change any 0 to 1, only one island with area = 4.</pre>

<p>&nbsp;</p>

<p>Notes:</p>

<ul>
	<li><code>1 &lt;= grid.length = grid[0].length &lt;= 50</code>.</li>
	<li><code>0 &lt;= grid[i][j] &lt;= 1</code>.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: (Naive) Depth First Search [Time Limit Exceeded]

**Intuition**

For each `0` in the grid, let's temporarily change it to a `1`, then count the size of the group from that square.

**Algorithm**

For each `0`, change it to a `1`, then do a depth first search to find the size of that component.  The answer is the maximum size component found.

Of course, if there is no `0` in the grid, then the answer is the size of the whole grid.

<iframe src="https://leetcode.com/playground/T2PdhCGT/shared" frameBorder="0" width="100%" height="500" name="T2PdhCGT"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^4)$$, where $$N$$ is the length and width of the `grid`.

* Space Complexity: $$O(N^2)$$, the additional space used in the depth first search by `stack` and `seen`.

---
#### Approach #2: Component Sizes [Accepted]

**Intuition**

As in the previous solution, we check every `0`.  However, we also store the size of each group, so that we do not have to use depth-first search to repeatedly calculate the same size.

However, this idea fails when the `0` touches the same group.  For example, consider `grid = [[0,1],[1,1]]`.  The answer is `4`, not `1 + 3 + 3`, since the right neighbor and the bottom neighbor of the `0` belong to the same group.

We can remedy this problem by keeping track of a group id (or index), that is unique for each group.  Then, we'll only add areas of neighboring groups with different ids.

**Algorithm**

For each group, fill it with value `index` and remember it's size as `area[index] = dfs(...)`.

Then for each `0`, look at the neighboring group ids `seen` and add the area of those groups, plus 1 for the `0` we are toggling.  This gives us a candidate answer, and we take the maximum.

To solve the issue of having potentially no `0`, we take the maximum of the previously calculated areas.

<iframe src="https://leetcode.com/playground/ZBn4MTj4/shared" frameBorder="0" width="100%" height="500" name="ZBn4MTj4"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length and width of the `grid`.

* Space Complexity: $$O(N^2)$$, the additional space used in the depth first search by `area`.

---

Analysis written by: [@awice](https://leetcode.com/awice).  Idea for Solution #2 by [@lee215](http://leetcode.com/lee215).
