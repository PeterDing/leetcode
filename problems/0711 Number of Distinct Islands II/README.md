# 0711 - Number of Distinct Islands II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard |  | [Leetcode](https://leetcode.com/problems/number-of-distinct-islands-ii/description/) |


-----------

```
Given a non-empty 2D array `grid` of 0's and 1's, an island is a group of
`1`'s (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same
as another if they have the same shape, or have the same shape after rotation
(90, 180, or 270 degrees only) or reflection (left/right direction or up/down
direction).

Example 1:



    11000100000000100011

Given the above grid map, return `1`.

Notice that:



    111

and



     111

are considered same island shapes. Because if we make a 180 degrees clockwise
rotation on the first island, then two islands will have the same shapes.



Example 2:



    11100100010100101110

Given the above grid map, return `2`.

Here are the two distinct islands:



    1111

and



    11


Notice that:



    1111

and



    1111

are considered same island shapes. Because if we flip the first array in the
up/down direction, then they have the same shapes.



Note: The length of each dimension in the given `grid` does not exceed 50.



s



posted @ 2018-03-10 23:55 [Grandyang](http://www.cnblogs.com/grandyang/)
阅读(...) 评论(...) [编辑](https://i.cnblogs.com/EditPosts.aspx?postid=8542820) 收藏

[刷新评论](javascript:void\(0\);)刷新页面返回顶部

### 公告

Copyright (C)2018 Grandyang
```

-----------

## Thought:
