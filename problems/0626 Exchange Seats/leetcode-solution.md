# 0626 - Exchange Seats

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/exchange-seats) | [solution](https://leetcode.com/problems/exchange-seats/solution/)


-----------

<p>Mary is a teacher in a middle school and she has a table <code>seat</code> storing students&#39; names and their corresponding seat ids.</p>
The column <b>id</b> is continuous increment.

<p>&nbsp;</p>
Mary wants to change seats for the adjacent students.

<p>&nbsp;</p>
Can you write a SQL query to output the result for Mary?

<p>&nbsp;</p>

<pre>
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
</pre>
For the sample input, the output is:

<p>&nbsp;</p>

<pre>
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
</pre>

<p><b>Note:</b><br />
If the number of students is odd, there is no need to change the last one&#39;s seat.</p>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach I: Using flow control statement `CASE` [Accepted]

**Algorithm**

For students with odd id, the new id is (id+1) after switch unless it is the last seat. And for students with even id, the new id is (id-1). In order to know how many seats in total, we can use a subquery:
```sql
SELECT
    COUNT(*) AS counts
FROM
    seat
```

Then, we can use the `CASE` statement and `MOD()` function to alter the seat id of each student.

**MySQL**

```sql
SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END) AS id,
    student
FROM
    seat,
    (SELECT
        COUNT(*) AS counts
    FROM
        seat) AS seat_counts
ORDER BY id ASC;
```

#### Approach II: Using bit manipulation and `COALESCE()` [Accepted]

**Algorithm**

Bit manipulation expression `(id+1)^1-1` can calculate the new id after switch.
```sql
SELECT id, (id+1)^1-1, student FROM seat;
```

```
| id | (id+1)^1-1 | student |
|----|------------|---------|
| 1  | 2          | Abbot   |
| 2  | 1          | Doris   |
| 3  | 4          | Emerson |
| 4  | 3          | Green   |
| 5  | 6          | Jeames  |
```

Then, we can make a temp table and join seat with this table like below.
```sql
SELECT
    *
FROM
    seat s1
        LEFT JOIN
    seat s2 ON (s1.id+1)^1-1 = s2.id
ORDER BY s1.id;
```
```
| id | student | id | student |
|----|---------|----|---------|
| 1  | Abbot   | 2  | Doris   |
| 2  | Doris   | 1  | Abbot   |
| 3  | Emerson | 4  | Green   |
| 4  | Green   | 3  | Emerson |
| 5  | Jeames  |    |         |
```
>Note:The first two columns are from s1 and the last two are from s2.

At last, we can output s1.id and s2.student. However, the s2.student is NULL for seat id '5' but s1.student is right. Thus, we we can use function [`COALESCE()`](https://dev.mysql.com/doc/refman/5.7/en/comparison-operators.html#function_coalesce) to generate the correct output for the last record.

**MySQL**

```sql
SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
ORDER BY s1.id;
```
>Note: This solution comes from [@FANGXIAOFANG](https://discuss.leetcode.com/user/fangxiaofang).
