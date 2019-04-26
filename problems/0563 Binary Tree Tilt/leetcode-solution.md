# 0563 - Binary Tree Tilt

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/binary-tree-tilt) | [solution](https://leetcode.com/problems/binary-tree-tilt/solution/)


-----------

<p>Given a binary tree, return the tilt of the <b>whole tree</b>.</p>

<p>The tilt of a <b>tree node</b> is defined as the <b>absolute difference</b> between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.</p>

<p>The tilt of the <b>whole tree</b> is defined as the sum of all nodes' tilt.</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> 
         1
       /   \
      2     3
<b>Output:</b> 1
<b>Explanation:</b> 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
</pre>
</p>

<p><b>Note:</b>
<ol>
<li>The sum of node values in any subtree won't exceed the range of 32-bit integer. </li>
<li>All the tilt values won't exceed the range of 32-bit integer.</li>
</ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]


## Solution

---
#### Approach 1: Using Recursion

**Algorithm**

From the problem statement, it is clear that we need to find the tilt value at every node of the given tree and add up all the tilt values to obtain the final result. To find the tilt value at any node, we need to subtract the sum of all the nodes in its left subtree and the sum of all the nodes in its right subtree. 

Thus, to find the solution, we make use of a recursive function `traverse` which when called from any node, returns the sum of the nodes below the current node including itself. With the help of such sum values for the right and left subchild of any node, we can directly obtain the tilt value corresponding to that node.

The below animation depicts how the value passing and tilt calculation:

!?!../Documents/563_Binary.json:1000,563!?!

<iframe src="https://leetcode.com/playground/kegZTTSb/shared" frameBorder="0" width="100%" height="480" name="kegZTTSb"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. where $$n$$ is the number of nodes. Each node is visited once.
* Space complexity : $$O(n)$$. In worst case when the tree is skewed depth of tree will be $$n$$. In average case depth will be $$\log n$$.

---

Analysis written by: [@vinod23](https://leetcode.com/vinod23)
