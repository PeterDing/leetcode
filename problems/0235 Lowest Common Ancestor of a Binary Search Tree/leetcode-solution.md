# 0235 - Lowest Common Ancestor of a Binary Search Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree) | [solution](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/)


-----------

<p>Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: &ldquo;The lowest common ancestor is defined between two nodes p and q&nbsp;as the lowest node in T that has both p and q&nbsp;as descendants (where we allow <b>a node to be a descendant of itself</b>).&rdquo;</p>

<p>Given binary search tree:&nbsp; root =&nbsp;[6,2,8,0,4,7,9,null,null,3,5]</p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;" />
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>Output:</strong> 6
<strong>Explanation: </strong>The LCA of nodes <code>2</code> and <code>8</code> is <code>6</code>.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>Output:</strong> 2
<strong>Explanation: </strong>The LCA of nodes <code>2</code> and <code>4</code> is <code>2</code>, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All of the nodes&#39; values will be unique.</li>
	<li>p and q are different and both values will&nbsp;exist in the BST.</li>
</ul>


-----------


## Similar Problems

- [Medium] [Lowest Common Ancestor of a Binary Tree](lowest-common-ancestor-of-a-binary-tree)




## Solution:

[TOC]

## Solution

We can solve this using the approaches to find [LCA in a binary tree](https://leetcode.com/articles/lowest-common-ancestor-of-a-binary-tree/).

But, binary search tree's property could be utilized, to come up with a better algorithm.

Lets review properties of a BST:
>1. Left subtree of a node N contains nodes whose values are lesser than or equal to node N's value.
>2. Right subtree of a node N contains nodes whose values are greater than node N's value.
>3. Both left and right subtrees are also BSTs.

#### Approach 1: Recursive Approach

**Intuition**

Lowest common ancestor for two nodes `p` and `q` would be the last ancestor node common to both of them. Here `last` is defined in terms of the depth of the node. The below diagram would help in understanding what `lowest` means.

<center>
<img src="../Figures/235/235_LCA_Binary_1.png" width="600"/>
</center>

Note: One of `p` or `q` would be in the left subtree and the other in the right subtree of the LCA node.

Following cases are possible:
<center>
<img src="../Figures/235/235_LCA_Binary_2.png" width="600"/>
</center>

**Algorithm**

1. Start traversing the tree from the root node.
2. If both the nodes `p` and `q` are in the right subtree, then continue the search with right subtree starting step 1.
3. If both the nodes `p` and `q` are in the left subtree, then continue the search with left subtree starting step 1.
4. If both step 2 and step 3 are not true, this means we have found the node which is common to node `p`'s and `q`'s subtrees.
and hence we return this common node as the LCA.

<iframe src="https://leetcode.com/playground/A7ZULghS/shared" frameBorder="0" width="100%" height="497" name="A7ZULghS"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.

* Space Complexity: $$O(N)$$. This is because the maximum amount of space utilized by the recursion stack would be $$N$$ since the height of a skewed BST could be $$N$$.
<br/>
<br/>

---

#### Approach 2: Iterative Approach

**Algorithm**

The steps taken are also similar to approach 1. The only difference is instead of recursively calling the function, we traverse down the tree iteratively. This is possible without using a stack or recursion since we don't need to backtrace to find the LCA node. In essence of it the problem is iterative, it just wants us to find the split point. The point from where `p` and `q` won't be part of the same subtree or when one is the parent of the other.

<iframe src="https://leetcode.com/playground/PfXQUZfN/shared" frameBorder="0" width="100%" height="500" name="PfXQUZfN"></iframe>

**Complexity Analysis**

* Time Complexity : $$O(N)$$, where $$N$$ is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.

* Space Complexity : $$O(1)$$.
<br/>

---
Analysis written by: [@godayaldivya](https://leetcode.com/godayaldivya/).
