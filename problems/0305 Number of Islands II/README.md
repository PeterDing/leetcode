# 0305 - Number of Islands II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard |  | [Leetcode](https://leetcode.com/problems/number-of-islands-ii/description/) |


-----------

```
A 2d grid map of `m` rows and `n` columns is initially filled with water. We
may perform an _addLand_ operation which turns the water at position (row,
col) into a land. Given a list of positions to operate, count the number of
islands after each _addLand_ operation. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may
assume all four edges of the grid are all surrounded by water.

Example:

Given `m = 3, n = 3`, `positions = [[0,0], [0,1], [1,2], [2,1]]`.
Initially, the 2d grid `grid` is filled with water. (Assume 0 represents water
and 1 represents land).



    0 0 0

Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.



    1 0 0

Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.



    1 1 0

Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.



    1 1 0

Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.



    1 1 0

We return the result as an array: `[1, 1, 2, 3]`

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the
`positions`?
```

-----------

## Thought: