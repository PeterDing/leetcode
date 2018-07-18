# 0352 - Data Stream as Disjoint Intervals

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Binary Search Tree | [Leetcode](https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/) |


-----------

```
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]


Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?


Credits:Special thanks to @yunhong for adding this problem and creating most of the test cases.
```

-----------

## Thought:
