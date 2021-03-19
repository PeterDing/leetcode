# 0100 - Same Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree, Depth-first Search | [Leetcode](https://leetcode.com/problems/same-tree) | [solution](https://leetcode.com/problems/same-tree/solution/)


-----------

<p>Given two binary trees, write a function to check if they are the same or not.</p>

<p>Two binary trees are considered the same if they are structurally identical and the nodes have the same value.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

<strong>Output:</strong> false
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong>     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

<strong>Output:</strong> false
</pre>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---

#### Approach 1: Recursion

**Intuition**

The simplest strategy here is to use recursion. 
Check if `p` and `q` nodes are not `None`, and their values are equal.
If all checks are OK, do the same for the child nodes
recursively.

**Implementation**

!?!../Documents/100_LIS.json:1000,373!?!

<iframe src="https://leetcode.com/playground/CtxuC6Za/shared" frameBorder="0" width="100%" height="395" name="CtxuC6Za"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N)$$, 
where N is a number of nodes in the tree, since one visits
each node exactly once.
 
* Space complexity : $$\mathcal{O}(\log(N))$$ in the best case of completely 
balanced tree and $$\mathcal{O}(N)$$ in the worst case
of completely unbalanced tree, to keep a recursion stack.
<br />
<br />


---
#### Approach 2: Iteration

**Intuition**

Start from the root and then at each iteration 
pop the current node out of the deque. Then do the same checks as in
 the approach 1 :

- `p` and `p` are not `None`, 

- `p.val` is equal to `q.val`,

and if checks are OK, push the child nodes. 

**Implementation**

<iframe src="https://leetcode.com/playground/e9Z7Jfqf/shared" frameBorder="0" width="100%" height="500" name="e9Z7Jfqf"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N)$$ since each node is visited
exactly once.
 
* Space complexity : $$\mathcal{O}(\log(N))$$ in the best case of completely 
balanced tree and $$\mathcal{O}(N)$$ in the worst case
of completely unbalanced tree, to keep a deque.

Analysis written by @[liaison](https://leetcode.com/liaison/)
and @[andvary](https://leetcode.com/andvary/)
