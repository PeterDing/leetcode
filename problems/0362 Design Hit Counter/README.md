# 0362 - Design Hit Counter

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/design-hit-counter/description/) |


-----------

```
Design a hit counter which counts the number of hits received in the past 5
minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you
may assume that calls are being made to the system in chronological order (ie,
the timestamp is monotonically increasing). You may assume that the earliest
timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

**Example:**


    HitCounter counter = new HitCounter();

**Follow up:**
What if the number of hits per second could be very large? Does your design
scale?

**Credits:**
Special thanks to [@elmirap](https://discuss.leetcode.com/user/elmirap) for
adding this problem and creating all test cases.
```

-----------

## Thought: