# 0183 - Customers Who Never Order

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/customers-who-never-order) | [solution](https://leetcode.com/problems/customers-who-never-order/solution/)


-----------

<p>Suppose that a website contains two tables, the <code>Customers</code> table and the <code>Orders</code> table. Write a SQL query to find all customers who never order anything.</p>

<p>Table: <code>Customers</code>.</p>

<pre>
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
</pre>

<p>Table: <code>Orders</code>.</p>

<pre>
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
</pre>

<p>Using the above tables as example, return the following:</p>

<pre>
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
</pre>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach: Using sub-query and `NOT IN` clause [Accepted]

**Algorithm**

If we have a list of customers who have ever ordered, it will be easy to know who never ordered.

We can use the following code to get such list.

```sql
select customerid from orders;
```

Then, we can use `NOT IN` to query the customers who are not in this list.

**MySQL**

```sql
select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid from orders
);
```
