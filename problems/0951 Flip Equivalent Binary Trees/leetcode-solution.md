# 0951 - Flip Equivalent Binary Trees

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/flip-equivalent-binary-trees) | [solution](https://leetcode.com/problems/flip-equivalent-binary-trees/solution/)


-----------

<p>For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.</p>

<p>A binary tree X&nbsp;is <em>flip equivalent</em> to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.</p>

<p>Write a function that determines whether two binary trees&nbsp;are <em>flip equivalent</em>.&nbsp; The trees are given by root nodes <code>root1</code> and <code>root2</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>root1 = <span id="example-input-1-1">[1,2,3,4,5,6,null,null,null,7,8]</span>, root2 = <span id="example-input-1-2">[1,3,2,null,6,4,5,null,null,null,null,8,7]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>We flipped at nodes with values 1, 3, and 5.
<img alt="Flipped Trees Diagram" src="https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png" style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;; width: 455px; height: 200px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>Each tree will have at most <code>100</code> nodes.</li>
	<li>Each value in each tree will be a unique&nbsp;integer in the range <code>[0, 99]</code>.</li>
</ol>

<div>
<p>&nbsp;</p>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Recursion

**Intuition**

If `root1` and `root2` have the same root value, then we only need to check if their children are equal (up to ordering.)

**Algorithm**

There are 3 cases:

* If `root1` or `root2` is `null`, then they are equivalent if and only if they are both `null`.

* Else, if `root1` and `root2` have different values, they aren't equivalent.

* Else, let's check whether the children of `root1` are equivalent to the children of `root2`.  There are two different ways to pair these children.

<iframe src="https://leetcode.com/playground/wjoLqdDo/shared" frameBorder="0" width="100%" height="242" name="wjoLqdDo"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(min(N_1, N_2))$$, where $$N_1, N_2$$ are the lengths of `root1` and `root2`.

* Space Complexity:  $$O(min(H_1, H_2))$$, where $$H_1, H_2$$ are the heights of the trees of `root1` and `root2`.
<br />
<br />


---
#### Approach 2: Canonical Traversal

**Intuition**

Flip each node so that the left child is smaller than the right, and call this the *canonical representation*.  All equivalent trees have exactly one canonical representation.

**Algorithm**

We can use a depth-first search to compare the canonical representation of each tree.  If the traversals are the same, the representations are equal.

When traversing, we should be careful to encode both when we enter or leave a node.

<iframe src="https://leetcode.com/playground/PZJH2Hcn/shared" frameBorder="0" width="100%" height="500" name="PZJH2Hcn"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N_1 + N_2)$$, where $$N_1, N_2$$ are the lengths of `root1` and `root2`.  (In Python, this is $$\min(N_1, N_2)$$.)

* Space Complexity:  $$O(N_1 + N_2)$$.  (In Python, this is $$\min(H_1, H_2)$$, where $$H_1, H_2$$ are the heights of the trees of `root1` and `root2`.)
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
