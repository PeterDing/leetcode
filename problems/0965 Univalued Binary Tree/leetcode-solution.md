# 0965 - Univalued Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/univalued-binary-tree) | [solution](https://leetcode.com/problems/univalued-binary-tree/solution/)


-----------

<p>A binary tree is <em>univalued</em> if every node in the tree has the same value.</p>

<p>Return <code>true</code>&nbsp;if and only if the given tree is univalued.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png" style="width: 265px; height: 172px;" />
<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,1,1,1,1,null,1]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png" style="width: 198px; height: 169px;" />
<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,2,2,5,2]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the given tree will be in the range <code>[1, 100]</code>.</li>
	<li>Each node&#39;s value will be an integer in the range <code>[0, 99]</code>.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Depth-First Search

**Intuition and Algorithm**

Let's output all the values of the array.  After, we can check that they are all equal.

To output all the values of the array, we perform a depth-first search.

<iframe src="https://leetcode.com/playground/dL2Yo8pb/shared" frameBorder="0" width="100%" height="378" name="dL2Yo8pb"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Recursion

**Intuition and Algorithm**

A tree is univalued if both its children are univalued, plus the root node has the same value as the child nodes.

We can write our function recursively.  `left_correct` will represent that the left child is correct: ie., that it is univalued, and the root value is equal to the left child's value.  `right_correct` will represent the same thing for the right child.  We need both of these properties to be true.

<iframe src="https://leetcode.com/playground/xLY6bNWX/shared" frameBorder="0" width="100%" height="208" name="xLY6bNWX"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(H)$$, where $$H$$ is the height of the given tree.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
