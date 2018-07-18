# 0356 - Line Reflection

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/line-reflection/description/) |


-----------

```
Given n points on a 2D plane, find if there is such a line parallel to y-axis
that reflect the given set of points.

**Example 1:**
Given _points_ = `[[1,1],[-1,1]]`, return `true`.

**Example 2:**
Given _points_ = `[[1,1],[-1,-1]]`, return `false`.

**Follow up:**
Could you do better than O(_n_2)?

**Hint:**

  1. Find the smallest and largest x-value for all points.
  2. If there is a line then it should be at y = (minX + maxX) / 2.
  3. For each point, make sure that it has a reflected point in the opposite side.

**Credits:**
Special thanks to [@memoryless](https://discuss.leetcode.com/user/memoryless)
for adding this problem and creating all test cases.
```

-----------

## Thought:
