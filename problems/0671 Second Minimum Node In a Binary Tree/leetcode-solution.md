# 0671 - Second Minimum Node In a Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree) | [solution](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/solution/)


-----------

<p>Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly <code>two</code> or <code>zero</code> sub-node. If the node has two sub-nodes, then this node&#39;s value is the smaller value among its two sub-nodes.</p>

<p>Given such a binary tree, you need to output the <b>second minimum</b> value in the set made of all the nodes&#39; value in the whole tree.</p>

<p>If no such second minimum value exists, output -1 instead.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 
    2
   / \
  2   5
     / \
    5   7

<b>Output:</b> 5
<b>Explanation:</b> The smallest value is 2, the second smallest value is 5.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 
    2
   / \
  2   2

<b>Output:</b> -1
<b>Explanation:</b> The smallest value is 2, but there isn&#39;t any second smallest value.
</pre>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [Kth Smallest Element in a BST](kth-smallest-element-in-a-bst)




## Solution:

[TOC]

## Solution

---
#### Approach #1: Brute Force [Accepted]

**Intuition and Algorithm**

Traverse the tree with a depth-first search, and record every unique value in the tree using a Set structure `uniques`.

Then, we'll look through the recorded values for the second minimum.  The first minimum must be $$\text{root.val}$$.

<iframe src="https://leetcode.com/playground/rVYM4qCQ/shared" frameBorder="0" name="rVYM4qCQ" width="100%" height="394"></iframe>


**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the total number of nodes in the given tree.  We visit each node exactly once, and scan through the $$O(N)$$ values in `unique` once.

* Space Complexity: $$O(N)$$, the information stored in `uniques`.

---
#### Approach #2: Ad-Hoc [Accepted]

**Intuition and Algorithm**

Let $$\text{min1 = root.val}$$.  When traversing the tree at some node, $$\text{node}$$, if $$\text{node.val > min1}$$, we know all values in the subtree at $$\text{node}$$ are at least $$\text{node.val}$$, so there cannot be a better candidate for the second minimum in this subtree.  Thus, we do not need to search this subtree.

Also, as we only care about the second minimum $$\text{ans}$$, we do not need to record any values that are larger than our current candidate for the second minimum, so unlike Approach #1 we can skip maintaining a Set of values(`uniques`) entirely.


<iframe src="https://leetcode.com/playground/btTLPkjK/shared" frameBorder="0" name="btTLPkjK" width="100%" height="394"></iframe>


**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the total number of nodes in the given tree.  We visit each node at most once.

* Space Complexity: $$O(N)$$.  The information stored in $$\text{ans}$$ and $$\text{min1}$$ is $$O(1)$$, but our depth-first search may store up to $$O(h) = O(N)$$ information in the call stack, where $$h$$ is the height of the tree.

---
Analysis written by: [@awice](https://leetcode.com/awice)
