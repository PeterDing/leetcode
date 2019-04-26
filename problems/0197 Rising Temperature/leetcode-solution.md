# 0197 - Rising Temperature

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/rising-temperature) | [solution](https://leetcode.com/problems/rising-temperature/solution/)


-----------

<p>Given a <code>Weather</code> table, write a SQL query to find all dates&#39; Ids with higher temperature compared to its previous (yesterday&#39;s) dates.</p>

<pre>
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
</pre>

<p>For example, return the following Ids for the above <code>Weather</code> table:</p>

<pre>
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
</pre>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach: Using `JOIN` and `DATEDIFF()` clause [Accepted]

**Algorithm**

MySQL uses [DATEDIFF](https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_datediff) to compare two date type values.

So, we can get the result by joining this table **weather** with itself and use this `DATEDIFF()` function.

**MySQL**

```sql
SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.date, w.date) = 1
        AND weather.Temperature > w.Temperature
;
```
