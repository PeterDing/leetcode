# 0803 - Bricks Falling When Hit

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Union Find | [Leetcode](https://leetcode.com/problems/bricks-falling-when-hit) | [solution](https://leetcode.com/problems/bricks-falling-when-hit/solution/)


-----------

<p>We have a grid of 1s and 0s; the 1s in a cell represent bricks.&nbsp; A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.</p>

<p>We will do some erasures&nbsp;sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may&nbsp;drop because of that&nbsp;erasure.</p>

<p>Return an array representing the number of bricks that will drop after each erasure in sequence.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> 
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
<strong>Output:</strong> [2]
<strong>Explanation: </strong>
If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> 
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
<strong>Output:</strong> [0,0]
<strong>Explanation: </strong>
When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The number of rows and columns in the grid will be in the range&nbsp;[1, 200].</li>
	<li>The number of erasures will not exceed the area of the grid.</li>
	<li>It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.</li>
	<li>An erasure may refer to a location with no brick - if it does, no bricks drop.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Reverse Time and Union-Find [Accepted]

**Intuition**

The problem is about knowing information about the connected components of a graph as we cut vertices.  In particular, we'll like to know the size of the "roof" (component touching the top edge) between each cut.  Here, a cut refers to the erasure of a vertex.

As we may know, a useful data structure for joining connected components is a disjoint set union structure.  The key idea in this problem is that we can use this structure if we work in reverse: instead of looking at the graph as a series of sequential cuts, we'll look at the graph after all the cuts, and reverse each cut.

**Algorithm**

We'll modify our typical disjoint-set-union structure to include a `dsu.size` operation, that tells us the size of this component.  The way we do this is whenever we make a component point to a new parent, we'll also send it's size to that parent.

We'll also include `dsu.top`, which tells us the size of the "roof", or the component connected to the top edge.  We use an *ephemeral* "source" node with label `R * C` where all nodes on the top edge (with row number `0`) are connected to the source node.

For more information on DSU, please look at *Approach #2* in the [article here](https://leetcode.com/articles/redundant-connection/).

Next, we'll introduce `A`, the grid after all the cuts have happened, and initialize our disjoint union structure on the graph induced by `A` (nodes are grid squares with a brick; edges between 4-directionally adjacent nodes).

After, if we get an cut at `(r, c)` but the original `grid[r][c]` was always `0`, then we couldn't have had a meaningful cut - the number of dropped bricks is `0`.

Otherwise, we'll look at the size of the new roof after adding this brick at `(r, c)`, and compare them to find the number of dropped bricks.

Since we were working in reverse time order, we should reverse our working answer to arrive at our final answer.

<iframe src="https://leetcode.com/playground/vKx7cbxE/shared" frameBorder="0" width="100%" height="500" name="vKx7cbxE"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N*Q*\alpha(N * Q))$$, where $$N = R*C$$ is the number of grid squares, $$Q$$ is the length of `hits`, and $$\alpha$$ is the *Inverse-Ackermann function*.

* Space Complexity: $$O(N)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
