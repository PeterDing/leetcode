# 0938 - Range Sum of BST

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Binary Search Tree | [Leetcode](https://leetcode.com/problems/range-sum-of-bst) | [solution](https://leetcode.com/problems/range-sum-of-bst/solution/)


-----------

<p>Given the <code>root</code> node of a binary search tree, return the sum of values of all nodes with value between <code>L</code> and <code>R</code> (inclusive).</p>

<p>The binary search tree is guaranteed to have unique values.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[10,5,15,3,7,null,18]</span>, L = <span id="example-input-1-2">7</span>, R = <span id="example-input-1-3">15</span>
<strong>Output: </strong><span id="example-output-1">32</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-2-1">[10,5,15,3,7,13,18,1,null,6]</span>, L = <span id="example-input-2-2">6</span>, R = <span id="example-input-2-3">10</span>
<strong>Output: </strong><span id="example-output-2">23</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the tree is at most <code>10000</code>.</li>
	<li>The final answer is guaranteed to be less than <code>2^31</code>.</li>
</ol>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Depth First Search

**Intuition and Algorithm**

We traverse the tree using a depth first search.  If `node.val` falls outside the range `[L, R]`, (for example `node.val < L`), then we know that only the right branch could have nodes with value inside `[L, R]`.

We showcase two implementations - one using a recursive algorithm, and one using an iterative one.

**Recursive Implementation**

<iframe src="https://leetcode.com/playground/zwwcTGCT/shared" frameBorder="0" width="100%" height="378" name="zwwcTGCT"></iframe>

**Iterative Implementation**

<iframe src="https://leetcode.com/playground/LyVV4ZSy/shared" frameBorder="0" width="100%" height="378" name="LyVV4ZSy"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the tree.

* Space Complexity:  $$O(H)$$, where $$H$$ is the height of the tree.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
