# 0687 - Longest Univalue Path

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree, Recursion | [Leetcode](https://leetcode.com/problems/longest-univalue-path) | [solution](https://leetcode.com/problems/longest-univalue-path/solution/)


-----------

<p>Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.</p>

<p>The length of path between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<p><strong>Input:</strong></p>

<pre>
              5
             / \
            4   5
           / \   \
          1   1   5
</pre>

<p><strong>Output:</strong>&nbsp;2</p>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<p><strong>Input:</strong></p>

<pre>
              1
             / \
            4   5
           / \   \
          4   4   5
</pre>

<p><strong>Output:</strong>&nbsp;2</p>

<p>&nbsp;</p>

<p><b>Note:</b> The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.</p>


-----------


## Similar Problems

- [Hard] [Binary Tree Maximum Path Sum](binary-tree-maximum-path-sum)

- [Medium] [Count Univalue Subtrees](count-univalue-subtrees)

- [Easy] [Path Sum III](path-sum-iii)




## Solution:

[TOC]

#### Approach #1: Recursion [Accepted]

**Intuition**

We can think of any path (of nodes with the same values) as up to two arrows extending from it's root.

Specifically, the *root* of a path will be the unique node such that the parent of that node does not appear in the path, and an *arrow* will be a path where the root only has one child node in the path.

Then, for each node, we want to know what is the longest possible arrow extending left, and the longest possible arrow extending right?  We can solve this using recursion.

**Algorithm**

Let `arrow_length(node)` be the length of the longest arrow that extends from the `node`.  That will be `1 + arrow_length(node.left)` if `node.left` exists and has the same value as `node`.  Similarly for the `node.right` case.

While we are computing arrow lengths, each candidate answer will be the sum of the arrows in both directions from that node.  We record these candidate answers and return the best one.

<iframe src="https://leetcode.com/playground/DjHbgZUi/shared" frameBorder="0" name="DjHbgZUi" width="100%" height="428"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of nodes in the tree.  We process every node once.

* Space Complexity: $$O(H)$$, where $$H$$ is the height of the tree.  Our recursive call stack could be up to $$H$$ layers deep.

---

Analysis written by: [@awice](https://leetcode.com/awice)
