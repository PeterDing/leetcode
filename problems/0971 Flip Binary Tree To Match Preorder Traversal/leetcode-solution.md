# 0971 - Flip Binary Tree To Match Preorder Traversal

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree, Depth-first Search | [Leetcode](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal) | [solution](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/solution/)


-----------

<p>Given a binary tree with <code>N</code> nodes, each node has a different value from&nbsp;<code>{1, ..., N}</code>.</p>

<p>A node in this binary tree can be <em>flipped</em>&nbsp;by swapping the left child and the right child of that node.</p>

<p>Consider the sequence of&nbsp;<code>N</code> values reported by a preorder traversal starting from the root.&nbsp; Call such a sequence of <code>N</code> values the&nbsp;<em>voyage</em>&nbsp;of the tree.</p>

<p>(Recall that a <em>preorder traversal</em>&nbsp;of a node means we report the current node&#39;s value, then preorder-traverse the left child, then preorder-traverse the right child.)</p>

<p>Our goal is to flip the <strong>least number</strong> of nodes in the tree so that the voyage of the tree matches the <code>voyage</code> we are given.</p>

<p>If we can do so, then return a&nbsp;list&nbsp;of the values of all nodes flipped.&nbsp; You may return the answer in any order.</p>

<p>If we cannot do so, then return the list <code>[-1]</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-01.png" style="width: 88px; height: 120px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[1,2]</span>, voyage = <span id="example-input-1-2">[2,1]</span>
<strong>Output: </strong><span id="example-output-1">[-1]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 127px; height: 120px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-2-1">[1,2,3]</span>, voyage = <span id="example-input-2-2">[1,3,2]</span>
<strong>Output: </strong><span id="example-output-2">[1]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 127px; height: 120px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-3-1">[1,2,3]</span>, voyage = <span id="example-input-3-2">[1,2,3]</span>
<strong>Output: </strong><span id="example-output-3">[]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 100</code></li>
</ol>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Depth-First Search

**Intuition**

As we do a pre-order traversal, we will flip nodes on the fly to try to match our voyage with the given one.

If we are expecting the next integer in our voyage to be `voyage[i]`, then there is only at most one choice for path to take, as all nodes have different values.

**Algorithm**

Do a depth first search.  If at any node, the node's value doesn't match the voyage, the answer is `[-1]`.

Otherwise, we know when to flip: the next number we are expecting in the voyage `voyage[i]` is different from the next child.

<iframe src="https://leetcode.com/playground/TSMMADqh/shared" frameBorder="0" width="100%" height="500" name="TSMMADqh"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
