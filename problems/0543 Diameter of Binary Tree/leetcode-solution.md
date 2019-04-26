# 0543 - Diameter of Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/diameter-of-binary-tree) | [solution](https://leetcode.com/problems/diameter-of-binary-tree/solution/)


-----------

<p>
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the <b>longest</b> path between any two nodes in a tree. This path may or may not pass through the root.
</p>

<p>
<b>Example:</b><br />
Given a binary tree <br />
<pre>
          1
         / \
        2   3
       / \     
      4   5    
</pre>
</p>
<p>
Return <b>3</b>, which is the length of the path [4,2,1,3] or [5,2,1,3].
</p>

<p><b>Note:</b>
The length of path between two nodes is represented by the number of edges between them.
</p>

-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Depth-First Search [Accepted]

**Intuition**

Any path can be written as two *arrows* (in different directions) from some node, where an arrow is a path that starts at some node and only travels down to child nodes.

If we knew the maximum length arrows `L, R` for each child, then the best path touches `L + R + 1` nodes.

**Algorithm**

Let's calculate the depth of a node in the usual way: max(depth of node.left, depth of node.right) + 1. While we do, a path "through" this node uses 1 + (depth of node.left) + (depth of node.right) nodes. Let's search each node and remember the highest number of nodes used in some path. The desired length is 1 minus this number.

<iframe src="https://leetcode.com/playground/6ahaRHCG/shared" frameBorder="0" width="100%" height="310" name="6ahaRHCG"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$.  We visit every node once.

* Space Complexity: $$O(N)$$, the size of our implicit call stack during our depth-first search.

---

Analysis written by: [@awice](https://leetcode.com/awice).
