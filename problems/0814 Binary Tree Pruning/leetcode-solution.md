# 0814 - Binary Tree Pruning

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/binary-tree-pruning) | [solution](https://leetcode.com/problems/binary-tree-pruning/solution/)


-----------

<p>We are given the head node <code>root</code>&nbsp;of a binary tree, where additionally every node&#39;s value is either a 0 or a 1.</p>

<p>Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.</p>

<p>(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> [1,null,0,0,1]
<strong>Output: </strong>[1,null,0,null,1]
 
<strong>Explanation:</strong> 
Only the red nodes satisfy the property &quot;every subtree not containing a 1&quot;.
The diagram on the right represents the answer.

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png" style="width:450px" />
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> [1,0,1,0,0,0,1]
<strong>Output: </strong>[1,null,1,null,1]


<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png" style="width:450px" />
</pre>

<pre>
<strong>Example 3:</strong>
<strong>Input:</strong> [1,1,0,1,1,0,1,0]
<strong>Output: </strong>[1,1,0,1,1,null,1]


<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png" style="width:450px" />
</pre>

<p><strong>Note: </strong></p>

<ul>
	<li>The binary tree&nbsp;will&nbsp;have&nbsp;at&nbsp;most <code>100 nodes</code>.</li>
	<li>The value of each node will only be <code>0</code> or <code>1</code>.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Recursion [Accepted]

**Intuition**

Prune children of the tree recursively.  The only decisions at each node are whether to prune the left child or the right child.

**Algorithm**

We'll use a function `containsOne(node)` that does two things: it tells us whether the subtree at this `node` contains a `1`, and it also prunes all subtrees not containing `1`.

If for example, `node.left` does not contain a one, then we should prune it via `node.left = null`.

Also, the parent needs to be checked.  If for example the tree is a single node `0`, the answer is an empty tree.

<iframe src="https://leetcode.com/playground/oKrtTG2C/shared" frameBorder="0" width="100%" height="293" name="oKrtTG2C"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the tree.  We process each node once.

* Space Complexity: $$O(H)$$, where $$H$$ is the height of the tree.  This represents the size of the implicit call stack in our recursion.

---

Analysis written by: [@awice](https://leetcode.com/awice).
