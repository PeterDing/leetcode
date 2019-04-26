# 0863 - All Nodes Distance K in Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree, Depth-first Search, Breadth-first Search | [Leetcode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree) | [solution](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solution/)


-----------

<p>We are given a binary tree (with root node&nbsp;<code>root</code>), a <code>target</code> node, and an integer value <code>K</code>.</p>

<p>Return a list of the values of all&nbsp;nodes that have a distance <code>K</code> from the <code>target</code> node.&nbsp; The answer can be returned in any order.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[3,5,1,6,2,0,8,null,null,7,4]</span>, target = <span id="example-input-1-2">5</span>, K = <span id="example-input-1-3">2</span>

<strong>Output: </strong><span id="example-output-1">[7,4,1]</span>

<strong>Explanation: </strong>
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" style="width: 280px; height: 240px;" />

Note that the inputs &quot;root&quot; and &quot;target&quot; are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The given tree is non-empty.</li>
	<li>Each node in the tree has unique values&nbsp;<code>0 &lt;= node.val &lt;= 500</code>.</li>
	<li>The <code>target</code>&nbsp;node is a node in the tree.</li>
	<li><code>0 &lt;= K &lt;= 1000</code>.</li>
</ol>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Annotate Parent

**Intuition**

If we know the parent of every node `x`, we know all nodes that are distance `1` from `x`.  We can then perform a breadth first search from the `target` node to find the answer.

**Algorithm**

We first do a depth first search where we annotate every node with information about it's parent.

After, we do a breadth first search to find all nodes a distance `K` from the `target`.

<iframe src="https://leetcode.com/playground/ySaDMJzK/shared" frameBorder="0" width="100%" height="500" name="ySaDMJzK"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Percolate Distance

**Intuition**

From `root`, say the `target` node is at depth `3` in the left branch.  It means that any nodes that are distance `K - 3` in the right branch should be added to the answer.

**Algorithm**

Traverse every `node` with a depth first search `dfs`.  We'll add all nodes `x` to the answer such that `node` is the node on the path from `x` to `target` that is closest to the `root`.

To help us, `dfs(node)` will return the distance from `node` to the `target`.  Then, there are 4 cases:

* If `node == target`, then we should add nodes that are distance `K` in the subtree rooted at `target`.

* If `target` is in the left branch of `node`, say at distance `L+1`, then we should look for nodes that are distance `K - L - 1` in the right branch.

* If `target` is in the right branch of `node`, the algorithm proceeds similarly.

* If `target` isn't in either branch of `node`, then we stop.

In the above algorithm, we make use of the auxillary function `subtree_add(node, dist)` which adds the nodes in the subtree rooted at `node` that are distance `K - dist` from the given `node`.

<iframe src="https://leetcode.com/playground/4h24GtWA/shared" frameBorder="0" width="100%" height="500" name="4h24GtWA"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
