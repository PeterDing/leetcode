# 0919 - Complete Binary Tree Inserter

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/complete-binary-tree-inserter) | [solution](https://leetcode.com/problems/complete-binary-tree-inserter/solution/)


-----------

<p>A <em>complete</em> binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.</p>

<p>Write a data structure&nbsp;<code>CBTInserter</code>&nbsp;that is initialized with a complete binary tree and supports the following operations:</p>

<ul>
	<li><code>CBTInserter(TreeNode root)</code> initializes the data structure on a given tree&nbsp;with head node <code>root</code>;</li>
	<li><code>CBTInserter.insert(int v)</code> will insert a <code>TreeNode</code>&nbsp;into the tree with value <code>node.val =&nbsp;v</code>&nbsp;so that the tree remains complete, <strong>and returns the value of the parent of the inserted <code>TreeNode</code></strong>;</li>
	<li><code>CBTInserter.get_root()</code> will return the head node of the tree.</li>
</ul>

<ol>
</ol>

<div>
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>inputs = <span id="example-input-1-1">[&quot;CBTInserter&quot;,&quot;insert&quot;,&quot;get_root&quot;]</span>, inputs = <span id="example-input-1-2">[[[1]],[2],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,1,[1,2]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>inputs = <span id="example-input-2-1">[&quot;CBTInserter&quot;,&quot;insert&quot;,&quot;insert&quot;,&quot;get_root&quot;]</span>, inputs = <span id="example-input-2-2">[[[1,2,3,4,5,6]],[7],[8],[]]</span>
<strong>Output: </strong><span id="example-output-2">[null,3,4,[1,2,3,4,5,6,7,8]]</span></pre>
</div>

<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The initial given tree is complete and contains between <code>1</code> and <code>1000</code> nodes.</li>
	<li><code>CBTInserter.insert</code> is called at most <code>10000</code> times per test case.</li>
	<li>Every value of a given or inserted node is between <code>0</code> and <code>5000</code>.</li>
</ol>
</div>
</div>

<div>
<p>&nbsp;</p>

<div>&nbsp;</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Deque

**Intuition**

Consider all the nodes numbered first by level and then left to right.  Call this the "number order" of the nodes.

At each insertion step, we want to insert into the node with the lowest number (that still has 0 or 1 children).

By maintaining a `deque` (double ended queue) of these nodes in number order, we can solve the problem.  After inserting a node, that node now has the highest number and no children, so it goes at the end of the deque.  To get the node with the lowest number, we pop from the beginning of the deque.

**Algorithm**

First, perform a breadth-first search to populate the `deque` with nodes that have 0 or 1 children, in number order.

Now when inserting a node, the parent is the first element of `deque`, and we add this new node to our `deque`.

<iframe src="https://leetcode.com/playground/vJC78XQe/shared" frameBorder="0" width="100%" height="500" name="vJC78XQe"></iframe>

**Complexity Analysis**

* Time Complexity:  The preprocessing is $$O(N)$$, where $$N$$ is the number of nodes in the tree.  Each insertion operation thereafter is $$O(1)$$.

* Space Complexity:  $$O(N_{\text{cur}})$$ space complexity, when the size of the tree during the current insertion operation is $$N_{\text{cur}}$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
