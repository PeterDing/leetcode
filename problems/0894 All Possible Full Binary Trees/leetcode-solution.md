# 0894 - All Possible Full Binary Trees

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree, Recursion | [Leetcode](https://leetcode.com/problems/all-possible-full-binary-trees) | [solution](https://leetcode.com/problems/all-possible-full-binary-trees/solution/)


-----------

<p>A <em>full binary tree</em>&nbsp;is a binary tree where each node has exactly 0 or 2&nbsp;children.</p>

<p>Return a list of all possible full binary trees with <code>N</code> nodes.&nbsp; Each element of the answer is the root node of one possible tree.</p>

<p>Each <code>node</code> of each&nbsp;tree in the answer <strong>must</strong> have <code>node.val = 0</code>.</p>

<p>You may return the final list of trees in any order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">7</span>
<strong>Output: </strong><span id="example-output-1">[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]</span>
<strong>Explanation:</strong>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png" style="width: 700px; height: 400px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 20</code></li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Recursion

**Intuition and Algorithm**

Let $$\text{FBT}(N)$$ be the list of all possible full binary trees with $$N$$ nodes.

Every full binary tree $$T$$ with 3 or more nodes, has 2 children at its root.  Each of those children `left` and `right` are themselves full binary trees.

Thus, for $$N \geq 3$$, we can formulate the recursion: $$\text{FBT}(N) =$$ [All trees with left child from $$\text{FBT}(x)$$ and right child from $$\text{FBT}(N-1-x)$$, for all $$x$$].

Also, by a simple counting argument, there are no full binary trees with a positive, even number of nodes.

Finally, we should cache previous results of the function $$\text{FBT}$$ so that we don't have to recalculate them in our recursion.

<iframe src="https://leetcode.com/playground/MNvnRoUP/shared" frameBorder="0" width="100%" height="497" name="MNvnRoUP"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(2^N)$$.  For odd $$N$$, let $$N = 2k + 1$$.  Then, $$\Big| \text{FBT}(N) \Big| = C_k$$, the $$k$$-th catalan number; and $$\sum\limits_{k < \frac{N}{2}} C_k$$ (the complexity involved in computing intermediate results required) is bounded by $$O(2^N)$$.  However, the proof is beyond the scope of this article.

* Space Complexity:  $$O(2^N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
