# 0007 - Reverse Integer

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/reverse-integer) | [solution](https://leetcode.com/problems/reverse-integer/solution/)

-----------

<p>Given a 32-bit signed integer, reverse digits of an integer.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 123
<strong>Output:</strong> 321
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -123
<strong>Output:</strong> -321
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 120
<strong>Output:</strong> 21
</pre>

<p><strong>Note:</strong><br />
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.</p>


-----------


## Similar Problems

- [Medium] [String to Integer (atoi)](string-to-integer-atoi)

- [Easy] [Reverse Bits](reverse-bits)




## Thought:

```python
n = xxxx
r = 0
i = 0
while True:
    if n == 0:
        break
    m = n % 10
    r = r * (10 ** i) + m
    n = n // 10
return r
```

