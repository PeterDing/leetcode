# 0196 - Delete Duplicate Emails

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/delete-duplicate-emails) | [solution](https://leetcode.com/problems/delete-duplicate-emails/solution/)


-----------

<p>Write a SQL query to <strong>delete</strong> all duplicate email entries in a table named <code>Person</code>, keeping only unique emails based on its <i>smallest</i> <b>Id</b>.</p>

<pre>
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
</pre>

<p>For example, after running your query, the above <code>Person</code> table should have the following rows:</p>

<pre>
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
</pre>

<p><strong>Note:</strong></p>

<p>Your output is the whole <code>Person</code>&nbsp;table after executing your sql. Use <code>delete</code> statement.</p>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach: Using `DELETE` and `WHERE` clause [Accepted]

**Algorithm**

By joining this table with itself on the *Email* column, we can get the following code.
```sql
SELECT p1.*
FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email
;
```

Then we need to find the bigger id having same email address with other records. So we can add a new condition to the `WHERE` clause like this.

```sql
SELECT p1.*
FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
;
```

As we already get the records to be deleted, we can alter this statement to `DELETE` in the end.

**MySQL**

```sql
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
```
