# 1021 - Distribute Coins in Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree, Depth-first Search | [Leetcode](https://leetcode.com/problems/distribute-coins-in-binary-tree/description/) |


-----------

```
Given the `root` of a binary tree with `N` nodes, each `node` in the tree has
`node.val` coins, and there are `N` coins total.

In one move, we may choose two adjacent nodes and move one coin from one node
to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.



**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/01/18/tree1.png)**

    
    
    **Input:** [3,0,0]
    **Output:** 2
    **Explanation:** From the root of the tree, we move one coin to its left child, and one coin to its right child.
    

**Example 2:**

**![](https://assets.leetcode.com/uploads/2019/01/18/tree2.png)**

    
    
    **Input:** [0,3,0]
    **Output:** 3
    **Explanation:** From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
    

**Example 3:**

**![](https://assets.leetcode.com/uploads/2019/01/18/tree3.png)**

    
    
    **Input:** [1,0,2]
    **Output:** 2
    

**Example 4:**

**![](https://assets.leetcode.com/uploads/2019/01/18/tree4.png)**

    
    
    **Input:** [1,0,0,null,3]
    **Output:** 4
    



**Note:**

  1. `1<= N <= 100`
  2. `0 <= node.val <= N`
```

-----------

## Thought:
