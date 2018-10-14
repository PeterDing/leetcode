# 0930 - All Possible Full Binary Trees

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree, Recursion | [Leetcode](https://leetcode.com/problems/all-possible-full-binary-trees/description/) |


-----------

```
A _full binary tree_  is a binary tree where each node has exactly 0 or 2
children.

Return a list of all possible full binary trees with `N` nodes.  Each element
of the answer is the root node of one possible tree.

Each `node` of each tree in the answer **must** have `node.val = 0`.

You may return the final list of trees in any order.



**Example 1:**

    
    
    **Input:** 7
    **Output:** [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    **Explanation:**
    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png)
    



**Note:**

  * `1 <= N <= 20`
```

-----------

## Thought:
