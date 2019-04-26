# 0872 - Leaf-Similar Trees

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree, Depth-first Search | [Leetcode](https://leetcode.com/problems/leaf-similar-trees) | [solution](https://leetcode.com/problems/leaf-similar-trees/solution/)


-----------

<p>Consider all the leaves of a binary tree.&nbsp; From&nbsp;left to right order, the values of those&nbsp;leaves form a <em>leaf value sequence.</em></p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png" style="width: 300px; height: 240px;" /></p>

<p>For example, in the given tree above, the leaf value sequence is <code>(6, 7, 4, 9, 8)</code>.</p>

<p>Two binary trees are considered <em>leaf-similar</em>&nbsp;if their leaf value sequence is the same.</p>

<p>Return <code>true</code> if and only if the two given trees with head nodes <code>root1</code> and <code>root2</code> are leaf-similar.</p>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Both of the given trees will have between <code>1</code> and <code>100</code> nodes.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Depth First Search

**Intuition and Algorithm**

Let's find the leaf value sequence for both given trees.  Afterwards, we can compare them to see if they are equal or not.

To find the leaf value sequence of a tree, we use a depth first search.  Our `dfs` function writes the node's value if it is a leaf, and then recursively explores each child.  This is guaranteed to visit each leaf in left-to-right order, as left-children are fully explored before right-children.

<iframe src="https://leetcode.com/playground/2esZiYkH/shared" frameBorder="0" width="100%" height="378" name="2esZiYkH"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(T_1 + T_2)$$, where $$T_1, T_2$$ are the lengths of the given trees.

* Space Complexity:  $$O(T_1 + T_2)$$, the space used in storing the leaf values.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
