# 1079 - Sum of Root To Leaf Binary Numbers

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/) |


-----------

```
Given a binary tree, each node has value `0` or `1`.  Each root-to-leaf path
represents a binary number starting with the most significant bit.  For
example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent
`01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from
the root to that leaf.

Return the sum of these numbers.



**Example 1:**

![](https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-
numbers.png)

    
    
    **Input:** [1,0,1,0,1,0,1]
    **Output:** 22
    **Explanation:** (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
    



**Note:**

  1. The number of nodes in the tree is between `1` and `1000`.
  2. node.val is `0` or `1`.
  3. The answer will not exceed `2^31 - 1`.
```

-----------

## Thought:
