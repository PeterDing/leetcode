# 0620 - Not Boring Movies

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/not-boring-movies) | [solution](https://leetcode.com/problems/not-boring-movies/solution/)


-----------

X city opened a new cinema, many people would like to go to this cinema. The cinema also gives out a poster indicating the movies&rsquo; ratings and descriptions.
<p>Please write a SQL query to output movies with an odd numbered ID and a description that is not &#39;boring&#39;. Order the result by rating.</p>

<p>&nbsp;</p>

<p>For example, table <code>cinema</code>:</p>

<pre>
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
</pre>
For the example above, the output should be:

<pre>
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+
</pre>

<p>&nbsp;</p>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach: Using `MOD()` function [Accepted]

**Algorithm**

We can use the `mod(id,2)=1` to determine the odd id, and then add a `description != 'boring'` should address this problem.

**MySQL**

```sql
select *
from cinema
where mod(id, 2) = 1 and description != 'boring'
order by rating DESC
;
```