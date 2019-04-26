# 0889 - Construct Binary Tree from Preorder and Postorder Traversal

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal) | [solution](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/solution/)


-----------

<p>Return any binary tree that matches the given preorder and postorder traversals.</p>

<p>Values in the traversals&nbsp;<code>pre</code> and <code>post</code>&nbsp;are distinct&nbsp;positive integers.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>pre = <span id="example-input-1-1">[1,2,4,5,3,6,7]</span>, post = <span id="example-input-1-2">[4,5,2,6,7,3,1]</span>
<strong>Output: </strong><span id="example-output-1">[1,2,3,4,5,6,7]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ul>
	<li><code>1 &lt;= pre.length == post.length &lt;= 30</code></li>
	<li><code>pre[]</code> and <code>post[]</code>&nbsp;are both permutations of <code>1, 2, ..., pre.length</code>.</li>
	<li>It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.</li>
</ul>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Recursion

**Intuition**

A preorder traversal is:

* `(root node) (preorder of left branch) (preorder of right branch)`

While a postorder traversal is:

* `(postorder of left branch) (postorder of right branch) (root node)`

For example, if the final binary tree is `[1, 2, 3, 4, 5, 6, 7]` (serialized), then the preorder traversal is `[1] + [2, 4, 5] + [3, 6, 7]`, while the postorder traversal is `[4, 5, 2] + [6, 7, 3] + [1]`.

If we knew how many nodes the left branch had, we could partition these arrays as such, and use recursion to generate each branch of the tree.

**Algorithm**

Let's say the left branch has $$L$$ nodes.  We know the head node of that left branch is `pre[1]`, but it also occurs last in the postorder representation of the left branch.  So `pre[1] = post[L-1]` (because of uniqueness of the node values.)  Hence, `L = post.indexOf(pre[1]) + 1`.

Now in our recursion step, the left branch is represnted by `pre[1 : L+1]` and `post[0 : L]`, while the right branch is represented by `pre[L+1 : N]` and `post[L : N-1]`.

<iframe src="https://leetcode.com/playground/rRvx9C7Q/shared" frameBorder="0" width="100%" height="378" name="rRvx9C7Q"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the number of nodes.

* Space Complexity:  $$O(N^2)$$.
<br />
<br />


---
#### Approach 2: Recursion (Space Saving Variant)

**Explanation**

We present a variation of *Approach 1* that uses indexes to refer to the subarrays of `pre` and `post`, instead of passing copies of those subarrays.  Here, `(i0, i1, N)` refers to `pre[i0:i0+N], post[i1:i1+N]`.

<iframe src="https://leetcode.com/playground/P82iKheu/shared" frameBorder="0" width="100%" height="446" name="P82iKheu"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the number of nodes.

* Space Complexity:  $$O(N)$$, the space used by the answer.
<br />
<br />

---


Analysis written by: [@awice](https://leetcode.com/awice).
