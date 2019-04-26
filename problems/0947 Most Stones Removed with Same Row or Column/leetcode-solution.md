# 0947 - Most Stones Removed with Same Row or Column

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Depth-first Search, Union Find | [Leetcode](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column) | [solution](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solution/)


-----------

<p>On a 2D plane, we place stones at some integer coordinate points.&nbsp; Each coordinate point may have at most one stone.</p>

<p>Now, a <em>move</em> consists of removing a stone&nbsp;that shares a column or row with another stone on the grid.</p>

<p>What is the largest possible number of moves we can make?</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>stones = <span id="example-input-1-2">[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]</span>
<strong>Output: </strong>5
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>stones = <span id="example-input-2-2">[[0,0],[0,2],[1,1],[2,0],[2,2]]</span>
<strong>Output: </strong>3
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>stones = <span id="example-input-3-2">[[0,0]]</span>
<strong>Output: </strong>0
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1 &lt;= stones.length &lt;= 1000</code></li>
	<li><code>0 &lt;= stones[i][j] &lt; 10000</code></li>
</ol>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Depth-First Search

**Intuition**

Let's say two stones are connected by an edge if they share a row or column, and define a connected component in the usual way for graphs: a subset of stones so that there doesn't exist an edge from a stone in the subset to a stone not in the subset.  For convenience, we refer to a *component* as meaning a connected component.

The main insight is that we can always make moves that reduce the number of stones in each component to 1.

Firstly, every stone belongs to exactly one component, and moves in one component do not affect another component.

Now, consider a spanning tree of our component.  We can make moves repeatedly from the leaves of this tree until there is one stone left.

**Algorithm**

To count connected components of the above graph, we will use depth-first search.

For every stone not yet visited, we will visit it and any stone in the same connected component.  Our depth-first search traverses each node in the component.

For each component, the answer changes by `-1 + component.size`.

<iframe src="https://leetcode.com/playground/vFbGLUPW/shared" frameBorder="0" width="100%" height="500" name="vFbGLUPW"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `stones`.

* Space Complexity:  $$O(N^2)$$.
<br />
<br />


---
#### Approach 2: Union-Find

**Intuition**

As in *Approach 1*, we will need to consider components of an underlying graph.  A "Disjoint Set Union" (DSU) data structure is ideal for this.

We will skip the explanation of how a DSU structure is implemented.  Please refer to [https://leetcode.com/problems/redundant-connection/solution/](https://leetcode.com/problems/redundant-connection/solution/) for a tutorial on DSU.

**Algorithm**

Let's connect row `i` to column `j`, which will be represented by `j+10000`.  The answer is the number of components after making all the connections.

Note that for brevity, our `DSU` implementation does not use union-by-rank.  This makes the asymptotic time complexity larger.

<iframe src="https://leetcode.com/playground/hhTCv59W/shared" frameBorder="0" width="100%" height="500" name="hhTCv59W"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `stones`.  (If we used union-by-rank, this can be $$O(N * \alpha(N))$$, where $$\alpha$$ is the Inverse-Ackermann function.)

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
