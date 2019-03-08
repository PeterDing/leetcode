# 0978 - Valid Mountain Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/valid-mountain-array/description/) |


-----------

```
Given an array `A` of integers, return `true` if and only if it is a _valid
mountain array_.

Recall that A is a mountain array if and only if:

  * `A.length >= 3`
  * There exists some `i` with `0 < i < A.length - 1` such that: 
    * `A[0] < A[1] < ... A[i-1] < A[i] `
    * `A[i] > A[i+1] > ... > A[B.length - 1]`



**Example 1:**

    
    
    **Input:** [2,1]
    **Output:** false
    

**Example 2:**

    
    
    **Input:** [3,5,5]
    **Output:** false
    

**Example 3:**

    
    
    **Input:** [0,3,2,1]
    **Output:** true



**Note:**

  1. `0 <= A.length <= 10000`
  2. `0 <= A[i] <= 10000 `
```

-----------

## Thought:
