# 0351 - Android Unlock Patterns

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/android-unlock-patterns) | [solution](https://leetcode.com/problems/android-unlock-patterns/solution/)


-----------

```
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n
≤ 9, count the total number of unlock patterns of the Android lock screen,
which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:

  1. Each pattern must connect at least m keys and at most n keys.
  2. All the keys must be distinct.
  3. If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
  4. The order of keys used matters.



![](https://discuss.leetcode.com/uploads/files/1461680355228-cptqh.png)

Explanation:



    | 1 | 2 | 3 || 4 | 5 | 6 || 7 | 8 | 9 |



Invalid move: `4 - 1 - 3 - 6 `
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: `4 - 1 - 9 - 2`
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: `2 - 4 - 1 - 3 - 6`
Line 1 - 3 is valid because it passes through key 2, which had been selected
in the pattern

Valid move: `6 - 5 - 4 - 1 - 9 - 2`
Line 1 - 9 is valid because it passes through key 5, which had been selected
in the pattern.

Example:
Given m = 1, n = 1, return 9.

Credits:
Special thanks to [@elmirap](https://discuss.leetcode.com/user/elmirap) for
adding this problem and creating all test cases.
```

-----------


## Similar Problems




## Thought:
