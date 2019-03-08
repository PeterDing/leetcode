# 1038 - Number of Squareful Arrays

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math, Backtracking, Graph | [Leetcode](https://leetcode.com/problems/number-of-squareful-arrays/description/) |


-----------

```
Given an array `A` of non-negative integers, the array is _squareful_ if for
every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations
`A1` and `A2` differ if and only if there is some index `i` such that `A1[i]
!= A2[i]`.



**Example 1:**

    
    
    **Input:** [1,17,8]
    **Output:** 2
    **Explanation:**
    [1,8,17] and [17,8,1] are the valid permutations.
    

**Example 2:**

    
    
    **Input:** [2,2,2]
    **Output:** 1
    



**Note:**

  1. `1 <= A.length <= 12`
  2. `0 <= A[i] <= 1e9`
```

-----------

## Thought:
