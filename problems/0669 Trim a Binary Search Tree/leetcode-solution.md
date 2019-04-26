# 0669 - Trim a Binary Search Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/trim-a-binary-search-tree) | [solution](https://leetcode.com/problems/trim-a-binary-search-tree/solution/)


-----------

<p>
Given a binary search tree and the lowest and highest boundaries as <code>L</code> and <code>R</code>, trim the tree so that all its elements lies in <code>[L, R]</code> (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
    1
   / \
  0   2

  L = 1
  R = 2

<b>Output:</b> 
    1
      \
       2
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

<b>Output:</b> 
      3
     / 
   2   
  /
 1
</pre>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach #1: Recursion [Accepted]

**Intuition**

Let `trim(node)` be the desired answer for the subtree at that node.  We can construct the answer recursively.

**Algorithm**

When $$\text{node.val > R}$$, we know that the trimmed binary tree must occur to the left of the node. Similarly, when $$\text{node.val < L}$$, the trimmed binary tree occurs to the right of the node. Otherwise, we will trim both sides of the tree.

<iframe src="https://leetcode.com/playground/8eWsgDRM/shared" frameBorder="0" name="8eWsgDRM" width="100%" height="309"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the total number of nodes in the given tree.  We visit each node at most once.

* Space Complexity: $$O(N)$$.  Even though we don't explicitly use any additional memory, the call stack of our recursion could be as large as the number of nodes in the worst case.

---
Analysis written by: [@awice](https://leetcode.com/awice)
