# 0176 - Second Highest Salary

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/second-highest-salary) | [solution](https://leetcode.com/problems/second-highest-salary/solution/)


-----------

<p>Write a SQL query to get the second highest salary from the <code>Employee</code> table.</p>

<pre>
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
</pre>

<p>For example, given the above Employee table, the query should return <code>200</code> as the second highest salary. If there is no second highest salary, then the query should return <code>null</code>.</p>

<pre>
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
</pre>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach: Using sub-query and `LIMIT` clause [Accepted]

**Algorithm**

Sort the distinct salary in descend order and then utilize the [`LIMIT`](https://dev.mysql.com/doc/refman/5.7/en/select.html) clause to get the second highest salary.

```sql
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
```

However, this solution will be judged as 'Wrong Answer' if there is no such second highest salary since there might be only one record in this table. To overcome this issue, we can take this as a temp table.

**MySQL**

```sql
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```

#### Approach: Using `IFNULL` and `LIMIT` clause [Accepted]

Another way to solve the 'NULL' problem is to use `IFNULL` funtion as below.

**MySQL**
```sql
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
```
