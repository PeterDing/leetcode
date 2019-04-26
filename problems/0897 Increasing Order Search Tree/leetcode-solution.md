# 0897 - Increasing Order Search Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree, Depth-first Search | [Leetcode](https://leetcode.com/problems/increasing-order-search-tree) | [solution](https://leetcode.com/problems/increasing-order-search-tree/solution/)


-----------

<p>Given a tree, rearrange the tree in <strong>in-order</strong> so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
&nbsp;/        / \ 
1        7   9

<strong>Output:</strong> [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
&nbsp; \
&nbsp;  2
&nbsp;   \
&nbsp;    3
&nbsp;     \
&nbsp;      4
&nbsp;       \
&nbsp;        5
&nbsp;         \
&nbsp;          6
&nbsp;           \
&nbsp;            7
&nbsp;             \
&nbsp;              8
&nbsp;               \
                 9  </pre>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the given tree will be between 1 and 100.</li>
	<li>Each node will have a unique integer value from 0 to 1000.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: In-Order Traversal

**Intuition**

The definition of a binary search tree is that for every node, all the values of the left branch are less than the value at the root, and all the values of the right branch are greater than the value at the root.

Because of this, an *in-order traversal* of the nodes will yield all the values in increasing order.

**Algorithm**

Once we have traversed all the nodes in increasing order, we can construct new nodes using those values to form the answer.

<iframe src="https://leetcode.com/playground/RonWhYrN/shared" frameBorder="0" width="100%" height="378" name="RonWhYrN"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(N)$$, the size of the answer.
<br />
<br />


---
#### Approach 2: Traversal with Relinking

**Intuition and Algorithm**

We can perform the same in-order traversal as in *Approach 1*.  During the traversal, we'll construct the answer on the fly, reusing the nodes of the given tree by cutting their left child and adjoining them to the answer.

<iframe src="https://leetcode.com/playground/5M7CYgmK/shared" frameBorder="0" width="100%" height="361" name="5M7CYgmK"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(H)$$ in *additional* space complexity, where $$H$$ is the height of the given tree, and the size of the implicit call stack in our in-order traversal.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
