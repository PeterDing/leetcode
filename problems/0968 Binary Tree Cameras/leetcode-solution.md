# 0968 - Binary Tree Cameras

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming, Tree, Depth-first Search | [Leetcode](https://leetcode.com/problems/binary-tree-cameras) | [solution](https://leetcode.com/problems/binary-tree-cameras/solution/)


-----------

<p>Given a binary tree, we install cameras on the nodes of the tree.&nbsp;</p>

<p>Each camera at&nbsp;a node can monitor <strong>its parent, itself, and its immediate children</strong>.</p>

<p>Calculate the minimum number of cameras needed to monitor all nodes of the tree.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png" style="width: 138px; height: 163px;" />
<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[0,0,null,0,0]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>One camera is enough to monitor all nodes if placed as shown.
</pre>

<div>
<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png" style="width: 139px; height: 312px;" />
<pre>
<strong>Input: </strong><span id="example-input-2-1">[0,0,null,0,null,0,null,null,0]</span>
<strong>Output: </strong><span id="example-output-2">2
<strong>Explanation:</strong> At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.</span>
</pre>

<p><br />
<strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the given tree will be in the range&nbsp;<code>[1, 1000]</code>.</li>
	<li><strong>Every</strong> node has value 0.</li>
</ol>
</div>
</div>


-----------


## Similar Problems

- [Medium] [Distribute Coins in Binary Tree](distribute-coins-in-binary-tree)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

Let's try to cover every node, starting from the top of the tree and working down.  Every node considered must be covered by a camera at that node or some neighbor.

Because cameras only care about local state, we can hope to leverage this fact for an efficient solution.  Specifically, when deciding to place a camera at a node, we might have placed cameras to cover some subset of this node, its left child, and its right child already.

**Algorithm**

Let `solve(node)` be some information about how many cameras it takes to cover the subtree at this node in various states.  There are essentially 3 states:

* [State 0] Strict subtree:  All the nodes below this node are covered, but not this node.
* [State 1] Normal subtree:  All the nodes below and including this node are covered, but there is no camera here.
* [State 2] Placed camera:  All the nodes below and including this node are covered, and there is a camera here (which may cover nodes above this node).

Once we frame the problem in this way, the answer falls out:

* To cover a strict subtree, the children of this node must be in state 1.
* To cover a normal subtree without placing a camera here, the children of this node must be in states 1 or 2, and at least one of those children must be in state 2.
* To cover the subtree when placing a camera here, the children can be in any state.

<iframe src="https://leetcode.com/playground/4oJtky7i/shared" frameBorder="0" width="100%" height="480" name="4oJtky7i"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(H)$$, where $$H$$ is the height of the given tree.
<br />
<br />


---
#### Approach 2: Greedy

**Intuition**

Instead of trying to cover every node from the top down, let's try to cover it from the bottom up - considering placing a camera with the deepest nodes first, and working our way up the tree.

If a node has its children covered and has a parent, then it is strictly better to place the camera at this node's parent.

**Algorithm**

If a node has children that are not covered by a camera, then we must place a camera here.  Additionally, if a node has no parent and it is not covered, we must place a camera here.

<iframe src="https://leetcode.com/playground/Zhw2ojEo/shared" frameBorder="0" width="100%" height="500" name="Zhw2ojEo"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(H)$$, where $$H$$ is the height of the given tree.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
