# 0272 - Closest Binary Search Tree Value II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard |  | [Leetcode](https://leetcode.com/problems/closest-binary-search-tree-value-ii) | [solution](https://leetcode.com/problems/closest-binary-search-tree-value-ii/solution/)


-----------

```
Given a non-empty binary search tree and a target value, find  _k_  values in
the BST that are closest to the target.
Note:
  * Given target value is a floating point.
  * You may assume  _k_  is always valid, that is:  _k_  ≤ total nodes.
  * You are guaranteed to have only one unique set of  _k_  values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than  _O_ ( _n_ )
runtime (where  _n_  = total nodes)?
Hint:
1\. Consider implement these two helper functions:
i. getPredecessor(N), which returns the next smaller node to N.
ii. getSuccessor(N), which returns the next larger node to N.
2\. Try to assume that each node has a parent pointer, it makes the problem
much easier.
3\. Without parent pointer we just need to keep track of the path from the
root to the current node using a stack.
4\. You would need two stacks to track the path in finding predecessor and
successor node separately.
```

-----------


## Similar Problems




## Thought:
