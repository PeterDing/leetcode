# 0694 - Number of Distinct Islands

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/number-of-distinct-islands/description/) |


-----------

```
Given a non-empty 2D array `grid` of 0's and 1's, an island is a group of
`1`'s (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same
as another if and only if one island can be translated (and not rotated or
reflected) to equal the other.

Example 1:



    11000

Given the above grid map, return `1`.



Example 2:



    11011

Given the above grid map, return `3`.

Notice that:



    11

and



     1

are considered different island shapes, because we do not consider reflection
/ rotation.



Note: The length of each dimension in the given `grid` does not exceed 50.
```

-----------

## Thought: