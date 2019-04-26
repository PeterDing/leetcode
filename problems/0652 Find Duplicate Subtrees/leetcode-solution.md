# 0652 - Find Duplicate Subtrees

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/find-duplicate-subtrees) | [solution](https://leetcode.com/problems/find-duplicate-subtrees/solution/)


-----------

<p>Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any <b>one</b> of them.</p>

<p>Two trees are duplicate if they have the same structure with same node values.</p>

<p><b>Example 1: </b></p>

<pre>
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
</pre>

<p>The following are two duplicate subtrees:</p>

<pre>
      2
     /
    4
</pre>

<p>and</p>

<pre>
    4
</pre>
Therefore, you need to return above trees&#39; root in the form of a list.

-----------


## Similar Problems

- [Hard] [Serialize and Deserialize Binary Tree](serialize-and-deserialize-binary-tree)

- [Medium] [Serialize and Deserialize BST](serialize-and-deserialize-bst)

- [Easy] [Construct String from Binary Tree](construct-string-from-binary-tree)




## Solution:

[TOC]

---
#### Approach #1: Depth-First Search [Accepted]

**Intuition**

We can serialize each subtree.  For example, the tree
```python
   1
  / \
 2   3
    / \
   4   5
```

can be represented as the serialization `1,2,#,#,3,4,#,#,5,#,#`, which is a unique representation of the tree.

**Algorithm**

Perform a depth-first search, where the recursive function returns the serialization of the tree.  At each node, record the result in a map, and analyze the map after to determine duplicate subtrees.

<iframe src="https://leetcode.com/playground/4UyWd7Zu/shared" frameBorder="0" width="100%" height="378" name="4UyWd7Zu"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the number of nodes in the tree.  We visit each node once, but each creation of `serial` may take $$O(N)$$ work.

* Space Complexity: $$O(N^2)$$, the size of `count`.

---
#### Approach #2: Unique Identifier [Accepted]

**Intuition**

Suppose we have a unique identifier for subtrees: two subtrees are the same if and only if they have the same id.

Then, for a node with left child id of `x` and right child id of `y`, `(node.val, x, y)` uniquely determines the tree.

**Algorithm**

If we have seen the triple `(node.val, x, y)` before, we can use the identifier we've remembered.  Otherwise, we'll create a new one.

<iframe src="https://leetcode.com/playground/sgdon7Zu/shared" frameBorder="0" width="100%" height="480" name="sgdon7Zu"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of nodes in the tree.  We visit each node once.

* Space Complexity: $$O(N)$$.  Every structure we use is using $$O(1)$$ storage per node.

---

Analysis written by: [@awice](https://leetcode.com/awice).  Approach #2 inspired by [@StefanPochmann](https://discuss.leetcode.com/topic/97625/o-n-time-and-space-lots-of-analysis).
