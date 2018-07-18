# 0635 - Design Log Storage System

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/design-log-storage-system/description/) |


-----------

```
You are given several logs that each log contains a unique id and timestamp.
Timestamp is a string that has the following format:
`Year:Month:Day:Hour:Minute:Second`, for example, `2017:01:01:23:59:59`. All
domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

`void Put(int id, string timestamp)`: Given a log's unique id and timestamp,
store the log in your storage system.



`int[] Retrieve(String start, String end, String granularity)`: Return the id
of logs whose timestamps are within the range from start to end. Start and end
all have the same format as timestamp. However, granularity means the time
level for consideration. For example, start = "2017:01:01:23:59:59", end =
"2017:01:02:23:59:59", granularity = "Day", it means that we need to find the
logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:



    put(1, "2017:01:01:23:59:59");



Note:

  1. There will be at most 300 operations of Put or Retrieve.
  2. Year ranges from [2000,2017]. Hour ranges from [00,23].
  3. Output for Retrieve has no order required.
```

-----------

## Thought: