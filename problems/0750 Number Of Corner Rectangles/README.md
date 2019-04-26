# 0750 - Number Of Corner Rectangles

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/number-of-corner-rectangles) | [solution](https://leetcode.com/problems/number-of-corner-rectangles/solution/)


-----------

```
Given a grid where each entry is only 0 or 1, find the number of corner
rectangles. A _corner rectangle_ is 4 distinct 1s on the grid that form an
axis-aligned rectangle. Note that only the corners need to have the value 1.
Also, all four 1s used must be distinct. Example 1: Input: grid = [[1, 0, 0,
1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]] Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2],
grid[1][4], grid[3][2], grid[3][4]. Example 2: Input: grid = [[1, 1, 1], [1,
1, 1], [1, 1, 1]] Output: 9 Explanation: There are four 2x2 rectangles, four
2x3 and 3x2 rectangles, and one 3x3 rectangle. Example 3: Input: grid = [[1,
1, 1, 1]] Output: 0 Explanation: Rectangles must have four distinct corners.
Note: 1\. The number of rows and columns of `grid` will each be in the range
`[1, 200]`. 2\. Each `grid[i][j]` will be either `0` or `1`. 3\. The number of
`1`s in the grid will be at most `6000`.```

-----------


## Similar Problems




## Thought:
