# 0286 - Walls and Gates

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/walls-and-gates/description/) |


-----------

```
You are given a _m x n_ 2D grid initialized with these three possible values.

  1. `-1` \- A wall or an obstacle.
  2. `0` \- A gate.
  3. `INF` \- Infinity means an empty room. We use the value `231 - 1 = 2147483647` to represent `INF` as you may assume that the distance to a gate is less than `2147483647`.

Fill each empty room with the distance to its _nearest_ gate. If it is
impossible to reach a gate, it should be filled with `INF`.

For example, given the 2D grid:


    INF  -1  0  INF

After running your function, the 2D grid should be:


      3  -1   0   1
```

-----------

## Thought: