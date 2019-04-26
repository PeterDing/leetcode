# 0627 - Swap Salary

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/swap-salary) | [solution](https://leetcode.com/problems/swap-salary/solution/)


-----------

<p>Given a table <code>salary</code>, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a <strong>single update statement</strong> and no intermediate temp table.</p>

<p>Note that you must write a single update statement, <strong>DO NOT</strong> write any select statement for this problem.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
</pre>
After running your <strong>update</strong> statement, the above salary table should have the following rows:

<pre>
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
</pre>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach: Using `UPDATE` and `CASE...WHEN` [Accepted]

**Algorithm**

To dynamically set a value to a column, we can use [`UPDATE`](https://dev.mysql.com/doc/refman/5.7/en/update.html) statement together when [`CASE...WHEN...`](https://dev.mysql.com/doc/refman/5.7/en/case.html) flow control statement.

**MySQL**

```sql
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;
```
