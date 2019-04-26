# 0184 - Department Highest Salary

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/department-highest-salary) | [solution](https://leetcode.com/problems/department-highest-salary/solution/)


-----------

<p>The <code>Employee</code> table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.</p>

<pre>
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2 &nbsp;| Jim &nbsp; | 90000 &nbsp;| 1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
</pre>

<p>The <code>Department</code> table holds all departments of the company.</p>

<pre>
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
</pre>

<p>Write a SQL query to find employees who have the highest salary in each of the departments.&nbsp;For the above tables, your SQL query should return the following rows (order of rows does not matter).</p>

<pre>
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT &nbsp; &nbsp; &nbsp; &nbsp; | Jim &nbsp; &nbsp; &nbsp;| 90000 &nbsp;|
| Sales      | Henry    | 80000  |
+------------+----------+--------+
</pre>

<p><strong>Explanation:</strong></p>

<p>Max and Jim both have&nbsp;the highest salary in the IT department and Henry has the highest salary in the Sales department.</p>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach: Using `JOIN` and `IN` clause [Accepted]

**Algorithm**

Since the **Employee** table contains the *Salary* and *DepartmentId* information, we can query the highest salary in a department.

```sql
SELECT
    DepartmentId, MAX(Salary)
FROM
    Employee
GROUP BY DepartmentId;
```
>Note: There might be multiple employees having the same highest salary, so it is safe not to include the employee name information in this query.

```
| DepartmentId | MAX(Salary) |
|--------------|-------------|
| 1            | 90000       |
| 2            | 80000       |
```

Then, we can join table **Employee** and **Department**, and query the (DepartmentId, Salary) are in the temp table using `IN` statement as below.

**MySQL**

```sql
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)
;
```
```
| Department | Employee | Salary |
|------------|----------|--------|
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
```
