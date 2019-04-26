# 0098 - Validate Binary Search Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree, Depth-first Search | [Leetcode](https://leetcode.com/problems/validate-binary-search-tree) | [solution](https://leetcode.com/problems/validate-binary-search-tree/solution/)


-----------

<p>Given a binary tree, determine if it is a valid binary search tree (BST).</p>

<p>Assume a BST is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
    2
   / \
  1   3
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
    5
   / \
  1   4
&nbsp;    / \
&nbsp;   3   6
<strong>Output:</strong> false
<strong>Explanation:</strong> The input is: [5,1,4,null,null,3,6]. The root node&#39;s value
&nbsp;            is 5 but its right child&#39;s value is 4.
</pre>


-----------


## Similar Problems

- [Medium] [Binary Tree Inorder Traversal](binary-tree-inorder-traversal)

- [Easy] [Find Mode in Binary Search Tree](find-mode-in-binary-search-tree)




## Solution:

[TOC]

## Solution

--- 

#### Tree definition

First of all, here is the definition of the ```TreeNode``` which we would use.

<iframe src="https://leetcode.com/playground/Dg4SeitH/shared" frameBorder="0" width="100%" height="225" name="Dg4SeitH"></iframe>
<br />
<br />


---
#### Intuition

On the first sight, the problem is trivial. Let's traverse the tree
and check at each step if `node.right.val > node.val` and 
`node.left.val < node.val`. This approach would even work for some
trees 
![compute](../Figures/98/98_not_bst.png)

The problem is this approach will not work for all cases. 
Not only the right child should be larger than the node 
but all the 
elements in the right subtree. Here is an example :

![compute](../Figures/98/98_not_bst_3.png)

That means one should keep both upper 
and lower limits for each node while traversing the tree, 
and compare the node value not
with children values but with these limits.
<br />
<br />


---
#### Approach 1: Recursion

The idea above could be implemented as a recursion.
One compares the node value with its upper and lower limits
if they are available. Then one repeats the same 
step recursively for left and right subtrees. 

<!--![LIS](../Figures/98/98_tr.gif)-->
!?!../Documents/98_LIS.json:1000,462!?!

<iframe src="https://leetcode.com/playground/76WDbVmU/shared" frameBorder="0" width="100%" height="446" name="76WDbVmU"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N)$$ since we visit each node exactly once. 
* Space complexity : $$\mathcal{O}(N)$$ since we keep up to the entire tree.

<br />
<br />


---
#### Approach 2: Iteration

The above recursion could be converted into iteration, 
with the help of stack. DFS would be better than BFS since 
it works faster here.

<iframe src="https://leetcode.com/playground/Qd5k8r2w/shared" frameBorder="0" width="100%" height="500" name="Qd5k8r2w"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N)$$ since we visit each node exactly once. 
* Space complexity : $$\mathcal{O}(N)$$ since we keep up to the entire tree.
<br />
<br />


---
#### Approach 3: Inorder traversal

**Algorithm**

Let's use the order of nodes in the 
[inorder traversal](https://leetcode.com/articles/binary-tree-inorder-traversal/) 
`Left -> Node -> Right`.

![postorder](../Figures/145_transverse.png)

Here the nodes are enumerated in the order you visit them, 
and you could follow `1-2-3-4-5` to compare different strategies.

`Left -> Node -> Right` order of inorder traversal 
means for BST that each element should be smaller 
than the next one.

Hence the algorithm with $$\mathcal{O}(N)$$ time complexity 
and $$\mathcal{O}(N)$$ space complexity could be simple:

- Compute inorder traversal list `inorder`.

- Check if each element in `inorder` is smaller than the next one.

![postorder](../Figures/98/98_bst_inorder.png)

> Do we need to keep the whole `inorder` traversal list? 

Actually, no. The last added inorder element is enough 
to ensure at each step that the tree is BST (or not).
Hence one could merge both steps into one and
reduce the used space.

**Implementation**

<iframe src="https://leetcode.com/playground/JK5dCFdt/shared" frameBorder="0" width="100%" height="429" name="JK5dCFdt"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N)$$ in the worst case
when the tree is BST or the "bad" element is a rightmost leaf.
 
* Space complexity : $$\mathcal{O}(N)$$ to keep `stack`.

Analysis written by @[liaison](https://leetcode.com/liaison/)
and @[andvary](https://leetcode.com/andvary/)
