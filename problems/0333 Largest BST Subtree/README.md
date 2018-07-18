# 0333 - Largest BST Subtree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/largest-bst-subtree/description/) |


-----------

```
Given a binary tree, find the largest subtree which is a Binary Search Tree
(BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:



        10

The Largest BST Subtree in this case is the highlighted one.
The return value is the subtree's size, which is 3.



Hint:

  1. You can recursively use algorithm similar to [98\. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) at each node of the tree, which will result in O(nlogn) time complexity.

Follow up:
Can you figure out ways to solve it with O(n) time complexity?
```

-----------

## Thought: