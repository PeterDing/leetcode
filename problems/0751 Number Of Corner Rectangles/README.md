# 0751 - Number Of Corner Rectangles

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/number-of-corner-rectangles/description/) |


-----------

```
Given a start IP address `ip` and a number of ips we need to cover `n`, return
a representation of the range as a list (of smallest possible length) of CIDR
blocks.

A CIDR block is a string consisting of an IP, followed by a slash, and then
the prefix length. For example: "123.45.67.89/20". That prefix length "20"
represents the number of common prefix bits in the specified range.

**Example 1:**


    **Input:** ip = "255.0.0.7", n = 10

**Note:**
    1. `ip` will be a valid IPv4 address.
    2. Every implied address `ip + x` (for `x < n`) will be a valid IPv4 address.
    3. `n` will be an integer in the range `[1, 1000]`.
```

-----------

## Thought: