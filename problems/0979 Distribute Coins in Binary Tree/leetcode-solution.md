# 0979 - Distribute Coins in Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree, Depth-first Search | [Leetcode](https://leetcode.com/problems/distribute-coins-in-binary-tree) | [solution](https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/)


-----------

<p>Given the <code>root</code> of a binary tree with <code>N</code> nodes, each <code>node</code>&nbsp;in the tree has <code>node.val</code> coins, and there are <code>N</code> coins total.</p>

<p>In one move, we may choose two adjacent nodes and move one coin from one node to another.&nbsp; (The move may be from parent to child, or from child to parent.)</p>

<p>Return the number of moves required to make every node have exactly one coin.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree1.png" style="width: 150px; height: 142px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,0,0]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>From the root of the tree, we move one coin to its left child, and one coin to its right child.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree2.png" style="width: 150px; height: 142px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[0,3,0]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree3.png" style="width: 150px; height: 142px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,0,2]</span>
<strong>Output: </strong><span id="example-output-3">2</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree4.png" style="width: 155px; height: 156px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,0,0,null,3]</span>
<strong>Output: </strong><span id="example-output-4">4</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1&lt;= N &lt;= 100</code></li>
	<li><code>0 &lt;= node.val &lt;= N</code></li>
</ol>
</div>
</div>
</div>
</div>

-----------


## Similar Problems

- [Hard] [Sum of Distances in Tree](sum-of-distances-in-tree)

- [Hard] [Binary Tree Cameras](binary-tree-cameras)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Depth First Search

**Intuition**

If the leaf of a tree has 0 coins (an excess of -1 from what it needs), then we should push a coin from its parent onto the leaf.  If it has say, 4 coins (an excess of 3), then we should push 3 coins off the leaf.  In total, the number of moves from that leaf to or from its parent is `excess = Math.abs(num_coins - 1)`.  Afterwards, we never have to consider this leaf again in the rest of our calculation.

**Algorithm**

We can use the above fact to build our answer.  Let `dfs(node)` be the *excess* number of coins in the subtree at or below this `node`: namely, the number of coins in the subtree, minus the number of nodes in the subtree.  Then, the number of moves we make from this node to and from its children is `abs(dfs(node.left)) + abs(dfs(node.right))`.  After, we have an excess of `node.val + dfs(node.left) + dfs(node.right) - 1` coins at this node.

<iframe src="https://leetcode.com/playground/9mtBQnVp/shared" frameBorder="0" width="100%" height="327" name="9mtBQnVp"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the tree.

* Space Complexity:  $$O(H)$$, where $$H$$ is the height of the tree.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
