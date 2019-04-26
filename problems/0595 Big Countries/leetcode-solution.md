# 0595 - Big Countries

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/big-countries) | [solution](https://leetcode.com/problems/big-countries/solution/)


-----------

<p>There is a table <code>World</code></p>

<pre>
+-----------------+------------+------------+--------------+---------------+
| name            | continent  | area       | population   | gdp           |
+-----------------+------------+------------+--------------+---------------+
| Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
| Albania         | Europe     | 28748      | 2831741      | 12960000      |
| Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
| Andorra         | Europe     | 468        | 78115        | 3712000       |
| Angola          | Africa     | 1246700    | 20609294     | 100990000     |
+-----------------+------------+------------+--------------+---------------+
</pre>

<p>A country is big if it has an area of bigger than 3 million square km or a population of more than 25 million.</p>

<p>Write a SQL solution to output big countries&#39; name, population and area.</p>

<p>For example, according to the above table, we should output:</p>

<pre>
+--------------+-------------+--------------+
| name         | population  | area         |
+--------------+-------------+--------------+
| Afghanistan  | 25500100    | 652230       |
| Algeria      | 37100000    | 2381741      |
+--------------+-------------+--------------+
</pre>

<p>&nbsp;</p>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach I: Using `WHERE` clause and `OR` [Accepted]

**Intuition**

Use `WHERE` clause in SQL to filter these records and get the target countries.

**Algorithm**

According to the definition, a big country meets at least one of the following two conditions:
1. It has an area of bigger than 3 million square km.
2. It has a population of more than 25 million.

So for the first condition, we can use the following code to get the big countries of this type.
```sql
SELECT name, population, area FROM world WHERE area > 3000000
```

In addition, we can use below code to get big countries of more than 25 million people.
```sql
SELECT name, population, area FROM world WHERE population > 25000000
```

As most people may already come into mind, we can use `OR` to combine these two solutions for the two sub-problems together.

**MySQL**

```sql
SELECT
    name, population, area
FROM
    world
WHERE
    area > 3000000 OR population > 25000000
;
```

#### Approach II: Using `WHERE` clause and `UNION` [Accepted]

**Algorithm**

The idea of this approach is the same as the first one. However, we use `UNION` instead of `OR`.

**MySQL**

```sql
SELECT
    name, population, area
FROM
    world
WHERE
    area > 3000000

UNION

SELECT
    name, population, area
FROM
    world
WHERE
    population > 25000000
;
```
>Note: This solution runs a little bit faster than the first one. However, they do not have big difference.
