# 0596 - Classes More Than 5 Students

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/classes-more-than-5-students) | [solution](https://leetcode.com/problems/classes-more-than-5-students/solution/)


-----------

<p>There is a table <code>courses</code> with columns: <b>student</b> and <b>class</b></p>

<p>Please list out all classes which have more than or equal to 5 students.</p>

<p>For example, the table:</p>

<pre>
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
</pre>

<p>Should output:</p>

<pre>
+---------+
| class   |
+---------+
| Math    |
+---------+
</pre>

<p>&nbsp;</p>

<p><b>Note:</b><br />
The students should not be counted duplicate in each course.</p>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach: Using `GROUP BY` clause and **sub-query** [Accepted]

**Intuition**

First, we can count the student number in each class. And then select the ones have more than 5 students.

**Algorithm**

To get the student number in each class. We can use `GROUP BY` and `COUNT`, which is very popular used to statistic bases on some character in a table.

```sql
SELECT
    class, COUNT(DISTINCT student)
FROM
    courses
GROUP BY class
;
```
>Note: We use `DISTINCT` here since the student name may duplicated in a class as it is mentioned int he problem description.

```
| class    | COUNT(student) |
|----------|----------------|
| Biology  | 1              |
| Computer | 1              |
| English  | 1              |
| Math     | 6              |
```
To continue, we can filter the classes by taking the above query as a sub-query.

```sql
SELECT
    class
FROM
    (SELECT
        class, COUNT(DISTINCT student) AS num
    FROM
        courses
    GROUP BY class) AS temp_table
WHERE
    num >= 5
;
```
>Note: Make an alias of `COUNT(student)` ('num' in this case) so that you can use in the `WHERE` clause because it cannot be used directly over there.

#### Approach: Using `GROUP BY` and `HAVING` condition [Accepted]

**Algorithm**

Using sub-query is one way to add some condition to a `GROUP BY` clause, however, using [`HAVING`](https://dev.mysql.com/doc/refman/5.7/en/group-by-handling.html) is another simpler and natural approach. So we can rewrite the above solution as below.

**MySQL**
```sql
SELECT
    class
FROM
    courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5
;
```
