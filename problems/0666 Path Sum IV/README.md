# 0666 - Path Sum IV

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/path-sum-iv/description/) |


-----------

```
If the depth of a tree is smaller than `5`, then this tree can be represented
by a list of three-digits integers.

For each integer in this list:

  1. The hundreds digit represents the depth `D` of this node, `1 <= D <= 4.`
  2. The tens digit represents the position `P` of this node in the level it belongs to, `1 <= P <= 8`. The position is the same as that in a full binary tree.
  3. The units digit represents the value `V` of this node, `0 <= V <= 9.`



Given a list of `ascending` three-digits integers representing a binary with
the depth smaller than 5. You need to return the sum of all paths from the
root towards the leaves.

Example 1:



    Input: [113, 215, 221]



Example 2:



    Input: [113, 221]
```

-----------

## Thought: