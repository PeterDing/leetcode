# 0548 - Split Array with Equal Sum

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/split-array-with-equal-sum/description/) |


-----------

```
Given an array with n integers, you need to find if there are triplets (i, j,
k) which satisfies following conditions:

  1. 0 < i, i + 1 < j, j + 1 < k < n - 1
  2. Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.

where we define that subarray (L, R) represents a slice of the original array
starting from the element indexed L to the element indexed R.

**Example:**


    **Input:** [1,2,1,2,1,2,1]

**Note:**

  1. 1 <= n <= 2000.
  2. Elements in the given array will be in range [-1,000,000, 1,000,000].
```

-----------

## Thought: