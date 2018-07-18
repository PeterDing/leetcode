# 0582 - Kill Process

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/kill-process/description/) |


-----------

```
Given n processes, each process has a unique PID (process id) and its PPID
(parent process id).

Each process only has one parent process, but may have one or more children
processes. This is just like a tree structure. Only one process has PPID that
is 0, which means this process has no parent process. All the PIDs will be
distinct positive integers.

We use two list of integers to represent a list of processes, where the first
list contains PID for each process and the second list contains the
corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill,
return a list of PIDs of processes that will be killed in the end. You should
assume that when a process is killed, all its children processes will be
killed. No order is required for the final answer.

Example 1:



    Input: 



Note:

  1. The given kill id is guaranteed to be one of the given PIDs.
  2. n >= 1.
```

-----------

## Thought: