# 0958 - Check Completeness of a Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/check-completeness-of-a-binary-tree) | [solution](https://leetcode.com/problems/check-completeness-of-a-binary-tree/solution/)


-----------

<p>Given a binary tree, determine if it is a <em>complete binary tree</em>.</p>

<p><u><b>Definition of a complete binary tree from <a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a>:</b></u><br />
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2<sup>h</sup> nodes inclusive at the last level h.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png" style="width: 180px; height: 145px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4,5,6]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<span><strong>Explanation: </strong></span>Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png" style="width: 200px; height: 145px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,3,4,5,null,7]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>The node with value 7 isn&#39;t as far left as possible.<span>
</span></pre>

<div>&nbsp;</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li>The tree will have between 1 and 100 nodes.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Breadth First Search

**Intuition**

This problem reduces to two smaller problems: representing the "location" of each node as a `(depth, position)` pair, and formalizing what it means for nodes to all be left-justified.

If we have say, 4 nodes in a row with depth 3 and positions 0, 1, 2, 3; and we want 8 new nodes in a row with depth 4 and positions 0, 1, 2, 3, 4, 5, 6, 7; then we can see that the rule for going from a node to its left child is `(depth, position) -> (depth + 1, position * 2)`, and the rule for going from a node to its right child is `(depth, position) -> (depth + 1, position * 2 + 1)`.  Then, our row at depth $$d$$ is completely filled if it has $$2^{d-1}$$ nodes, and all the nodes in the last level are left-justified when their positions take the form `0, 1, ...` in sequence with no gaps.

A cleaner way to represent depth and position is with a code: `1` will be the root node, and for any node with code `v`, the left child will be `2*v` and the right child will be `2*v + 1`.  This is the scheme we will use.  Under this scheme, our tree is complete if the codes take the form `1, 2, 3, ...` in sequence with no gaps.

**Algorithm**

At the root node, we will associate it with the code `1`.  Then, for each node with code `v`, we will associate its left child with code `2 * v`, and its right child with code `2 * v + 1`.

We can find the codes of every node in the tree in "reading order" (top to bottom, left to right) sequence using a breadth first search.  (We could also use a depth first search and sort the codes later.)

Then, we check that the codes are the sequence `1, 2, 3, ...` with no gaps.  Actually, we only need to check that the last code is correct, since the last code is the largest value.


<iframe src="https://leetcode.com/playground/JXyfvuSS/shared" frameBorder="0" width="100%" height="480" name="JXyfvuSS"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the tree.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
